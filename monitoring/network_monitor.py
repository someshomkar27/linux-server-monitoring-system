import socket

def check_connectivity():
    try:
        socket.create_connection(("google.com", 80), timeout=5)
        return "Connected"
    except:
        return "Disconnected"