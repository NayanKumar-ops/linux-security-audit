from utils.colors import GREEN, RED, YELLOW, RESET

def print_result(status, message):
    if status == "PASS":
        print(f"[{GREEN} PASS {RESET}] {message}")
    elif status == "FAIL":
        print(f"[{RED} FAIL {RESET}] {message}")
    elif status == "WARN":
        print(f"[{YELLOW} WARN {RESET}] {message}")
