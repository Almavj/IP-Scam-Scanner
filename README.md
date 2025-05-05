# 🌌 IP Galaxy - Cosmic IP Tracker

![Screenshot_2025-05-05_11_51_26](https://github.com/user-attachments/assets/2108813b-f4a2-4af7-a044-efcc6f9c92ef)


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
## GeoIP Database Setup

1. Get a free [MaxMind license key](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data)
2. Run this secure download command:
   ```bash
   read -sp "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: " k && \
   wget -qO- "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=${k}&suffix=tar.gz" | \
   tar -xz --strip-components=1 -C ./data/ GeoLite2-City_*/GeoLite2-City.mmdb && \
   unset k
# 2. Extract
tar -xvzf GeoLite2-City.tar.gz

# 3. Move the .mmdb file to your data directory
cp GeoLite2-City_*/GeoLite2-City.mmdb ./data/

# 4. Clean up
rm GeoLite2-City.tar.gz
tar -xvzf GeoLite2-City.tar.gz
cp GeoLite2-City_*/GeoLite2-City.mmdb ./data/
