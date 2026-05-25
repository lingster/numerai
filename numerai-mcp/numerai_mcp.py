#!/usr/bin/env python3
"""
Numerai GraphQL MCP server — entry point.

Thin shim that delegates to numerai_mcp_pkg.server. Kept at the package root
so .mcp.json's `python numerai_mcp.py` command continues to work after the
refactor into a proper package.
"""

from numerai_mcp_pkg.server import main

if __name__ == "__main__":
    main()
