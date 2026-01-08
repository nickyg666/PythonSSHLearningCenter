#!/bin/bash
# PythonSSHLearningCenter Installation Script
# Installs WiFi hotspot with shellinabox captive portal and Python learning environment

set -e

echo "=========================================="
echo "PythonSSHLearningCenter Installer"
echo "=========================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root (use sudo)"
    exit 1
fi

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Get username (orangepi by default, or first real user)
USER="${USER:-orangepi}"
if [ "$USER" = "root" ]; then
    USER="orangepi"
fi

echo "[1/10] Installing required packages..."
apt update
apt install -y create_ap nginx shellinabox dnsmasq hostapd python3-tk git

echo "[2/10] Configuring shellinabox (HTTP, no SSL)..."
cp "$SCRIPT_DIR/configs/shellinabox/shellinabox" /etc/default/shellinabox
systemctl restart shellinabox
systemctl enable shellinabox

echo "[3/10] Setting up captive portal nginx config..."
mkdir -p /etc/nginx/sites-available
cp "$SCRIPT_DIR/configs/nginx/captive-portal" /etc/nginx/sites-available/
rm -f /etc/nginx/sites-enabled/default
ln -sf /etc/nginx/sites-available/captive-portal /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx

echo "[4/10] Copying shellinabox CSS themes..."
cp -r "$SCRIPT_DIR/configs/shellinabox/options-enabled" /etc/shellinabox/

echo "[5/10] Installing DNS setup script..."
cp "$SCRIPT_DIR/scripts/setup-captive-portal-dns.sh" /usr/local/bin/
chmod +x /usr/local/bin/setup-captive-portal-dns.sh

echo "[6/10] Installing hotspot service..."
cp "$SCRIPT_DIR/configs/systemd/create-ap-hotspot.service" /etc/systemd/system/
systemctl daemon-reload
systemctl enable create-ap-hotspot.service

echo "[7/10] Setting up Python learning examples..."
mkdir -p "/home/$USER/python-fun"
cp -r "$SCRIPT_DIR/python-examples/"* "/home/$USER/python-fun/"
chown -R "$USER:$USER" "/home/$USER/python-fun"

echo "[8/10] Setting up welcome message..."
cp "$SCRIPT_DIR/scripts/welcome-message.sh" "/home/$USER/.welcome"
chown "$USER:$USER" "/home/$USER/.welcome"
echo "/home/$USER/.welcome" >> "/home/$USER/.bashrc" || echo "# Welcome message already in bashrc"

echo "[9/10] Setting up passwordless access for $USER..."
passwd -d "$USER" 2>/dev/null || echo "Note: Could not remove password for $USER"
cat > /etc/sudoers.d/$USER-nopass << EOF
$USER ALL=(ALL) NOPASSWD: ALL
EOF
chmod 0440 /etc/sudoers.d/$USER-nopass

echo "[10/10] Starting hotspot service..."
systemctl start create-ap-hotspot.service
sleep 3

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "📶 WiFi Hotspot:"
echo "   SSID: jailbreakBox"
echo "   Password: (none - open network)"
echo "   Gateway: 192.168.12.1"
echo ""
echo "🖥️  Captive Portal:"
echo "   URL: http://192.168.12.1:4200"
echo "   Auto-redirects from captive portal detection"
echo ""
echo "🐍 Python Learning:"
echo "   Location: ~/python-fun/"
echo "   Start with: cd ~/python-fun && python3 hello.py"
echo ""
echo "🎮 Quick Start:"
echo "   1. Connect to 'jailbreakBox' WiFi"
echo "   2. Open browser (captive portal auto-opens)"
echo "   3. Try: cd ~/python-fun/games && python3 guess_number.py"
echo ""
echo "📚 Learn More:"
echo "   nano ~/python-fun/LEARN.md"
echo ""
echo "✅ Useful Commands:"
echo "   sudo systemctl status create-ap-hotspot.service"
echo "   sudo create_ap --list-clients wlan0"
echo "   sudo journalctl -u create-ap-hotspot.service -f"
echo ""
