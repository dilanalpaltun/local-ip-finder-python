import socket


def get_local_ip() -> str | None:
    """
    Returns the local IP address of the machine running this script.
    """
    try:
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        return local_ip
    except Exception as err:
        print("Could not detect local IP address:", err)
        return None


if __name__ == "__main__":
    ip = get_local_ip()
    if ip:
        print(f"Local IP: {ip}")
    else:
        print("Local IP could not be detected.")
