def get_logs(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"ERROR_READING_LOGS: {e}"
