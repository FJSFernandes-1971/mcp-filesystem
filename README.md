# mcp-filesystem

This repository contains a small MCP-compatible filesystem service. Use the server to expose read-only filesystem access over MCP, following the instructions in `requirements.txt` and `server.py`.

## Troubleshooting Git clone errors

If you see `fatal: unable to access ... 403 CONNECT tunnel failed` when running `git clone`, the network is blocking the HTTPS tunnel before Git can reach GitHub. Try the following to resolve it:

1. **Confirm network access**: `curl -I https://github.com` to check whether HTTPS requests are allowed. If the request is blocked, contact your network administrator or try an allowed network.
2. **Configure the proxy (if required)**: set the proxy environment variables and Git settings before cloning:
   ```bash
   export https_proxy=http://<proxy-host>:<proxy-port>
   export http_proxy=http://<proxy-host>:<proxy-port>
   git config --global http.proxy "$http_proxy"
   git config --global https.proxy "$https_proxy"
   ```
3. **Trust your proxy's TLS certificate**: if the proxy uses a custom certificate, add it to your trust store and point Git to it:
   ```bash
   git config --global http.sslCAInfo /path/to/proxy-ca.pem
   ```
4. **Use an alternate download method**: if tunneling remains blocked, download the repository as a ZIP from GitHub via a browser on a network that allows it, then copy it into this environment.

These steps address the common causes of 403 tunnel failures: missing proxy configuration, blocked outbound HTTPS, or untrusted proxy certificates.
