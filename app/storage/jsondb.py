import json
from pathlib import Path
from app.models import ServerList, RoutingRule

DB_PATH = Path("db")
SERVERS_FILE = DB_PATH / "servers.json"
RULES_FILE = DB_PATH / "rules.json"


def load_servers() -> ServerList:
    with open(SERVERS_FILE) as f:
        data = json.load(f)
    return ServerList(**data)


def save_servers(server_list: ServerList):
    with open(SERVERS_FILE, "w") as f:
        json.dump(server_list.model_dump(), f, indent=2)


def load_routing_rule() -> RoutingRule:
    with open(RULES_FILE) as f:
        data = json.load(f)
    return RoutingRule(**data)


def save_routing_rule(rule: RoutingRule):
    with open(RULES_FILE, "w") as f:
        json.dump(rule.model_dump(), f, indent=2)
