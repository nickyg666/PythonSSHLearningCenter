# 📅 System Configuration Update - January 8, 2026

## 👥 User Account Setup

### Overview
Two user accounts are configured on the Orange Pi Zero 2 system to facilitate both normal operations and administrative tasks.

### orangepi User (Default System User)
- **Username:** `orangepi`
- **Password:** `orangepi`
- **UID:** 1000
- **Shell:** `/bin/bash`
- **Purpose:** Default user for normal operations, running scripts, and daily use
- **Groups:** orangepi tty disk dialout sudo audio video plugdev games users systemd-journal input netdev docker pulse-access
- **Sudo Access:** Yes (requires password)
- **Use Case:** Safe for everyday use, requires password for elevated privileges

### lorenzo User (Administrative User)
- **Username:** `lorenzo`
- **Password:** None (passwordless login)
- **UID:** 1001
- **Shell:** `/bin/bash`
- **Purpose:** System administration tasks requiring full sudo access
- **Groups:** lorenzo(1001), sudo(27)
- **Sudo Access:** `ALL : ALL NOPASSWD: ALL`
- **Use Case:** Quick administrative operations without repeated password prompts

## 🔐 Security Considerations

### Why Two Users?
1. **Safety:** `orangepi` user requires password for sudo, preventing accidental system changes
2. **Convenience:** `lorenzo` user has passwordless sudo for efficient administration
3. **Separation:** Distinct users for different privilege levels (principle of least privilege)

### When to Use Each User

**Use `orangepi` for:**
- Daily operations and learning
- Running Python scripts and games
- SSH access from external networks
- Experimentation where sudo password protection is desired
- Safe environment where accidental system damage is less likely

**Use `lorenzo` for:**
- System administration and configuration
- Package installation (`sudo apt install`)
- System service management
- Quick sudo operations during development
- Tasks requiring repeated elevated privileges

### Security Notes
⚠️ **Important:** The `lorenzo` user has full passwordless sudo access. Use this account only in trusted environments and for administrative purposes only.

## 🚀 Usage Examples

### Switching Between Users

```bash
# Switch to lorenzo user (passwordless)
su - lorenzo

# Switch back to orangepi user
exit

# Run a single command as lorenzo
sudo -u lorenzo [command]

# Run command with lorenzo's sudo privileges
sudo -u lorenzo sudo [command]
```

### SSH Access

```bash
# SSH as orangepi (requires password)
ssh orangepi@<orange-pi-ip>

# SSH as lorenzo (passwordless - use carefully!)
ssh lorenzo@<orange-pi-ip>
```

### Common Tasks

```bash
# As orangepi - Safe everyday use
orangepi@orangepizero2:~$ cd ~/python-fun/games
orangepi@orangepizero2:~$ python3 guess_number.py

# As lorenzo - Administrative tasks
lorenzo@orangepizero2:~$ sudo apt update
lorenzo@orangepizero2:~$ sudo systemctl restart create-ap-hotspot.service

# Quick switch for one admin command
orangepi@orangepizero2:~$ sudo -u lorenzo sudo systemctl status shellinabox
```

## 🔧 User Management Commands

### Check User Status
```bash
# Check orangepi user
passwd -S orangepi
# Output: orangepi P 2026-01-08 0 99999 7 -1 (P = password set)

# Check lorenzo user
passwd -S lorenzo
# Output: lorenzo NP 2026-01-08 0 99999 7 -1 (NP = no password)

# Check lorenzo's sudo permissions
sudo -l -U lorenzo
# Output: User lorenzo may run the following commands:
#         (ALL : ALL) NOPASSWD: ALL
```

### Modify Users (If Needed)
```bash
# Set/Change orangepi password
sudo passwd orangepi

# Set password for lorenzo (adds security)
sudo passwd lorenzo

# Remove lorenzo password (back to passwordless)
sudo passwd -d lorenzo

# Remove lorenzo user entirely
sudo userdel -r lorenzo
```

## 📚 Integration with PythonSSHLearningCenter

### Browser Terminal Access
When using the browser terminal (Shellinabox), you'll be logged in as the `orangepi` user by default. This is the safer default for learning and experimentation.

### Python Scripts
All Python scripts and games in `~/python-fun/` are designed to run under the `orangepi` user account. No special permissions are required.

### WiFi Hotspot
The WiFi hotspot ("jailbreakBox") allows connections from any device. When accessed via browser terminal, users connect as `orangepi` for safety.

## 🎯 Best Practices

### For Learners/Students
1. Always use `orangepi` account for learning
2. Only switch to `lorenzo` when instructed by teacher/documentation
3. Be cautious with sudo commands
4. Ask before running commands you don't understand

### For Administrators
1. Use `lorenzo` only when necessary
2. Consider changing lorenzo's password if security is a concern
3. Monitor sudo usage in system logs (`journalctl`)
4. Keep orangepi's password secure

### For Development
1. Develop and test as `orangepi` (safer)
2. Switch to `lorenzo` for system-level configuration
3. Document any changes that require elevated privileges
4. Consider creating additional users with specific permissions for different roles

## 🔄 Troubleshooting

### Can't Login as orangepi
```bash
# If orangepi password was forgotten, reset as lorenzo
sudo -u lorenzo sudo passwd orangepi
```

### lorenzo Sudo Not Working
```bash
# Check if lorenzo is in sudo group
groups lorenzo

# Verify sudoers file (as root)
sudo cat /etc/sudoers.d/lorenzo
# Should contain: lorenzo ALL=(ALL:ALL) NOPASSWD: ALL
```

### Permission Denied on Files
```bash
# Check file ownership
ls -la /path/to/file

# Fix ownership if needed
sudo chown orangepi:orangepi /path/to/file

# Or access as lorenzo
sudo -u lorenzo [command]
```

## 📊 User Comparison Table

| Feature | orangepi | lorenzo |
|---------|----------|---------|
| Password | Required | None |
| Sudo | Yes (with password) | Yes (NOPASSWD) |
| UID | 1000 | 1001 |
| Default Use | Yes | No |
| Safety Level | High | Medium |
| Best For | Learning, Daily Use | Admin, Development |

## ✅ Verification Checklist

- [x] orangepi user exists with password `orangepi`
- [x] lorenzo user exists with no password
- [x] lorenzo has full sudo access (NOPASSWD: ALL)
- [x] orangepi has sudo access (requires password)
- [x] Both users have shell `/bin/bash`
- [x] Both users in sudo group
- [x] SSH access works for both users
- [x] Browser terminal defaults to orangepi user

---

**Date:** January 8, 2026
**Configured by:** opencode
**Status:** ✅ Active and Verified
