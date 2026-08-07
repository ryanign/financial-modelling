"""
Session 00 — Environment Verification
Run with: python session_00_setup/verify.py
(activate fm-py312 environment first)
"""

import sys

REQUIRED = {
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "scipy": "scipy",
    "yfinance": "yfinance",
}

def check_python():
    major, minor = sys.version_info[:2]
    version_str = f"{major}.{minor}.{sys.version_info[2]}"
    ok = major == 3 and minor >= 12
    status = "✓" if ok else "✗  (need 3.12+)"
    print(f"{'Python':<14}: {version_str:<10} {status}")
    return ok

def check_package(import_name, display_name):
    try:
        mod = __import__(import_name)
        version = getattr(mod, "__version__", "unknown")
        print(f"{display_name:<14}: {version:<10} ✓")
        return True
    except ImportError:
        print(f"{display_name:<14}: {'NOT FOUND':<10} ✗")
        return False

def main():
    print("\n--- Environment Check ---\n")
    results = []
    results.append(check_python())
    for import_name, display_name in REQUIRED.items():
        results.append(check_package(import_name, display_name))

    print()
    if all(results):
        print("Environment ready. Proceed to Session 01.")
    else:
        print("Issues found. Run `pip install -r requirements.txt` and try again.")
        print("If problems persist, check notes.md section 6.")
    print()

if __name__ == "__main__":
    main()
