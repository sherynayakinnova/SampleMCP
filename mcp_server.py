import json

from mcp.server.mcpserver import MCPServer

server = MCPServer(name="calculator")

history: list[dict] = []


def _record(operation: str, a: float, b: float, result: float) -> None:
    history.append({"operation": operation, "a": a, "b": b, "result": result})


@server.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    result = a + b
    _record("add", a, b, result)
    return result


@server.tool()
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    result = a - b
    _record("subtract", a, b, result)
    return result


@server.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    result = a * b
    _record("multiply", a, b, result)
    return result


@server.resource("calc://history")
def get_history() -> str:
    """The list of calculations performed so far, as JSON."""
    return json.dumps(history, indent=2)


@server.prompt()
def explain_calculation(operation: str, a: float, b: float, result: float) -> str:
    """Ask the model to explain a calculation in plain English."""
    return (
        f"Explain, in one or two plain-English sentences suitable for a beginner, "
        f"why {operation}({a}, {b}) equals {result}."
    )


if __name__ == "__main__":
    server.run()
