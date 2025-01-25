# Model Context Protocol Server for Solana Client

Installation of server:

```sh
git clone git@github.com:tywenk/mcp-sol.git
cd mcp-sol
uv sync
mcp install src/server.py
```

Ensure the Claude desktop JSON config at `/Users/{user}/Library/Application Support/Claude` (on a Mac) looks something like this. Note that the `uv` binary and paths are all absolute.

```json
{
  "globalShortcut": "Alt+Space",
  "mcpServers": {
    "Solana Client": {
      "command": "/Users/tywen/.local/bin/uv",
      "args": [
        "--directory",
        "/Users/tywen/Developer/mcp-sol",
        "run",
        "--with",
        "mcp",
        "mcp",
        "run",
        "/Users/tywen/Developer/mcp-sol/src/server.py"
      ]
    }
  }
}
```
