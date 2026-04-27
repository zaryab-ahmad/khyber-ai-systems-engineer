# math_engine.py

def heavy_calculation(task_id):
    """This function now lives in a physical file, 
    so Windows can 'find' it when starting new processes."""
    print(f"Chef {task_id}: Starting heavy math...")
    # 10 Million operations
    result = sum(i * i for i in range(10**7))
    return f"Chef {task_id}: Done with result {result}"