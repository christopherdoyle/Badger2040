import config
import urequests

endpoint = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={config.OSRS_USERNAME}"


def main(badger):
    badger.set_pen(15)
    badger.clear()
    badger.set_pen(0)

    response = urequests.get(endpoint)
    parts = response.content.decode().split("\n")

    attack_level = parts[1].split(",")[1]
    strength_level = parts[3].split(",")[1]
    defence_level = parts[2].split(",")[1]

    badger.text(config.OSRS_USERNAME, 10, 5)
    badger.text(f"Attack: {attack_level}", 20, 25)
    badger.text(f"Strength: {strength_level}", 20, 40)
    badger.text(f"Defence: {defence_level}", 20, 55)

    badger.update()

    while True:
        badger.keepalive()
        badger.halt()
