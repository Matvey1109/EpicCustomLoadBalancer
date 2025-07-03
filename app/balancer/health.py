import httpx
from app.storage import jsondb


def perform_health_check():
    server_list = jsondb.load_servers()

    for server in server_list.servers:
        url = f"http://{server.host}:{server.port}/health"
        try:
            response = httpx.get(url, timeout=1.0)
            server.healthy = response.status_code == 200
        except httpx.RequestError:
            server.healthy = False

    jsondb.save_servers(server_list)
