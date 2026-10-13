# Test record — 2026-10-13

| Test | Status | Evidence / scope |
| --- | --- | --- |
| Config unit tests | PASS | 3/3 on Windows, system Python 3.10.11 |
| Playwright + Chrome launch | PASS | Python 3.13 virtualenv, Playwright 1.63.0; headless Chrome |
| Visit example.com and record title | PASS | `logs/status.json`: `title=Example Domain`, `ok=true` |
| Python 3.12 compatibility | Not tested | Python 3.12 is not installed |
| Scheduled long-running loop | Not tested | Requires elapsed-time observation |
| Crash/restart wrapper | Not tested | Requires deliberate process kill |
| Interactive startup shortcut | Not tested | Requires interactive login |
| Reboot and auto-login | Not implemented | Deliberately not enabling insecure auto-login |
| RDP disconnect / Chrome GUI continuity | Not tested | Requires a remote interactive Windows machine |
| One-hour unattended operation | Not tested | Needs log evidence |
| US Windows VPS | Not tested | No VPS bought; no recurring cost |

Important: a headless Chrome smoke test is NOT evidence of graphical RDP session continuity.
