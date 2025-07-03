from app.storage import jsondb
from app.models import Server
from itertools import cycle

_rr_cycle = None
_rr_ids = []


def get_next_server() -> Server:
    global _rr_cycle, _rr_ids

    servers = [s for s in jsondb.load_servers().servers if s.healthy]
    rule = jsondb.load_routing_rule()

    if not servers:
        raise Exception("No healthy servers available.")

    if rule.algorithm == "least_connections":
        return min(servers, key=lambda s: s.active_connections)
    
    elif rule.algorithm == "round_robin":
        server_ids = [s.id for s in servers]
        if _rr_cycle is None or server_ids != _rr_ids:
            _rr_cycle = cycle(servers)
            _rr_ids = server_ids

        return next(_rr_cycle)
