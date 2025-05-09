import argparse
import uvicorn
from condAPI.endpoints import root_router

def start_service(port):
    print(f"Starting the service on port {port}...")
    uvicorn.run(
        "condAPI.__main__:root_router",
        host="0.0.0.0",
        port=port,
        reload=True
    )


def main():
    """ 
        Main entry point for the application.
    """
    parser = argparse.ArgumentParser(description="Management of the condAPI service.")
    subparsers = parser.add_subparsers(dest="command", description="Management of the condAPI service.")

    # Subcomando para iniciar el servicio
    start_parser = subparsers.add_parser("start", help="Starts the service")
    start_parser.add_argument(
        "--port", type=int, default=8000, help="Port to run the service on (default: 8000)"
    )

    args = parser.parse_args()

    if args.command == "start":
        start_service(args.port)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()