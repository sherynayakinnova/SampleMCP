from mcp_server import server

if __name__ == "__main__":
    server.run(transport="streamable-http", host="127.0.0.1", port=8000)
