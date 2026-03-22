from tools import execute_tool
from .planner import plan_step
from .verifier import is_resolved
from .memory import log, get_failures
from tools.get_logs import get_logs


def run_agent(log_path):
    observation = {
        "log_path": log_path,
        "logs": get_logs(log_path),
        "last_result": "start"
    }

    last_actions = []

    for step in range(8):
        plan = plan_step(observation, get_failures())
        action = plan["action"]

        result = execute_tool(action, observation)

        observation["last_result"] = result
        observation["logs"] = get_logs(observation.get("log_path"))

        log({
            "step": step,
            "action": action,
            "reason": plan.get("reason", ""),
            "result": result
        })

        last_actions.append(action)

        if len(last_actions) >= 3 and len(set(last_actions[-3:])) == 1:
            return "failed_loop_detected"

        if is_resolved(observation):
            return "resolved"

    return "failed"
