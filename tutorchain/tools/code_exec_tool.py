# tutorchain/tools/code_exec_tool.py
"""
Code Execution Tool:
Yeh tool safe environment me student ka Python code run karta hai.
NOTE: exec() powerful hota hai, isliye hum safe builtins use kar rahe hain.
"""

import traceback


def execute_python_code(code: str) -> dict:
    """
    Executes provided Python code safely.
    
    Returns:
    {
        'stdout': any printed variables/output,
        'error': error_message (optional),
        'traceback': full_traceback (optional)
    }
    """

    try:
        local_vars = {}

        # Safe exec - empty builtins to stop dangerous operations
        safe_globals = {"__builtins__": {}}

        exec(code, safe_globals, local_vars)

        return {
            "stdout": local_vars
        }

    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }
