import socket

def get_external_ip():
    try:
        # Connect to an external server to determine the public IP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Google's public DNS server
            return f"External IP Address: {s.getsockname()[0]}"
    except Exception as e:
        return f"Error: {e}"

print(get_external_ip())
