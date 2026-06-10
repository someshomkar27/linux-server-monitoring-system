from monitoring.cpu_monitor import get_cpu_usage
from monitoring.memory_monitor import get_memory_usage
from monitoring.disk_monitor import get_disk_usage
from monitoring.network_monitor import check_connectivity
from log_analysis.parser import analyze_logs


def main():
    print("\n===== Linux Server Monitoring System =====\n")

    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    print(f"CPU Usage: {cpu}%")

    print(
        f"Memory Usage: {memory['used']} GB / {memory['total']} GB ({memory['percent']}%)"
    )

    print(
        f"Disk Usage: {disk['used']} GB / {disk['total']} GB ({disk['percent']}%)"
    )

    print(f"Network Status: {check_connectivity()}")

    # Alerts
    if cpu > 80:
        print("ALERT: High CPU Usage")

    if memory["percent"] > 80:
        print("ALERT: High Memory Usage")

    if disk["percent"] > 90:
        print("ALERT: Disk Usage Critical")

    # Log Analysis
    errors = analyze_logs()

    for error in errors:
        print(f"LOG ALERT: {error}")

    print("\n==========================================")


if __name__ == "__main__":
    main()