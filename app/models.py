from pydantic import BaseModel
from typing import Literal


class Server(BaseModel):
    id: str
    host: str
    port: int
    active_connections: int = 0
    healthy: bool = True


class ServerList(BaseModel):
    servers: list[Server]


class RoutingRule(BaseModel):
    algorithm: Literal["round_robin", "least_connections"] = "round_robin"
