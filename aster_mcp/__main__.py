from aster_mcp.simple_server import SimpleAsterMCPServer

if __name__ == "__main__":
    server = SimpleAsterMCPServer()
    server.run(transport="sse")
