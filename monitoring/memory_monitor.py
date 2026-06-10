import psutil

def get_memory_usage():
    memory = psutil.virtual_memory()

    return {
        "total": round(memory.total / (1024 ** 3), 2),
        "used": round(memory.used / (1024 ** 3), 2),
        "percent": memory.percent
    }

if __name__ == "__main__":
    print(get_memory_usage())