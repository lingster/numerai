import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { McpAgent } from "agents/mcp";
import { registerTools } from "./tools";

export class NumeraiMCP extends McpAgent {
	server = new McpServer({
		name: "Numerai GraphQL MCP",
		version: "1.0.0",
	});

	async init() {
		const env = this.env as Env;
		// DurableObjectState storage — isolated per session (per DO instance).
		// Credentials written here are never shared across different client sessions.
		const storage = (this.ctx as DurableObjectState).storage;

		registerTools(this.server, {
			async getToken() {
				const publicId =
					(await storage.get<string>("auth_public_id")) ?? env.NUMERAI_PUBLIC_ID;
				const secretKey =
					(await storage.get<string>("auth_secret_key")) ?? env.NUMERAI_SECRET_KEY;
				return publicId && secretKey ? `${publicId}$${secretKey}` : undefined;
			},
			async setCredentials(publicId: string, secretKey: string) {
				await storage.put("auth_public_id", publicId);
				await storage.put("auth_secret_key", secretKey);
			},
			async clearCredentials() {
				await storage.delete("auth_public_id");
				await storage.delete("auth_secret_key");
			},
			async getStoredPublicId() {
				return storage.get<string>("auth_public_id");
			},
			hasEnvFallback: !!(env.NUMERAI_PUBLIC_ID && env.NUMERAI_SECRET_KEY),
		});
	}
}

export default {
	fetch(request: Request, env: Env, ctx: ExecutionContext) {
		const url = new URL(request.url);

		if (url.pathname === "/mcp") {
			return NumeraiMCP.serve("/mcp").fetch(request, env, ctx);
		}

		if (url.pathname === "/health") {
			return Response.json({ status: "ok", name: "Numerai GraphQL MCP", version: "1.0.0" });
		}

		return Response.json({
			name: "Numerai GraphQL MCP Server",
			version: "1.0.0",
			mcp_endpoint: "/mcp",
			docs: "https://github.com/lingster/numerai",
		});
	},
};
