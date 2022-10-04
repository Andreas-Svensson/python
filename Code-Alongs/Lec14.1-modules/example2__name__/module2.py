import numpy as np

def trigonometric_identity(angle: float) -> float:
    """Calculates trig identity
    
    param:
    angle: angle in radians

    return trigonometric one
    """
    print("Running trigonometric_identity()")
    return np.cos(angle)**2 + np.sin(angle)**2

if __name__ == "__main__": # if code is run from this namespace:
    run_message = "Running directly from module2.py"
    print("\n"+ "="*(42 + len(run_message)))
    print(f"="*20, run_message, "="*20)
    print("="*(42 + len(run_message)) + "\n")

    print(trigonometric_identity(42))
else:
    run_message = "Imported module \"module2\""
    print("\n"+ "="*(42 + len(run_message)))
    print(f"="*20, run_message, "="*20)
    print("="*(42 + len(run_message)) + "\n")