# WinAutoRunner

A portfolio-grade **prototype** for scheduled Python + Playwright + Chrome tasks on Windows.
Inspired by a publicly described deployment use case, **not** client-delivered software.
No real customer data, account credentials, or scraping of restricted services.

## Scope

- Standalone demonstration against https://example.com (page title and URL).
- Scheduled interval loop; JSON status and text logs in an ignored `logs/` directory.
- Optional Chrome CDP attachment via explicit `cdp_url` in local config.
- Windows PowerShell scripts for installation, a single test, loop, status and
  interactive-user startup shortcut.
- Unit tests for configuration validation.

## Quick start (Windows, Python 3.12)

1. Install Python 3.12 and Google Chrome.
2. From PowerShell in this repository run `powershell -ExecutionPolicy Bypass -File scripts/install.ps1`.
3. Run `powershell -ExecutionPolicy Bypass -File scripts/run-once.ps1`.
4. Confirm `logs/status.json` has `"ok": true`.
5. For periodic checks run `powershell -ExecutionPolicy Bypass -File scripts/run-loop.ps1`.
6. Optionally run `scripts/setup-startup.ps1` for an **already logged-in** user.

To change settings, copy `config/config.example.json` to `config/config.local.json`
and use `--config config/config.local.json` with the Python entrypoint.
The default URL is a safe public test page.

## Caveats

- This project **does not** implement automatic Windows login.
- User Startup folder scripts are not equivalent to system-level boot services.
- Chrome in a remote interactive session may freeze when RDP disconnects.
- `tscon`, reboot, Windows Server, and 24/7 continuity require separate empirical tests.
- Do not bind CDP to a public interface or use your main Chrome profile.
- Customer-provided script/README needed for a production implementation.
- See [RDP notes](docs/windows-rdp.md) and [test record](docs/test-results.md).

## Tests

```powershell
python -m unittest discover -s tests -v
```

## License

MIT (see LICENSE).
