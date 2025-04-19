# Running Your MCP Server with FastMCP v2.0

This guide walks you through how to run your MCP server using FastMCP v2.0 and install it for use with Claude Desktop.

---

## ✅ Prerequisites
Assumes:
- Your environment is already set up
- Your server code (e.g., `server.py`) is complete and ready to run

---

## 🚀 Running the Server

### 1. Install FastMCP (if not already installed)

It's recommended to use `uv`:
```bash
uv pip install fastmcp
```

If you don’t have `uv`, you can install it via Homebrew (macOS):
```bash
brew install uv
```

Or use pip directly:
```bash
pip install fastmcp
```

### 2. Run Your Server

Using FastMCP’s run command:
```bash
fastmcp run server.py
```

If your script uses the standard entry point:
```python
if __name__ == "__main__":
    mcp.run()
```
Then you can also simply:
```bash
python server.py
```

---

## 🛠️ Installing Server for Claude Desktop

### 1. Install the Server

This command prepares your server for Claude Desktop integration:
```bash
fastmcp install server.py
```

### 2. Restart Claude Desktop

After installing, restart Claude Desktop to load your newly installed server.

---

## 🔧 Additional Tips

### Specify Dependencies
Declare additional packages when instantiating FastMCP:
```python
mcp = FastMCP("My Server", dependencies=["pandas", "numpy"])
```

### Set Environment Variables
Pass env variables during installation:
```bash
fastmcp install server.py -e API_KEY=your_api_key
```

### Use a `.env` File
Load environment configuration from a file:
```bash
fastmcp install server.py -f .env
```

---

## ✅ Example Claude Prompt
If you’ve defined a tool like `add`, you can talk to Claude like this:
> "Please add 5 and 7."

Claude will then use the MCP server to calculate the result.

---

For more info, visit: https://github.com/jlowin/fastmcp

