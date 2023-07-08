import programs

import badger2040


def main():
    # needed for wifi to work...?
    badger2040.system_speed(badger2040.SYSTEM_FAST)
    badger = badger2040.Badger2040()
    badger.set_update_speed(badger2040.UPDATE_FAST)

    badger.set_pen(15)
    badger.clear()
    badger.set_pen(0)
    badger.text("Initializing", 20, 20)
    badger.update()

    programs.net.init(badger)

    badger.set_pen(15)
    badger.clear()
    badger.set_pen(0)
    badger.text("BADGER BADGER BADGER", 20, 20)
    badger.update()

    while True:
        badger.keepalive()

        if badger.pressed(badger2040.BUTTON_A):
            programs.net.main(badger)
        elif badger.pressed(badger2040.BUTTON_B):
            programs.status.main(badger)

        badger.halt()


if __name__ == "__main__":
    main()
