from monitoring.cpu_monitor import get_cpu_usage
from monitoring.memory_monitor import get_memory_usage
from monitoring.disk_monitor import get_disk_usage
from monitoring.network_monitor import check_connectivity


def main():
    print("\n===== Linux Server Monitoring System =====\n")

    print(f"CPU Usage: {get_cpu_usage()}%")

    memory = get_memory_usage()
    print(
        f"Memory Usage: {memory['used']} GB / {memory['total']} GB ({memory['percent']}%)"
    )

    disk = get_disk_usage()
    print(
        f"Disk Usage: {disk['used']} GB / {disk['total']} GB ({disk['percent']}%)"
    )

    print(f"Network Status: {check_connectivity()}")

    print("\n==========================================")


if __name__ == "__main__":
    main()