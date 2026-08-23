# Linux house server

Serve Daily Prayer on your LAN. The site is the `web` folder. Grok Build is not required.

Do not port-forward this on your router. Keep it on the private network only.

If you also run the voiced Daily Office and Daily Office Reader, keep those on **8765** and **8766**. This app uses **8767**.

## 1. Put the files on the machine

```bash
git clone https://github.com/mohuddle/daily-prayer.git ~/Work/daily-prayer
```

Use another path if you prefer; keep it stable. The unit file below assumes `~/Work/daily-prayer`.

## 2. Python

You need Python 3. On Arch / Omarchy:

```bash
python3 --version
```

## 3. Try it once

```bash
cd ~/Work/daily-prayer
python3 scripts/serve_lan.py --host 0.0.0.0 --ports 8767
```

On this machine: http://127.0.0.1:8767/

On a phone on the same Wi‑Fi: `http://<this-host-ipv4>:8767/`

```bash
ip -4 addr
```

Stop with Ctrl+C.

## 4. Firewall (only if you use one)

If `firewalld` is running, allow TCP 8767 on the home zone. Many desktop installs have no inbound firewall.

```bash
sudo firewall-cmd --permanent --add-port=8767/tcp
sudo firewall-cmd --reload
```

## 5. Start at login with systemd --user

Copy the unit, edit the path if your clone is not under `~/Work/daily-prayer`, then enable it:

```bash
mkdir -p ~/.config/systemd/user
cp ~/Work/daily-prayer/scripts/daily-prayer.service ~/.config/systemd/user/
# If the repo lives elsewhere, edit WorkingDirectory and ExecStart in that copy.
systemctl --user daemon-reload
systemctl --user enable --now daily-prayer.service
systemctl --user status daily-prayer.service
```

That starts the server when you log in.

To start it at boot even before a graphical login:

```bash
loginctl enable-linger "$USER"
```

Useful commands:

```bash
systemctl --user restart daily-prayer.service
journalctl --user -u daily-prayer.service -f
```

## 6. Optional: desktop autostart

If you would rather not use systemd, copy `scripts/daily-prayer.desktop` to `~/.config/autostart/` and edit the `Path=` and `Exec=` lines.

## 7. Update later

```bash
cd ~/Work/daily-prayer
git pull
systemctl --user restart daily-prayer.service
```
