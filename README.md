# SampleMCP

A small, hands-on project for learning the Model Context Protocol (MCP) —
starting from plain calculator scripts and building up to a working MCP
server with tools, resources, and prompts, run over both local (stdio) and
network (streamable-http) transports.

## Contents

| File | Description |
|---|---|
| `calculator.py` | Standalone script: add and subtract two numbers from the command line. |
| `multiplication.py` | Standalone script: multiply two numbers from the command line. |
| `mcp_server.py` | MCP server exposing `add`, `subtract`, `multiply` as tools, a `calc://history` resource, and an `explain_calculation` prompt. Runs over stdio by default. |
| `mcp_server_http.py` | The same server, run over network (`streamable-http`) transport on `http://127.0.0.1:8000/mcp`. |
| `mcp_client.py` | Example MCP client: spawns `mcp_server.py` over stdio, lists and calls its tools/resources/prompts. |
| `mcp_client_http.py` | Example MCP client that connects to `mcp_server_http.py` over HTTP instead of spawning a subprocess. |
| `MCP_Overview.pptx` | Slide deck explaining MCP concepts (client/server, tools/resources/prompts, transports), grounded in this project's code. |
| `requirements.txt` | Python dependencies. |

## Requirements

- Python 3.11+
- The `mcp` Python SDK (version 2.x — see note below)
- [Node.js](https://nodejs.org/) + `npx`, only if you want to use the MCP Inspector

Install dependencies:

```bash
pip install -r requirements.txt
```

> **Note on `mcp` SDK version:** this project uses `mcp==2.2.0`. In this
> major version, `FastMCP` was renamed to `MCPServer`
> (`from mcp.server.mcpserver import MCPServer`). If you're following an
> older MCP tutorial that imports `FastMCP` from `mcp.server.fastmcp`, it
> won't match this install — use `MCPServer` instead, or pin `mcp<2`.

## Running the basic scripts

```bash
python calculator.py
python multiplication.py
```

Each prompts for two numbers and prints the result(s).

## Running the MCP server and client (stdio)

`mcp_client.py` spawns `mcp_server.py` itself, so just run:

```bash
python mcp_client.py
```

This will:
1. List the server's tools, resources, and prompts
2. Call `add`, `subtract`, and `multiply`
3. Read the `calc://history` resource (the log of calculations made)
4. Fetch the `explain_calculation` prompt

## Running the MCP server and client over HTTP

Start the server (it keeps running independently, like a normal web server):

```bash
python mcp_server_http.py
```

In a separate terminal, run the client:

```bash
python mcp_client_http.py
```

## Exploring with the MCP Inspector

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is a
browser-based tool for manually calling a server's tools/resources/prompts.

```bash
npx -y @modelcontextprotocol/inspector python mcp_server.py
```

This opens a local web UI (URL printed in the terminal, including an auth
token) where you can inspect and invoke everything `mcp_server.py` exposes.

> **Windows note:** on machines with corporate security policies
> (AppLocker/EDR), the `mcp` and `uv` console-script `.exe` wrappers may be
> blocked with `Access is denied`. The command above sidesteps that by
> launching the Inspector directly via `npx` and pointing it at `python`
> instead of going through those wrappers.

## MCP concepts covered

- **Tools** — functions the model can call (`add`, `subtract`, `multiply`)
- **Resources** — data a client can read (`calc://history`)
- **Prompts** — reusable message templates a client can fetch
  (`explain_calculation`)
- **Client vs. server** — the client always initiates; the server only
  reacts
- **Transports** — `stdio` (client spawns the server as a subprocess,
  same machine only) vs. `streamable-http` (server runs standalone,
  reachable over the network)

See `MCP_Overview.pptx` for a slide-deck walkthrough of all of the above.
