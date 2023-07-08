import time

import config
import network
import rp2
import uasyncio
import ubinascii

nic = network.WLAN(network.STA_IF)


async def connect(ssid, pwd):
    max_connect_wait_secs = 20
    if not nic.isconnected():
        my_mac_address = ubinascii.hexlify(nic.config("mac"), ":").decode()
        print(f"MAC: {my_mac_address}")

        print(f"Connecting to '{ssid}'", end="")
        nic.active(True)
        # power saving mode
        nic.config(pm=0xA11140)
        nic.connect(ssid, pwd)

        start_time = time.time()
        i = 0
        while not nic.isconnected():
            if i % 10:
                print(".", end="")
            time.sleep(0.1)
            if time.time() - start_time >= max_connect_wait_secs:
                print(f"Failed to connect to '{ssid}'")
                break
            i += 1
        print("")


def init(badger):
    rp2.country(config.COUNTRY)
    loop = uasyncio.get_event_loop()
    loop.run_until_complete(connect(config.SSID, config.PSK))


def main(badger):
    if nic.isconnected():
        ip_address_str = nic.ifconfig()[0]
        msg = f"Connected: {ip_address_str}"
    else:
        msg = "Not connected"

    print(msg)
    badger.text(msg, 10, 40)
    badger.update()

    while True:
        badger.keepalive()
        badger.halt()
