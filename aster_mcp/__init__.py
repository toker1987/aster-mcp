import asyncio
from aster_mcp.server import serve

if __name__ == "__main__":
    asyncio.run(serve())
```

**Commit changes.**

---

## If That Fails Too — Check `__init__.py` Fully

Click on `aster_mcp/__init__.py` and share **everything** you see inside it — the full contents, not just the top part.

Also tell me **every file** you see inside the `aster_mcp/` folder like:
```
__init__.py
__main__.py
server.py       ← exists?
tools.py        ← exists?
client.py       ← exists?
config.py       ← exists?
