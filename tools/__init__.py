from .get_logs import get_logs
from .restart_service import restart_service
from .install_dependencies import install_dependency
from .fix_env import fix_env
from .fix_config import fix_config

TOOLS = {
    "get_logs": get_logs,
    "restart_service": restart_service,
    "install_dependency": install_dependency,
    "fix_env": fix_env,
    "fix_config": fix_config,
}


def execute_tool(action, context):
    if action not in TOOLS:
        return f"TOOL_NOT_FOUND: {action}"

    if action == "get_logs":
        return TOOLS[action](context.get("log_path", "logs.txt"))

    if action == "install_dependency":
        return TOOLS[action](context.get("package", ""))

    if action == "fix_config":
        return TOOLS[action](context)

    return TOOLS[action]()
