import ipaddress
import microcontroller
import os
import socketpool
import time
import wifi

def connect_to_wifi():
    print("Retrieving Wifi configuration from settings.toml")
    wifi_ssid = os.getenv("WIFI_SSID")
    wifi_pass = os.getenv("WIFI_PASSWORD")

    print(f"Connecting to '{wifi_ssid}'")
    wifi.radio.connect(wifi_ssid, wifi_pass)

    print("Connected!")

def print_wifi_info():
    print("****\nWifi Info\n****")
    print("MAC Address:", [hex(i) for i in wifi.radio.mac_address])
    print("IP Address:", wifi.radio.ipv4_address)

def ping(ipv4_str):
    ipv4 = ipaddress.ip_address(ipv4_str)
    time_to_ping_ms = wifi.radio.ping(ipv4)*1000
    print(f"Ping {ipv4_str}: {time_to_ping_ms} ms")
    return time_to_ping_ms

def update_clock_position(ms):
    # TODO: Update clock position to point to new ms value
    print(f"Updating clock position: {ms}")


def main():
    print("Initializing...")
    connect_to_wifi()
    print_wifi_info()
    # Ping 1.1.1.1 Dns provider every second
    while True:
        time_to_ping = ping("1.1.1.1")
        update_clock_position(time_to_ping)
        # Wait 1 second before next iteration of the loop
        time.sleep(1)

try:
    main()
except ConnectionError as connection_error:
    print("Error Connecting to Wifi")
    print(connection_error.errno)
except Exception as error:
    print(f"Error:\n{error}")
    print("Resetting Microcontroller in 1 minute")
    time.sleep(60)
    microcontroller.reset()

