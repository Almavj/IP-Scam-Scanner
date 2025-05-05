#!/usr/bin/env python3
import os
import sys
import time
import requests
import socket
import re
import json
import platform
from netifaces import interfaces, ifaddresses, AF_INET
from datetime import datetime
from pyfiglet import Figlet
import random
import webbrowser
import geoip2.database
import whois
import dns.resolver
import csv
import logging
from concurrent.futures import ThreadPoolExecutor
import subprocess
from tqdm import tqdm
from typing import Dict, List, Optional, Tuple


class CosmicConfig:
    GEOIP_DATABASE = "GeoLite2-City.mmdb"
    MAP_PROVIDER = "https://www.google.com/maps?q={lat},{lon}"
    IP_API_URL = "http://ip-api.com/json/{ip}?fields=66846719"
    PUBLIC_IP_CHECK = "https://api.ipify.org?format=json"
    LOG_FILE = "ip_tracker_logs.json"
    EXPORT_DIR = "ip_reports"
    TRACEROUTE_MAX_HOPS = 30


class QuantumMagic:
    @staticmethod
    def quantum_rainbow(text):
        colors = ['\033[38;5;196m', '\033[38;5;202m', '\033[38;5;226m',
                 '\033[38;5;118m', '\033[38;5;33m', '\033[38;5;129m']
        return ''.join([f"{colors[i%6]}{char}" for i, char in enumerate(text)]) + '\033[0m'

    @staticmethod
    def animate_creation(text):
        for i in range(len(text)+1):
            print(f"\r{text[:i]}", end='', flush=True)
            time.sleep(0.02)
        print()

    @staticmethod
    def cosmic_quotes():
        quotes = [
            "Decrypting the digital cosmos...",
            "Warping through network dimensions...",
            "The network never lies...",
            "Mapping the digital universe..."
        ]
        return random.choice(quotes)

    @staticmethod
    def generate_crystal_ball():
        balls = ["🔮", "✨", "🌌", "🌀", "⚡"]
        return random.choice(balls)


class StellarColors:
    RED = "\033[38;5;196m"
    GREEN = "\033[38;5;46m"
    YELLOW = "\033[38;5;226m"
    BLUE = "\033[38;5;33m"
    PURPLE = "\033[38;5;129m"
    CYAN = "\033[38;5;51m"
    WHITE = "\033[38;5;255m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RAINBOW = QuantumMagic.quantum_rainbow


