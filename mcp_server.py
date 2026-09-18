from mcp.server.mcpserver import MCPServer

server = MCPServer(name="calculator")


@server.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@server.tool()
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


@server.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


if __name__ == "__main__":
    server.run()
