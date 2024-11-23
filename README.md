
---

# DDoS Layer 4 Attack (Python Script)

This Python script simulates a **Layer 4 DDoS (Denial of Service)** attack by sending UDP packets to a target IP and port. It supports routing traffic through proxy servers, which can be free or premium proxies. 

---

## Features
- Perform a Layer 4 DDoS attack using UDP packets.
- Route traffic through a list of proxy servers.
- Supports multi-threading for high-intensity attacks.

---

## Requirements
- **Proxy List**: You need a proxy list to route traffic. You can use any **free proxy list** or **premium proxies**.
- **Proxy Format**: Each proxy should be listed in the format `IP:PORT`.

---

## Usage

To run the script, execute the following command:

```bash
python layer4.py
```

### Command-Line Options:
- `TARGET_IP`: The IP address of the target to attack.
- `TARGET_PORT`: The port number of the target server.
- `PROXY_FILE`: Path to the file containing the list of proxies (in `IP:PORT` format).
- `NUM_THREADS`: Number of threads to use for sending packets.
- `PACKET_SIZE`: Size of each UDP packet to send (default: `1024` bytes).
- `DELAY`: Time delay between sending each packet (default: `0.1` seconds).

### Example Usage:

```bash
$ python layer4.py
```

When prompted, this is example input the following:

```
Target IP: 102.232.121.44
Target Port: 53
Proxy: proxies.txt
Thread: 1000
Packet Send (default 1024): 2048
Delay Per Second (default 0.1): 0.1
```

### Parameter Explanation:
- **Target IP**: The IP address of the server you wish to attack (e.g., `102.232.121.44`).
- **Target Port**: The port number on the target server (e.g., `53` for DNS).
- **Proxy**: The path to the proxy list file (e.g., `proxies.txt`).
- **Thread**: Number of concurrent threads for sending packets.
- **Packet Size**: Size of each UDP packet in bytes (default is `1024`).
- **Delay Per Second**: Time delay in seconds between each packet (default is `0.1`).

---

## Disclaimer

**Important**: This script is intended for **educational purposes only**. **Do not use this on networks or systems that you do not have explicit permission to test**. Unauthorized use of this tool can lead to legal consequences. Always act responsibly and ethically.

---
