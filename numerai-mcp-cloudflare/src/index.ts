import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { McpAgent } from "agents/mcp";
import { registerTools } from "./tools";

export class NumeraiMCP extends McpAgent {
	server = new McpServer({
		name: "Numerai GraphQL MCP",
		version: "1.0.0",
	});

	async init() {
		registerTools(this.server, this.env as Env);
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

		return Response.json(
			{
				name: "Numerai GraphQL MCP Server",
				version: "1.0.0",
				mcp_endpoint: "/mcp",
				docs: "https://github.com/lingster/numerai",
			},
			{ status: 200 },
		);
	},
};
