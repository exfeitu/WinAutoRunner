# WinAutoRunner

Windows Chrome + Playwright 定时自动化演示项目，供工程能力验证与作品集展示。

不含客户代码、账号、业务数据。演示使用 https://example.com。
支持定时打开页面、写入状态 JSON 和日志、PowerShell 启动与检查脚本。

运行环境目标为 Windows + Python 3.12 + Google Chrome。
先运行 `scripts/install.ps1`，再运行 `scripts/run-once.ps1`。
测试记录见 `docs/test-results.md`。

**未承诺 24/7 稳定性**：自动登录、Windows Server、RDP 断线保活、
Windows 更新与真实 VPS 部署尚未验证。请勿在公网开放 Chrome 远程调试端口。
