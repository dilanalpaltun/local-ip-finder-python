# Local IP Finder (Python)

A tiny Python script that prints the local IP address of the machine it runs on.

## How it works
It uses:
- `socket.gethostname()`
- `socket.gethostbyname()`

## Run
```bash
python src/ip_finder.py
Output example
Local IP: 192.168.1.10
