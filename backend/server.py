import argparse
import signal
import sys

import uvicorn

def handle_shutdown(signum, frame):
    print("Shutting down...")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the RAG Chat server")
    parser.add_argument("--host", type=str, default="localhost", help="host to bind the server (default: localhost)")
    parser.add_argument("--port", type=int, default=8000, help="port to bind the server (default: 8000)")
    parser.add_argument("--reload", action="store_true", help="enable auto-reload")
    parser.add_argument("--log-level", type=str, default="info", choices=["critical", "error", "warning", "info", "debug"], help="log level (default: info)")

    args = parser.parse_args()

    reload = False
    if args.reload:
        reload = True

    try:
        uvicorn.run("src.main:app", host=args.host, port=args.port, reload=reload, log_level=args.log_level)
    except Exception as e:
        print(e)
        sys.exit(1)