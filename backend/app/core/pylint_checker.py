import subprocess

def run_pylint(code: str) -> str:
    """Run pylint on the given code and return the output."""
    with open("temp_script.py", "w") as f:
        f.write(code)

    result = subprocess.run(["pylint", "temp_script.py", "--disable=all", "--enable=E,F,W"], capture_output=True, text=True)
    return result.stdout