import os
from dotenv import load_dotenv

load_dotenv()

CANVAS_ACCESS_TOKEN=os.getenv("CANVAS_ACCESS_TOKEN")
CANVAS_BASE_URL=os.getenv("CANVAS_BASE_URL")