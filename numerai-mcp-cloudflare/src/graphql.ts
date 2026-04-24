const API_URL = "https://api-tournament.numer.ai/";

interface GQLResponse<T> {
	data?: T;
	errors?: Array<{ message: string; locations?: unknown[]; path?: unknown[] }>;
}

export async function gql<T = unknown>(
	query: string,
	variables?: Record<string, unknown>,
	authToken?: string,
): Promise<T> {
	const headers: Record<string, string> = { "Content-Type": "application/json" };
	if (authToken) headers["Authorization"] = `Token ${authToken}`;

	const resp = await fetch(API_URL, {
		method: "POST",
		headers,
		body: JSON.stringify({ query, variables }),
	});

	if (!resp.ok) {
		throw new Error(`HTTP ${resp.status} from Numerai API: ${await resp.text()}`);
	}

	const result = (await resp.json()) as GQLResponse<T>;
	if (result.errors?.length) {
		throw new Error(result.errors.map((e) => e.message).join("; "));
	}
	if (result.data === undefined) {
		throw new Error("No data returned from API");
	}
	return result.data;
}

type ToolContent = { content: Array<{ type: "text"; text: string }>; isError?: boolean };

export async function toolResult(fn: () => Promise<unknown>): Promise<ToolContent> {
	try {
		const data = await fn();
		return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
	} catch (err) {
		const msg = err instanceof Error ? err.message : String(err);
		return { isError: true, content: [{ type: "text", text: `Error: ${msg}` }] };
	}
}
