# manage.py
import sys
import code
import asyncio
from app.main import app  # your FastAPI app
from models.users import User
import IPython

def shell():
    context = {
        "app": app,
        "User": User,
    }
    print("Launching IPython shell...")
    IPython.start_ipython(argv=[], user_ns=context)
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "shell":
        shell()
    else:
        print("Usage: python manage.py shell")
