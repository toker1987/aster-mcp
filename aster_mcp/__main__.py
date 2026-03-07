import os
from aster_mcp.simple_server import SimpleAsterMCPServer

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9002))
    server = SimpleAsterMCPServer(port=port, host="0.0.0.0")
    server.run(transport="sse")
```

4. **Ctrl+S** → commit → push
5. Wait for Railway to redeploy
6. Then visit:
```
https://aster-mcp-production.up.railway.app/sse
