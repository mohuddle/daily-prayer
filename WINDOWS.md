# Windows 11 house server

Serve Daily Prayer on your LAN. The site is the `web` folder. Grok Build is not required.

Do not port-forward this on your router. Keep it on the private network only.

If you also run the voiced Daily Office and Daily Office Reader, keep those on **8765** and **8766**. This app uses **8767**.

## 1. Put the files on the PC

```powershell
git clone https://github.com/mohuddle/daily-prayer.git C:\DailyPrayer
```

## 2. Install Python

Install [Python 3](https://www.python.org/downloads/windows/). Check **Add python.exe to PATH**.

```powershell
python --version
```

## 3. Try it once

```powershell
cd C:\DailyPrayer
python scripts\serve_lan.py --host 0.0.0.0 --ports 8767
```

On this PC: http://127.0.0.1:8767/

On a phone on the same Wi‑Fi: `http://<this-pc-ipv4>:8767/`

```powershell
ipconfig
```

Stop with Ctrl+C.

## 4. Allow the port on the Private network

1. Windows Defender Firewall → Advanced settings → Inbound Rules → New Rule…
2. Port → TCP → **8767**
3. Allow the connection
4. Check **Private** only
5. Name it `Daily Prayer LAN`

## 5. Start at boot with Task Scheduler

1. Task Scheduler → Create Task…
2. Name: `Daily Prayer LAN`
3. Run whether user is logged on or not
4. Triggers → At startup
5. Actions → New
   - Program/script: `python.exe`
   - Add arguments: `scripts\serve_lan.py --host 0.0.0.0 --ports 8767`
   - Start in: `C:\DailyPrayer`
6. Uncheck **Stop the task if it runs longer than**

If `python.exe` is not found at startup, use the full path from `where.exe python`.

Reboot once and confirm http://127.0.0.1:8767/ loads.

## 6. Update later

```powershell
cd C:\DailyPrayer
git pull
```

Restart the scheduled task (or reboot) so it serves the new files.
