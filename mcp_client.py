import asyncio
import sys

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def main():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"],
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            print()
            result = await session.call_tool("add", {"a": 10, "b": 5})
            print("add(10, 5) ->", result.structured_content)

            result = await session.call_tool("subtract", {"a": 10, "b": 5})
            print("subtract(10, 5) ->", result.structured_content)

            result = await session.call_tool("multiply", {"a": 10, "b": 5})
            print("multiply(10, 5) ->", result.structured_content)

            print()
            resources = await session.list_resources()
            print("Available resources:")
            for resource in resources.resources:
                print(f"  - {resource.uri}: {resource.description}")

            history = await session.read_resource("calc://history")
            print("\ncalc://history contents:")
            print(history.contents[0].text)

            print()
            prompts = await session.list_prompts()
            print("Available prompts:")
            for prompt in prompts.prompts:
                print(f"  - {prompt.name}: {prompt.description}")

            prompt_result = await session.get_prompt(
                "explain_calculation",
                {"operation": "add", "a": "10", "b": "5", "result": "15"},
            )
            print("\nexplain_calculation prompt messages:")
            for message in prompt_result.messages:
                print(f"  [{message.role}] {message.content.text}")


if __name__ == "__main__":
    asyncio.run(main())
