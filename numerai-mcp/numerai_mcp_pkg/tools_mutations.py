"""
Mutation tools for the Numerai GraphQL API.

Two tiers:

  * "safe" mutations — model lifecycle, webhooks, bio/links, submissions,
    compute-pickle uploads. These run without an explicit confirmation flag
    because they are reversible or low-blast-radius.

  * "stake" mutations — v2ChangeStake, increaseStake, releaseStake,
    cancelPendingStakeRelease, v3ChangePayoutSelection. These move real NMR
    and are protected by a `confirm: bool = False` argument. Callers must
    explicitly pass `confirm=True` after the user has authorised the action.
    The guard lives in safety.require_confirm().

Operations not wrapped here (deleteAccount, changePassword, v2WithdrawNmr,
revokeApiToken, account auth flows, …) are still reachable via
`graphql_query` if the caller really needs them, but no first-class tool is
provided.
"""

from __future__ import annotations

from typing import Any, Optional

from .client import post_graphql, parse, extract
from . import models as M
from .safety import require_confirm


def register(mcp) -> None:
    # ----------------------------------------------------------------------
    # Safe model lifecycle / metadata
    # ----------------------------------------------------------------------

    @mcp.tool()
    def add_model(name: str, tournament: int) -> dict[str, Any]:
        """Create a new model slot under the authenticated account.

        Returns the newly-created Model (including its UUID).
        """
        query = """
        mutation AddModel($name: String!, $tournament: Int!) {
          addModel(name: $name, tournament: $tournament) {
            id name tournament username
            computeEnabled hidden archived insertedAt profileUrl
          }
        }
        """
        return parse(
            post_graphql(query, variables={"name": name, "tournament": tournament}, use_auth=True),
            "addModel",
            M.Model,
        )

    @mcp.tool()
    def archive_model(model_id: str) -> dict[str, Any]:
        """Archive a model (reversible — use unarchive_model to restore)."""
        query = """
        mutation ArchiveModel($modelId: ID!) {
          archiveModel(modelId: $modelId) {
            id name archived archivedAt
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id}, use_auth=True),
            "archiveModel",
            M.Model,
        )

    @mcp.tool()
    def unarchive_model(model_id: str) -> dict[str, Any]:
        """Restore a previously archived model."""
        query = """
        mutation UnarchiveModel($modelId: ID!) {
          unarchiveModel(modelId: $modelId) {
            id name archived
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id}, use_auth=True),
            "unarchiveModel",
            M.Model,
        )

    @mcp.tool()
    def rename_model(model_id: str, name: str) -> dict[str, Any]:
        """Rename a model. Use model_name_available() first to check the new name."""
        query = """
        mutation RenameModel($modelId: ID!, $name: String!) {
          renameModel(modelId: $modelId, name: $name) {
            id name tournament
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id, "name": name}, use_auth=True),
            "renameModel",
            M.Model,
        )

    @mcp.tool()
    def set_submission_webhook(model_id: Optional[str], new_submission_webhook: Optional[str]) -> dict[str, Any]:
        """Set/update/clear the compute webhook URL for a model.

        Pass `new_submission_webhook=None` (or omit) to clear. The returned
        value is the new webhook URL (or empty string).
        """
        query = """
        mutation SetSubmissionWebhook($modelId: String, $newSubmissionWebhook: String) {
          setSubmissionWebhook(modelId: $modelId, newSubmissionWebhook: $newSubmissionWebhook)
        }
        """
        resp = post_graphql(
            query,
            variables={"modelId": model_id, "newSubmissionWebhook": new_submission_webhook},
            use_auth=True,
        )
        return {"webhook": extract(resp, "setSubmissionWebhook"), "raw": resp}

    @mcp.tool()
    def set_user_bio(value: str, model_id: Optional[str] = None) -> dict[str, Any]:
        """Set the bio for the account or a specific model (if model_id given)."""
        query = """
        mutation SetUserBio($value: String!, $modelId: ID) {
          setUserBio(value: $value, modelId: $modelId)
        }
        """
        resp = post_graphql(query, variables={"value": value, "modelId": model_id}, use_auth=True)
        return {"ok": extract(resp, "setUserBio"), "raw": resp}

    @mcp.tool()
    def set_user_link(link_url: str, link_text: Optional[str] = None, model_id: Optional[str] = None) -> dict[str, Any]:
        """Set the personal/model profile link."""
        query = """
        mutation SetUserLink($linkUrl: String!, $linkText: String, $modelId: ID) {
          setUserLink(linkUrl: $linkUrl, linkText: $linkText, modelId: $modelId)
        }
        """
        resp = post_graphql(
            query,
            variables={"linkUrl": link_url, "linkText": link_text, "modelId": model_id},
            use_auth=True,
        )
        return {"ok": extract(resp, "setUserLink"), "raw": resp}

    @mcp.tool()
    def trigger_model_webhook(model_id: str) -> dict[str, Any]:
        """Manually fire the configured compute webhook for a model."""
        query = """
        mutation TriggerModelWebhook($modelId: String!) {
          triggerModelWebhook(modelId: $modelId)
        }
        """
        resp = post_graphql(query, variables={"modelId": model_id}, use_auth=True)
        return {"result": extract(resp, "triggerModelWebhook"), "raw": resp}

    # ----------------------------------------------------------------------
    # Submissions
    # ----------------------------------------------------------------------

    @mcp.tool()
    def create_submission(
        filename: str,
        tournament: int,
        model_id: Optional[str] = None,
        data_datestamp: Optional[int] = None,
        source: Optional[str] = None,
        trigger_id: Optional[str] = None,
        version: Optional[int] = None,
    ) -> dict[str, Any]:
        """Finalise a Classic-tournament submission after PUT-uploading the CSV.

        Workflow:
          1. submission_upload_auth(filename, tournament, model_id) -> presigned URL
          2. HTTP PUT the CSV bytes to that URL
          3. create_submission(filename, tournament, model_id) -> finalise
        """
        query = """
        mutation CreateSubmission(
          $filename: String!, $tournament: Int!, $modelId: ID,
          $dataDatestamp: Int, $source: String, $triggerId: ID, $version: Int
        ) {
          createSubmission(
            filename: $filename, tournament: $tournament, modelId: $modelId,
            dataDatestamp: $dataDatestamp, source: $source, triggerId: $triggerId, version: $version
          ) {
            id filename insertedAt status dataDatestamp tickersAcceptedCount tickersSubmittedCount
            round { number tournament }
          }
        }
        """
        variables = {
            "filename": filename, "tournament": tournament, "modelId": model_id,
            "dataDatestamp": data_datestamp, "source": source, "triggerId": trigger_id, "version": version,
        }
        return parse(post_graphql(query, variables=variables, use_auth=True), "createSubmission", M.V2Submission)

    @mcp.tool()
    def create_signals_submission(
        filename: str,
        model_id: Optional[str] = None,
        tournament: Optional[int] = None,
        data_datestamp: Optional[int] = None,
        source: Optional[str] = None,
        trigger_id: Optional[str] = None,
        version: Optional[int] = None,
    ) -> dict[str, Any]:
        """Finalise a Signals submission after PUT-uploading the CSV.

        Companion to submission_upload_signals_auth().
        """
        query = """
        mutation CreateSignalsSubmission(
          $filename: String!, $modelId: ID, $tournament: Int,
          $dataDatestamp: Int, $source: String, $triggerId: ID, $version: Int
        ) {
          createSignalsSubmission(
            filename: $filename, modelId: $modelId, tournament: $tournament,
            dataDatestamp: $dataDatestamp, source: $source, triggerId: $triggerId, version: $version
          ) {
            id filename insertedAt status dataDatestamp tickersAcceptedCount tickersSubmittedCount
            round { number tournament }
          }
        }
        """
        variables = {
            "filename": filename, "modelId": model_id, "tournament": tournament,
            "dataDatestamp": data_datestamp, "source": source, "triggerId": trigger_id, "version": version,
        }
        return parse(post_graphql(query, variables=variables, use_auth=True), "createSignalsSubmission", M.V2Submission)

    # ----------------------------------------------------------------------
    # Compute pickle workflow (upload .pkl, register it, assign to a model)
    # ----------------------------------------------------------------------

    @mcp.tool()
    def create_compute_pickle_upload(
        filename: str,
        tournament: int,
        data_version_id: Optional[str] = None,
        docker_image_id: Optional[str] = None,
        model_id: Optional[str] = None,
        source: Optional[str] = None,
    ) -> dict[str, Any]:
        """Register a compute-pickle after PUT-uploading the .pkl bytes.

        Workflow:
          1. compute_pickle_upload_auth(filename) -> presigned URL
          2. HTTP PUT the .pkl to that URL
          3. create_compute_pickle_upload(filename, tournament, data_version_id, docker_image_id, model_id)

        `data_version_id` and `docker_image_id` come from
        compute_pickle_data_versions() and compute_pickle_docker_images()
        respectively.
        """
        query = """
        mutation CreateComputePickleUpload(
          $filename: String!, $tournament: Int!,
          $dataVersionId: ID, $dockerImageId: ID, $modelId: ID, $source: String
        ) {
          createComputePickleUpload(
            filename: $filename, tournament: $tournament,
            dataVersionId: $dataVersionId, dockerImageId: $dockerImageId,
            modelId: $modelId, source: $source
          ) {
            id label filename insertedAt modelId
            dataVersionId dockerImageId triggerStatus validationStatus
          }
        }
        """
        variables = {
            "filename": filename, "tournament": tournament,
            "dataVersionId": data_version_id, "dockerImageId": docker_image_id,
            "modelId": model_id, "source": source,
        }
        return parse(
            post_graphql(query, variables=variables, use_auth=True),
            "createComputePickleUpload",
            M.ComputePickleUpload,
        )

    @mcp.tool()
    def trigger_compute_pickle_upload(
        pickle_id: Optional[str] = None,
        model_id: Optional[str] = None,
        trigger_validation: Optional[bool] = None,
    ) -> dict[str, Any]:
        """Trigger validation/processing for a compute-pickle.

        Pass either `pickle_id` (specific pickle) or `model_id` (latest pickle
        for that model). `trigger_validation=True` runs the validation pipeline.
        """
        query = """
        mutation TriggerComputePickleUpload($pickleId: ID, $modelId: ID, $triggerValidation: Boolean) {
          triggerComputePickleUpload(pickleId: $pickleId, modelId: $modelId, triggerValidation: $triggerValidation) {
            id triggerStatus validationStatus diagnosticsStatus updatedAt
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={"pickleId": pickle_id, "modelId": model_id, "triggerValidation": trigger_validation},
                use_auth=True,
            ),
            "triggerComputePickleUpload",
            M.ComputePickleUpload,
        )

    @mcp.tool()
    def assign_pickle_to_model(pickle_id: str, model_id: str) -> dict[str, Any]:
        """Assign a compute-pickle to a model slot."""
        query = """
        mutation AssignPickleToModel($pickleId: ID, $modelId: String) {
          assignPickleToModel(pickleId: $pickleId, modelId: $modelId)
        }
        """
        resp = post_graphql(
            query,
            variables={"pickleId": pickle_id, "modelId": model_id},
            use_auth=True,
        )
        return {"result": extract(resp, "assignPickleToModel"), "raw": resp}

    @mcp.tool()
    def update_pickle_label(pickle_id: str, label: str) -> dict[str, Any]:
        """Rename a compute-pickle's label."""
        query = """
        mutation UpdatePickleLabel($pickleId: ID!, $label: String) {
          updatePickleLabel(pickleId: $pickleId, label: $label) {
            id label updatedAt
          }
        }
        """
        return parse(
            post_graphql(query, variables={"pickleId": pickle_id, "label": label}, use_auth=True),
            "updatePickleLabel",
            M.ComputePickleUpload,
        )

    # ----------------------------------------------------------------------
    # Stake mutations — guarded with confirm=True
    # ----------------------------------------------------------------------

    @mcp.tool()
    def v2_change_stake(
        tournament_number: int,
        type: str,
        value: str,
        model_id: Optional[str] = None,
        confirm: bool = False,
    ) -> dict[str, Any]:
        """⚠️ Stake change (delta increase OR decrease) for a model. Moves real NMR.

        `type`: "increase" or "decrease". `value`: NMR amount as a string.
        Requires `confirm=True`. The user must have explicitly authorised the
        operation before this tool is called.
        """
        refusal = require_confirm("v2ChangeStake", confirm)
        if refusal:
            return refusal
        query = """
        mutation V2ChangeStake($modelId: ID, $tournamentNumber: Int!, $type: String!, $value: String!) {
          v2ChangeStake(modelId: $modelId, tournamentNumber: $tournamentNumber, type: $type, value: $value) {
            id type status requestedAmount dueDate drain
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={
                    "modelId": model_id, "tournamentNumber": tournament_number,
                    "type": type, "value": value,
                },
                use_auth=True,
            ),
            "v2ChangeStake",
            M.V2ChangeStakeRequest,
        )

    @mcp.tool()
    def increase_stake(model_id: str, amount: str, confirm: bool = False) -> dict[str, Any]:
        """⚠️ Add NMR to an existing stake. Moves real NMR. Requires confirm=True."""
        refusal = require_confirm("increaseStake", confirm)
        if refusal:
            return refusal
        query = """
        mutation IncreaseStake($modelId: ID!, $amount: String!) {
          increaseStake(modelId: $modelId, amount: $amount) {
            id type status requestedAmount dueDate drain
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id, "amount": amount}, use_auth=True),
            "increaseStake",
            M.V2ChangeStakeRequest,
        )

    @mcp.tool()
    def release_stake(
        model_id: str,
        amount: str,
        drain: Optional[bool] = None,
        confirm: bool = False,
    ) -> dict[str, Any]:
        """⚠️ Schedule stake release. Funds become available after the unlock
        period. Requires confirm=True. Pass `drain=True` to release all stake
        regardless of amount."""
        refusal = require_confirm("releaseStake", confirm)
        if refusal:
            return refusal
        query = """
        mutation ReleaseStake($modelId: ID!, $amount: String!, $drain: Boolean) {
          releaseStake(modelId: $modelId, amount: $amount, drain: $drain) {
            id type status requestedAmount dueDate drain
          }
        }
        """
        return parse(
            post_graphql(
                query,
                variables={"modelId": model_id, "amount": amount, "drain": drain},
                use_auth=True,
            ),
            "releaseStake",
            M.V2ChangeStakeRequest,
        )

    @mcp.tool()
    def cancel_pending_stake_release(model_id: str, confirm: bool = False) -> dict[str, Any]:
        """⚠️ Cancel a pending stake-release request. Requires confirm=True."""
        refusal = require_confirm("cancelPendingStakeRelease", confirm)
        if refusal:
            return refusal
        query = """
        mutation CancelPendingStakeRelease($modelId: ID!) {
          cancelPendingStakeRelease(modelId: $modelId) {
            id type status requestedAmount dueDate drain
          }
        }
        """
        return parse(
            post_graphql(query, variables={"modelId": model_id}, use_auth=True),
            "cancelPendingStakeRelease",
            M.V2ChangeStakeRequest,
        )

    @mcp.tool()
    def v3_change_payout_selection(
        model_id: str,
        tournament_number: int,
        take_profit: bool,
        confirm: bool = False,
    ) -> dict[str, Any]:
        """⚠️ Toggle take-profit on / off for a model's V3 payouts.

        Changes how earnings are settled. Requires confirm=True.
        """
        refusal = require_confirm("v3ChangePayoutSelection", confirm)
        if refusal:
            return refusal
        query = """
        mutation V3ChangePayoutSelection($modelId: ID!, $tournamentNumber: Int!, $takeProfit: Boolean!) {
          v3ChangePayoutSelection(modelId: $modelId, tournamentNumber: $tournamentNumber, takeProfit: $takeProfit)
        }
        """
        resp = post_graphql(
            query,
            variables={"modelId": model_id, "tournamentNumber": tournament_number, "takeProfit": take_profit},
            use_auth=True,
        )
        return {"result": extract(resp, "v3ChangePayoutSelection"), "raw": resp}
