# 🌌 IP Galaxy - Cosmic IP Tracker

![Banner](Documents/python/s![screenshot](https://github.com/user-attachments/assets/546d4dea-ec56-4c8f-836a-e133c812f2de)
creenshot.jpeg)

A multi-dimensional IP tracking tool that provides cosmic-level insights about IP addresses across different countries.

## Features

- 🌍 GeoIP tracking with visual maps
- 🔮 Whois information and DNS lookups
- 🌀 Traceroute visualization
- 📊 Data export capabilities
- 🌈 Beautiful terminal interface

## Installation

# 1. Clone the repository
git clone https://github.com/Almavj/ip-scam-scanner.git

# 2. Navigate to the project folder
cd ip-scam-scanner

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download GeoIP database (Required)
wget "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=YOUR_LICENSE&suffix=tar.gz" -O GeoLite2-City.tar.gz
tar -xvzf GeoLite2-City.tar.gz
cp GeoLite2-City_*/GeoLite2-City.mmdb ./data/