class GalacticNetwork:
    @staticmethod
    def validate_ip(ip):
        ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        return (re.match(ipv4_pattern, ip) or re.match(ipv6_pattern, ip))

    @staticmethod
    def is_private_ip(ip):
        patterns = [
            r'^10\.', r'^172\.(1[6-9]|2[0-9]|3[0-1])\.', 
            r'^192\.168\.', r'^169\.254\.', r'^127\.',
            r'^fc00::', r'^fd00::', r'^fe80::'
        ]
        return any(re.match(pattern, ip) for pattern in patterns)

    @staticmethod
    def get_local_network_crystals():
        network_info = []
        for interface in interfaces():
            addrs = ifaddresses(interface).get(AF_INET, [])
            for addr in addrs:
                if 'addr' in addr:
                    info = {
                        'interface': interface,
                        'ip': addr['addr'],
                        'netmask': addr.get('netmask', 'N/A'),
                        'broadcast': addr.get('broadcast', 'N/A'),
                        'type': 'Private' if GalacticNetwork.is_private_ip(addr['addr']) else 'Public',
                        'timestamp': datetime.now().isoformat()
                    }
                    network_info.append(info)
        return network_info

    @staticmethod
    def cosmic_public_ip():
        services = [
            'https://api.ipify.org?format=json',
            'https://ipinfo.io/json',
            'https://ifconfig.me/all.json'
        ]
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(requests.get, url, timeout=3) for url in services]
            for future in futures:
                try:
                    result = future.result()
                    if result.status_code == 200:
                        return result.json().get('ip', 'Unknown')
                except:
                    continue
        return 'Unknown'

    @staticmethod
    def reverse_dns_lookup(ip):
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            return hostname
        except (socket.herror, socket.gaierror):
            return "Not found"

    @staticmethod
    def get_asn_info(ip):
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}?fields=as")
            data = response.json()
            return data.get('as', 'Unknown')
        except:
            return "ASN lookup failed"

    @staticmethod
    def perform_whois(domain):
        try:
            w = whois.whois(domain)
            # Convert datetime objects to strings
            whois_data = {
                'registrar': w.registrar,
                'name_servers': w.name_servers
            }
            # Handle creation_date (could be list or single value)
            if w.creation_date:
                if isinstance(w.creation_date, list):
                    whois_data['creation_date'] = [d.isoformat() if d else None for d in w.creation_date]
                else:
                    whois_data['creation_date'] = w.creation_date.isoformat() if w.creation_date else None
            
            # Handle expiration_date (could be list or single value)
            if w.expiration_date:
                if isinstance(w.expiration_date, list):
                    whois_data['expiration_date'] = [d.isoformat() if d else None for d in w.expiration_date]
                else:
                    whois_data['expiration_date'] = w.expiration_date.isoformat() if w.expiration_date else None
            
            return whois_data
        except Exception as e:
            return f"Whois failed: {str(e)}"

    @staticmethod
    def cosmic_traceroute(ip):
        if platform.system() == "Windows":
            command = ["tracert", "-h", str(CosmicConfig.TRACEROUTE_MAX_HOPS), ip]
        else:
            command = ["traceroute", "-m", str(CosmicConfig.TRACEROUTE_MAX_HOPS), ip]
        
        try:
            print(f"\n{StellarColors.CYAN}🌀 Launching cosmic traceroute...{StellarColors.RESET}")
            result = subprocess.run(command, capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"Traceroute failed: {str(e)}"

# ==================== DISPLAY FUNCTIONS ====================
def display_cosmic_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    f = Figlet(font='starwars')
    banner = f.renderText('IP  GALAXY')
    print(StellarColors.RAINBOW(banner))
    
    crystal_ball = QuantumMagic.generate_crystal_ball()
    quote = QuantumMagic.cosmic_quotes()
    QuantumMagic.animate_creation(f"{crystal_ball} {StellarColors.PURPLE}{quote}{StellarColors.RESET}")
    
    print(f"{StellarColors.BLUE}╔════════════════════════════════════════════════════════════════════════════╗")
    print(f"║ {StellarColors.YELLOW}COSMIC IP TRACKER {StellarColors.WHITE}| {StellarColors.GREEN}Track Across Dimensions {StellarColors.WHITE}| {StellarColors.CYAN}By: Alma {StellarColors.BLUE}║")
    print(f"╚════════════════════════════════════════════════════════════════════════════╝{StellarColors.RESET}")
    print(f"{StellarColors.PURPLE}🌌 Version: 3.0 {StellarColors.WHITE}| {StellarColors.CYAN}GitHub: AlmaTech {StellarColors.WHITE}| {StellarColors.GREEN}Contact: +2547-8399142{StellarColors.RESET}\n")

def display_stellar_menu():
    menu_options = [
        ("Italy", StellarColors.CYAN, "🇮🇹"),
        ("Indonesia", StellarColors.GREEN, "🇮🇩"),
        ("Japan", StellarColors.BLUE, "🇯🇵"),
        ("United States", StellarColors.PURPLE, "🇺🇸"),
        ("France", StellarColors.RED, "🇫🇷"),
        ("Korea", StellarColors.YELLOW, "🇰🇷"),
        ("Germany", StellarColors.GREEN, "🇩🇪"),
        ("Turkey", StellarColors.CYAN, "🇹🇷"),
        ("Kenya", StellarColors.BLUE, "🇰🇪"),
        ("Exit", StellarColors.RED, "🚪")
    ]
    
    print(f"{StellarColors.YELLOW}╔════════════════════════════════════════════════════════════════════════════╗")
    print(f"║ {StellarColors.WHITE}{StellarColors.BOLD}SELECT A COSMIC DESTINATION:{StellarColors.YELLOW}                                       ║")
    print(f"╠════════════════════════════════════════════════════════════════════════════╣")
    
    for i in range(0, 10, 2):
        opt1 = menu_options[i]
        opt2 = menu_options[i+1] if i+1 < len(menu_options) else None
        
        line = "║ "
        line += f"{opt1[1]}{opt1[2]} [{i+1}] {opt1[0]:<15}{StellarColors.YELLOW}"
        if opt2:
            line += f"{opt2[1]}{opt2[2]} [{i+2}] {opt2[0]:<15}{StellarColors.YELLOW}"
        else:
            line += " " * 25
        print(line + "║")
    
    print(f"╚════════════════════════════════════════════════════════════════════════════╝{StellarColors.RESET}")

def show_local_network_crystals(ip, country_name):
    print(f"\n{StellarColors.PURPLE}🔮 [ Local Network - {country_name} ]{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}IP: {StellarColors.WHITE}{ip} {StellarColors.YELLOW}(Private){StellarColors.RESET}")
    
    local_info = GalacticNetwork.get_local_network_crystals()
    
    if local_info:
        print(f"\n{StellarColors.BLUE}🌐 Network Interfaces:{StellarColors.RESET}")
        for idx, info in enumerate(local_info, 1):
            print(f"\n{StellarColors.GREEN}Interface #{idx}:{StellarColors.RESET}")
            print(f"  {StellarColors.CYAN}Name: {StellarColors.WHITE}{info['interface']}{StellarColors.RESET}")
            print(f"  {StellarColors.CYAN}IP: {StellarColors.WHITE}{info['ip']}{StellarColors.RESET}")
            print(f"  {StellarColors.CYAN}Type: {StellarColors.WHITE}{info['type']}{StellarColors.RESET}")
            print(f"  {StellarColors.CYAN}Netmask: {StellarColors.WHITE}{info['netmask']}{StellarColors.RESET}")
            print(f"  {StellarColors.CYAN}Broadcast: {StellarColors.WHITE}{info['broadcast']}{StellarColors.RESET}")
    else:
        print(f"{StellarColors.RED}No network interfaces found!{StellarColors.RESET}")
    
    if input(f"\n{StellarColors.YELLOW}Track your public IP instead? (y/n): {StellarColors.RESET}").lower() == 'y':
        public_ip = GalacticNetwork.cosmic_public_ip()
        print(f"{StellarColors.CYAN}Your public IP: {StellarColors.WHITE}{public_ip}{StellarColors.RESET}")
        if input(f"{StellarColors.YELLOW}Track this IP? (y/n): {StellarColors.RESET}").lower() == 'y':
            return track_across_dimensions(public_ip, country_name)
    
    return True

def display_geoip_results(data: Dict, country_name: str):
    print(f"\n{StellarColors.GREEN}🌍 [ GeoIP2 - {country_name} ]{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}IP: {StellarColors.WHITE}{data.get('ip', 'N/A')}{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}Country: {StellarColors.WHITE}{data.get('country', 'N/A')}{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}Region: {StellarColors.WHITE}{data.get('region', 'N/A')}{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}City: {StellarColors.WHITE}{data.get('city', 'N/A')}{StellarColors.RESET}")
    
    # Handle coordinates with Google Maps link
    if 'coordinates' in data and isinstance(data['coordinates'], (tuple, list)) and len(data['coordinates']) == 2:
        lat, lon = data['coordinates']
        print(f"{StellarColors.CYAN}Coordinates: {StellarColors.WHITE}{lat}, {lon}{StellarColors.RESET}")
        map_url = CosmicConfig.MAP_PROVIDER.format(lat=lat, lon=lon)
        print(f"{StellarColors.CYAN}Google Maps: {StellarColors.WHITE}{map_url}{StellarColors.RESET}")
        
        # Auto-open map if coordinates are valid
        if input(f"{StellarColors.YELLOW}Open in Google Maps? (y/n): {StellarColors.RESET}").lower() == 'y':
            webbrowser.open(map_url)
    else:
        print(f"{StellarColors.YELLOW}Coordinates: Not available{StellarColors.RESET}")
    
    print(f"{StellarColors.CYAN}Timezone: {StellarColors.WHITE}{data.get('timezone', 'N/A')}{StellarColors.RESET}")

def display_ipapi_results(data: Dict, country_name: str):
    print(f"\n{StellarColors.BLUE}🌐 [ IP-API - {country_name} ]{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}IP: {StellarColors.WHITE}{data.get('query', 'N/A')}{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}Country: {StellarColors.WHITE}{data.get('country', 'N/A')}{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}Region: {StellarColors.WHITE}{data.get('regionName', 'N/A')}{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}City: {StellarColors.WHITE}{data.get('city', 'N/A')}{StellarColors.RESET}")
    
    # Handle coordinates with Google Maps link
    lat = data.get('lat')
    lon = data.get('lon')
    if lat is not None and lon is not None:
        print(f"{StellarColors.CYAN}Coordinates: {StellarColors.WHITE}{lat}, {lon}{StellarColors.RESET}")
        map_url = CosmicConfig.MAP_PROVIDER.format(lat=lat, lon=lon)
        print(f"{StellarColors.CYAN}Google Maps: {StellarColors.WHITE}{map_url}{StellarColors.RESET}")
        
        # Auto-open map if coordinates are valid
        if input(f"{StellarColors.YELLOW}Open in Google Maps? (y/n): {StellarColors.RESET}").lower() == 'y':
            webbrowser.open(map_url)
    else:
        print(f"{StellarColors.YELLOW}Coordinates: Not available{StellarColors.RESET}")
    
    print(f"{StellarColors.CYAN}ISP: {StellarColors.WHITE}{data.get('isp', 'N/A')}{StellarColors.RESET}")

def serialize_complex(obj):
    """Handle serialization of complex objects"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, (list, tuple, set)):
        return [serialize_complex(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: serialize_complex(v) for k, v in obj.items()}
    elif hasattr(obj, '__dict__'):
        return serialize_complex(vars(obj))
    return str(obj)

def display_cosmic_insights(data: Dict):
    print(f"\n{StellarColors.PURPLE}✨ [ Cosmic Insights ]{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}Reverse DNS: {StellarColors.WHITE}{data.get('reverse_dns', 'N/A')}{StellarColors.RESET}")
    print(f"{StellarColors.CYAN}ASN Info: {StellarColors.WHITE}{data.get('asn_info', 'N/A')}{StellarColors.RESET}")
    
    # Display whois information if available
    if isinstance(data.get('whois'), dict):
        print(f"\n{StellarColors.CYAN}Whois Information:{StellarColors.RESET}")
        whois_data = data['whois']
        print(f"{StellarColors.CYAN}Registrar: {StellarColors.WHITE}{whois_data.get('registrar', 'N/A')}{StellarColors.RESET}")
        
        # Handle creation date (could be list or single value)
        creation_date = whois_data.get('creation_date')
        if creation_date:
            if isinstance(creation_date, list):
                creation_date = creation_date[0] if creation_date else None
            print(f"{StellarColors.CYAN}Creation Date: {StellarColors.WHITE}{creation_date}{StellarColors.RESET}")
        
        # Handle expiration date (could be list or single value)
        expiration_date = whois_data.get('expiration_date')
        if expiration_date:
            if isinstance(expiration_date, list):
                expiration_date = expiration_date[0] if expiration_date else None
            print(f"{StellarColors.CYAN}Expiration Date: {StellarColors.WHITE}{expiration_date}{StellarColors.RESET}")
        
        # Display name servers if available
        name_servers = whois_data.get('name_servers')
        if name_servers:
            print(f"{StellarColors.CYAN}Name Servers:{StellarColors.RESET}")
            for ns in (name_servers if isinstance(name_servers, list) else [name_servers]):
                print(f"{StellarColors.WHITE}- {ns}{StellarColors.RESET}")
    
    # Display traceroute results if requested
    if input(f"\n{StellarColors.YELLOW}Show traceroute results? (y/n): {StellarColors.RESET}").lower() == 'y':
        print(f"\n{StellarColors.CYAN}🌀 Traceroute Results:{StellarColors.RESET}")
        print(data.get('traceroute', 'N/A'))

def log_cosmic_journey(data: Dict):
    """Save tracking data to JSON log file with proper serialization"""
    os.makedirs(CosmicConfig.EXPORT_DIR, exist_ok=True)
    
    try:
        with open(os.path.join(CosmicConfig.EXPORT_DIR, CosmicConfig.LOG_FILE), 'a') as f:
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'data': serialize_complex(data)
            }
            json.dump(log_entry, f, indent=2)
            f.write('\n')
    except Exception as e:
        print(f"{StellarColors.RED}Failed to log journey: {e}{StellarColors.RESET}")

def offer_data_export(data: Dict):
    """Export data to JSON/CSV with comprehensive handling"""
    if input(f"\n{StellarColors.YELLOW}Export this data? (y/n): {StellarColors.RESET}").lower() != 'y':
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ip_report_{timestamp}"
    os.makedirs(CosmicConfig.EXPORT_DIR, exist_ok=True)
    
    # JSON Export
    json_path = os.path.join(CosmicConfig.EXPORT_DIR, f"{filename}.json")
    try:
        with open(json_path, 'w') as f:
            json.dump(serialize_complex(data), f, indent=4)
        print(f"{StellarColors.GREEN}JSON report saved to {json_path}{StellarColors.RESET}")
    except Exception as e:
        print(f"{StellarColors.RED}Failed to create JSON: {e}{StellarColors.RESET}")

    # CSV Export
    csv_path = os.path.join(CosmicConfig.EXPORT_DIR, f"{filename}.csv")
    try:
        flat_data = {
            'ip': data.get('ip', ''),
            'country': data.get('country', ''),
            'timestamp': datetime.now().isoformat(),
            'reverse_dns': data.get('reverse_dns', ''),
            'asn_info': data.get('asn_info', ''),
            'latitude': '',
            'longitude': '',
            'map_url': ''
        }

        # Extract coordinates from all sources
        for source in data.get('sources', []):
            if 'coordinates' in source and isinstance(source['coordinates'], (list, tuple)) and len(source['coordinates']) == 2:
                flat_data['latitude'], flat_data['longitude'] = source['coordinates']
                flat_data['map_url'] = CosmicConfig.MAP_PROVIDER.format(lat=flat_data['latitude'], lon=flat_data['longitude'])
            elif 'lat' in source and 'lon' in source:
                flat_data['latitude'] = source['lat']
                flat_data['longitude'] = source['lon']
                flat_data['map_url'] = CosmicConfig.MAP_PROVIDER.format(lat=source['lat'], lon=source['lon'])

        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=flat_data.keys())
            writer.writeheader()
            writer.writerow(flat_data)
        print(f"{StellarColors.GREEN}CSV report saved to {csv_path}{StellarColors.RESET}")
    except Exception as e:
        print(f"{StellarColors.RED}Failed to create CSV: {e}{StellarColors.RESET}")

# ==================== CORE TRACKING FUNCTION ====================
def track_across_dimensions(ip, country_name):
    if not GalacticNetwork.validate_ip(ip):
        print(f"\n{StellarColors.RED}⚠ Invalid IP address format!{StellarColors.RESET}")
        return False
    
    if GalacticNetwork.is_private_ip(ip):
        return show_local_network_crystals(ip, country_name)
    
    try:
        cosmic_data = {
            'ip': ip,
            'country': country_name,
            'timestamp': datetime.now().isoformat(),
            'sources': []
        }
        
        # Try GeoIP2 database first
        try:
            with geoip2.database.Reader(CosmicConfig.GEOIP_DATABASE) as reader:
                response = reader.city(ip)
                geoip_data = {
                    'source': 'GeoIP2',
                    'country': response.country.name,
                    'region': response.subdivisions.most_specific.name,
                    'city': response.city.name,
                    'postal': response.postal.code,
                    'coordinates': (response.location.latitude, response.location.longitude),
                    'timezone': response.location.time_zone,
                    'accuracy': response.location.accuracy_radius
                }
                cosmic_data['sources'].append(geoip_data)
                display_geoip_results(geoip_data, country_name)
        except Exception as geoip_error:
            pass
        
        # Try IP-API
        try:
            headers = {'User-Agent': 'CosmicIPTracker/3.0'}
            response = requests.get(CosmicConfig.IP_API_URL.format(ip=ip), headers=headers, timeout=10)
            api_data = response.json()
            
            if api_data.get('status') == 'success':
                ipapi_data = {
                    'source': 'IP-API',
                    'country': api_data.get('country'),
                    'region': api_data.get('regionName'),
                    'city': api_data.get('city'),
                    'isp': api_data.get('isp'),
                    'org': api_data.get('org'),
                    'as': api_data.get('as'),
                    'lat': api_data.get('lat'),
                    'lon': api_data.get('lon'),
                    'timezone': api_data.get('timezone'),
                    'zip': api_data.get('zip'),
                    'reverse_dns': api_data.get('reverse')
                }
                cosmic_data['sources'].append(ipapi_data)
                display_ipapi_results(ipapi_data, country_name)
        except Exception as api_error:
            pass
        
        # Additional cosmic data
        cosmic_data.update({
            'reverse_dns': GalacticNetwork.reverse_dns_lookup(ip),
            'asn_info': GalacticNetwork.get_asn_info(ip),
            'whois': GalacticNetwork.perform_whois(ip),
            'traceroute': GalacticNetwork.cosmic_traceroute(ip)
        })
        
        display_cosmic_insights(cosmic_data)
        log_cosmic_journey(cosmic_data)
        offer_data_export(cosmic_data)
        
        return True
        
    except Exception as e:
        print(f"\n{StellarColors.RED}Cosmic Tracking Error: {e}{StellarColors.RESET}")
        return False

# ==================== MAIN COSMIC FLOW ====================
def main():
    try:
        os.makedirs(CosmicConfig.EXPORT_DIR, exist_ok=True)
        
        while True:
            display_cosmic_banner()
            display_stellar_menu()
            
            choice = input(f"\n{StellarColors.WHITE}[{StellarColors.RED}?{StellarColors.WHITE}] Select cosmic destination (1-10): {StellarColors.RESET}").strip()
            
            if choice == "10":
                QuantumMagic.animate_creation(f"{StellarColors.RED}Returning to earthly realm...{StellarColors.RESET}")
                time.sleep(1)
                sys.exit()
                
            country_map = {
                "1": ("Italy", "🇮🇹"),
                "2": ("Indonesia", "🇮🇩"),
                "3": ("Japan", "🇯🇵"),
                "4": ("United States", "🇺🇸"),
                "5": ("France", "🇫🇷"),
                "6": ("Korea", "🇰🇷"),
                "7": ("Germany", "🇩🇪"),
                "8": ("Turkey", "🇹🇷"),
                "9": ("Kenya", "🇰🇪")
            }
            
            if choice in country_map:
                country_name, flag = country_map[choice]
                ip = input(f"\n{flag} {StellarColors.YELLOW}Enter IP to track in {country_name} (blank for your IP): {StellarColors.RESET}").strip()
                
                if not ip:
                    ip = GalacticNetwork.cosmic_public_ip()
                    print(f"{StellarColors.CYAN}Using your public IP: {StellarColors.WHITE}{ip}{StellarColors.RESET}")
                    time.sleep(1)
                
                track_across_dimensions(ip, country_name)
                input(f"\n{StellarColors.GREEN}Press Enter to continue cosmic exploration...{StellarColors.RESET}")
            else:
                print(f"{StellarColors.RED}Invalid cosmic coordinates!{StellarColors.RESET}")
                time.sleep(2)
                
    except KeyboardInterrupt:
        QuantumMagic.animate_creation(f"\n{StellarColors.RED}Cosmic journey interrupted!{StellarColors.RESET}")
        sys.exit(0)

if __name__ == '__main__':
    try:
        import geoip2
        import pyfiglet
        import netifaces
        import whois
        import dns
        import tqdm
    except ImportError as e:
        print(f"{StellarColors.RED}Missing cosmic component: {e}{StellarColors.RESET}")
        print(f"{StellarColors.YELLOW}Run: pip install geoip2 pyfiglet netifaces python-whois dnspython tqdm{StellarColors.RESET}")
        sys.exit(1)
    
    if not os.path.exists(CosmicConfig.GEOIP_DATABASE):
        print(f"{StellarColors.YELLOW}For ultimate cosmic tracking, download GeoLite2 database:{StellarColors.RESET}")
        print(f"{StellarColors.CYAN}https://dev.maxmind.com/geoip/geolite2-free-geolocation-data{StellarColors.RESET}")
        print(f"{StellarColors.PURPLE}Place the .mmdb file in the same directory as this script{StellarColors.RESET}")
    
    main()