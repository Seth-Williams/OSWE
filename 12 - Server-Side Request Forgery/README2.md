## Subnet Scanning with SSRF

Rather than scanning an entire subnet, we can try scanning for network gateways.2 Network designs commonly use a /16 or /24 subnet mask with the gateway running on the IP where the forth octet is ".1" (for example: 192.168.1.1/24 or 172.16.0.1/16).

We can check for valid hosts but closed ports with the following: 
```bash
curl -X POST -H "Content-Type: application/json" -d '{"url":"http://127.0.0.1:6666"}' http://apigateway:8000/files/import -s -w 'Total: %{time_total} microseconds\n' -o /dev/null
```

The request to a closed port is taking me about .25 - .31 seconds. 

When changing the host to a non reachable one, it takes much longer. 

Check ssrf_gaway_scanner.py to see the finished script. 