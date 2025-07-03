import httpx
from fastapi import APIRouter, Request, HTTPException
from app.balancer import manager, health
from app.storage import jsondb
from app.models import ServerList, RoutingRule

router = APIRouter()


@router.get("/route")
async def route_request(request: Request):
    health.perform_health_check()
    server = manager.get_next_server()
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://{server.host}:{server.port}/")
        return {
            "target": f"http://{server.host}:{server.port}",
            "response": response.text,
        }
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Backend request failed")


@router.get("/servers", response_model=ServerList)
def get_servers():
    return jsondb.load_servers()


@router.post("/servers")
def update_servers(servers: ServerList):
    jsondb.save_servers(servers)
    return {"status": "updated"}


@router.get("/rule", response_model=RoutingRule)
def get_rule():
    return jsondb.load_routing_rule()


@router.post("/rule")
def update_rule(rule: RoutingRule):
    jsondb.save_routing_rule(rule)
    return {"status": "updated"}


@router.post("/healthcheck")
def healthcheck():
    health.perform_health_check()
    return {"status": "completed"}
