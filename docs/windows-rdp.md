# Windows RDP and unattended operation

The prototype is NOT a production 24/7 guarantee.

Graphical Chrome automation requires a usable interactive Windows desktop session.
A startup shortcut only runs when that user actually signs in. Reboot without auto-logon
will **not** start a graphical app automatically. Password-based auto-logon stores
sensitive credentials locally; do not enable it casually on internet-facing servers.

`tscon` may transfer an RDP session to the console but is not portable across every
hosting environment. Test with a real authorized server, the actual user session,
RDP disconnect, Chrome page rendering, and a full reboot. Avoid publishing RDP
credentials or exposing Chrome's CDP port to the internet.

Security: customer owns the VPS and pays the provider directly; dedicated
least-privilege account, strong MFA on the provider, firewall/RDP allowlists,
encrypted backups, and no secrets in Git or logs. Never disable security updates;
configure active hours and supervised maintenance windows instead.
