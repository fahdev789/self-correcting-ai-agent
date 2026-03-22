def is_resolved(observation):
    logs = observation.get("logs", "").lower()
    last = observation.get("last_result", "").lower()
    return ("error" not in logs) and ("failed" not in logs) and ("ok" in last)
