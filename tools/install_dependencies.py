def install_dependency(pkg: str = ""):
    pkg = pkg or "missing-package"
    return f"SIMULATED: pip install {pkg} -> OK"
