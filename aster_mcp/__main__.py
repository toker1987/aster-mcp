import os
from aster_mcp.simple_server import SimpleAsterMCPServer

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9002))
    server = SimpleAsterMCPServer(port=port, host="0.0.0.0")
    server.run(transport="sse")
