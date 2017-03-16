# ProtonVPN_PingServers
Script to test latency of ProtonVPN Servers

Developed in Python 3 for PhotonVPN Beta, though easily adapted to any service with multiple access server ovpn configs.  The Script’s required positional parameter is used to match the “Region” naming convention of the ovpn files, i.e. “us” will match any file with “us” in the filename, thus any server with a “us” region presence.  This will also match the pivot servers (us-is), but I don’t see this as an issue.



Requires: 
Root or sudo access,
pyping library (https://pypi.python.org/pypi/pyping/)
