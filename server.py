# FastMCP V2.0, instead of FastMCP V1.0 built-in to official MCP devkit
from fastmcp import FastMCP
from fastmcp.utilities.types import Image
from PIL import Image as PILImage
from pydantic import BaseModel
import io

mcp = FastMCP("Demo", dependencies=["pillow"])

# Basic tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Using tools with a model
class UserInfo(BaseModel):
    user_id: int
    notify: bool = False

@mcp.tool()
async def send_notification(user: UserInfo, message: str) -> dict:
    """Sends a notification to a user if requested."""
    if user.notify:
        # Simulate sending notification
        print(f"Notifying user {user.user_id}: {message}")
        return {"status": "sent", "user_id": user.user_id}
    return {"status": "skipped", "user_id": user.user_id}

# Basic resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Image example
# Note: As for now (2025/04/22) FastMCP V2 does not support using fastmcp.utilities.types.Image for input type hinting.
@mcp.tool()
def load_google_image() -> Image:
    """Loads the google.png image from the disk."""
    return Image(path="E:/Documents/Programming Projects/My-FastMCP-Example/google.png")  # Load the specific image

if __name__ == "__main__":
    mcp.run()