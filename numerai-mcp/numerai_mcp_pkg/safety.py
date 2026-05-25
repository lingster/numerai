"""Safety helpers for mutations with real-money side effects."""

from __future__ import annotations

from typing import Any


class ConfirmationRequired(Exception):
    pass


def require_confirm(action: str, confirm: bool) -> dict[str, Any] | None:
    """Return a refusal envelope when `confirm` is not explicitly True.

    Use at the top of any mutation tool that moves NMR, releases stake, or
    otherwise has irreversible consequences. The wrapper still requires the
    caller to set confirm=True even if the tool is reachable from a privileged
    context — Claude won't accidentally pass it without the user explicitly
    asking.
    """
    if confirm is True:
        return None
    return {
        "refused": True,
        "action": action,
        "reason": (
            "This mutation has irreversible or financial consequences. "
            "Re-call the tool with confirm=True to proceed. Make sure the user "
            "has explicitly authorised this action."
        ),
    }
