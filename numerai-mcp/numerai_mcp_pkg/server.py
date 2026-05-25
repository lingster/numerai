"""FastMCP server entry point. Registers every query + mutation tool."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from . import tools_queries, tools_mutations

mcp = FastMCP("numerai-graphql")

tools_queries.register(mcp)
tools_mutations.register(mcp)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
