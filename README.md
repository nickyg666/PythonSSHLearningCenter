# PythonSSHLearningCenter

A complete WiFi hotspot with shellinabox captive portal and beginner Python learning environment for kids.

## 🎯 What This Project Does

- **WiFi Hotspot**: Creates an open WiFi network (jailbreakBox)
- **Captive Portal**: Redirects all HTTP traffic to web-based terminal
- **Shellinabox**: Browser-based SSH terminal for easy access
- **Python Learning**: Kid-friendly coding examples and games
- **Auto-Detection**: Works with iOS, Android, and Windows captive portal detection

## 🌟 Features

### Hotspot & Captive Portal
- Open WiFi network (no password required)
- Automatic internet sharing from ethernet
- Captive portal redirects to shellinabox terminal
- Platform detection for iOS/Android/Windows
- Auto-start on boot

### Shellinabox Terminal
- Browser-based SSH access
- Passwordless login for kids
- Welcome message with Python quick-start guide
- Custom terminal themes

### Python Learning Environment
- Interactive games (guess the number, text adventures)
- Turtle graphics for visual programming
- Well-commented examples
- Easy-to-follow instructions
- Encourages experimentation

## 📦 System Requirements

- Orange Pi Zero 2 (or similar SBC)
- WiFi adapter (wlan0)
- Ethernet connection (end0) for internet sharing
- Debian-based Linux (tested on Armbian)

## 🚀 Quick Install

```bash
# Clone or download this project
cd PythonSSHLearningCenter

# Run installation script
sudo ./install.sh
```

That's it! The script handles:
- ✅ Installing all dependencies
- ✅ Configuring hostapd and dnsmasq
- ✅ Setting up shellinabox captive portal
- ✅ Configuring nginx redirects
- ✅ Installing Python learning examples
- ✅ Setting up welcome message
- ✅ Enabling auto-start on boot

## 📂 Project Structure

```
PythonSSHLearningCenter/
├── configs/
│   ├── dnsmasq/          # DNS and DHCP config
│   ├── hostapd/          # WiFi access point config
│   ├── nginx/             # Captive portal web config
│   ├── shellinabox/       # Terminal config and themes
│   └── systemd/           # Service files for auto-start
├── python-examples/
│   ├── games/             # Interactive Python games
│   ├── turtle/            # Turtle graphics examples
│   └── LEARN.md         # Python learning guide
├── scripts/
│   ├── setup-captive-portal-dns.sh  # DNS redirects
│   └── welcome-message.sh            # Login welcome screen
├── install.sh            # Automated installer
├── export-config.sh      # Export current configs
└── README.md            # This file
```

## 🎮 Python Examples Included

### Games (`python-examples/games/`)
- `hello.py` - First Python program with input/math
- `guess_number.py` - Classic number guessing game
- `adventure.py` - Choose-your-own-adventure story

### Turtle Art (`python-examples/turtle/`)
- `draw_shapes.py` - Learn to draw basic shapes
- `rainbow_turtle.py` - Colorful art with loops

See `python-examples/LEARN.md` for detailed explanations.

## 🔧 Manual Configuration

### Hotspot Network
- **SSID**: jailbreakBox
- **Gateway**: 192.168.12.1
- **DHCP Range**: 192.168.12.1 - 192.168.12.254
- **WiFi Interface**: wlan0
- **Internet Source**: end0 (ethernet)

### Captive Portal
- **Port**: HTTP 80 → redirects to 192.168.12.1:4200
- **Shellinabox**: Port 4200 (HTTP, no SSL)
- **Detection URLs**: Handles iOS/Android/Windows endpoints

## 📝 Usage

### Start/Stop Hotspot
```bash
sudo systemctl start create-ap-hotspot.service
sudo systemctl stop create-ap-hotspot.service
sudo systemctl status create-ap-hotspot.service
```

### Access Terminal
- **WiFi**: Connect to "jailbreakBox" network
- **Browser**: Captive portal auto-opens, or go to http://192.168.12.1:4200
- **Login**: Just press Enter (no password)

### Try Python Examples
```bash
cd ~/python-fun/games
python3 guess_number.py

cd ~/python-fun/turtle
python3 rainbow_turtle.py
```

## 🔍 Troubleshooting

### Hotspot not visible
```bash
sudo rfkill unblock wifi
sudo systemctl restart create-ap-hotspot.service
```

### Captive portal not working
```bash
curl http://127.0.0.1/  # Test locally
sudo systemctl restart shellinabox nginx
```

### No internet on clients
```bash
sudo iptables -t nat -L -n -v  # Check NAT rules
sudo systemctl restart create-ap-hotspot.service
```

### Turtle graphics won't open
- SSH may not support graphics
- Use device directly or enable X11 forwarding
- Ensure `python3-tk` is installed

## 🎓 Teaching Python with This Setup

This environment is designed for young coders (7+ years):

1. **Easy Access**: Browser-based terminal, no SSH client needed
2. **Passwordless**: Just connect WiFi and start typing
3. **Instant Feedback**: Run code and see results immediately
4. **Fun First**: Games before theory
5. **Encourages Exploration**: Break things, learn what works

See `python-examples/LEARN.md` for teaching tips and activity ideas.

## 🔐 Security Notes

- Open network (no WPA/WPA2) - use in trusted environment
- Passwordless login configured for easy access
- Sudo without password for the main user
- **System security intact** - only affects user account, not root

## 📚 Additional Resources

- Python Documentation: https://docs.python.org/3/
- Turtle Graphics: https://docs.python.org/3/library/turtle.html
- Raspberry Pi Projects (similar hardware): https://projects.raspberrypi.org/

## 🤝 Contributing

To add new Python examples:
1. Create file in appropriate `python-examples/` directory
2. Add clear comments explaining each step
3. Test the example
4. Commit and push changes

## 📄 License

Use as you wish.

---

**Perfect for:**
- Teaching kids to code
- Portable coding lab
- STEM education
- After-school programs
- Home learning environment

**Made with ❤️ for young coders**
