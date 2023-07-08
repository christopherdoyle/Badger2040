from typing import Any

import machine

BUTTON_DOWN: int
BUTTON_A: int
BUTTON_B: int
BUTTON_C: int
BUTTON_UP: int
BUTTON_USER: None
BUTTON_MASK: int
SYSTEM_VERY_SLOW: int
SYSTEM_SLOW: int
SYSTEM_NORMAL: int
SYSTEM_FAST: int
SYSTEM_TURBO: int
UPDATE_NORMAL: int
UPDATE_MEDIUM: int
UPDATE_FAST: int
UPDATE_TURBO: int
RTC_ALARM: int
LED: int
ENABLE_3V3: int
BUSY: int
WIDTH: int
HEIGHT: int
SYSTEM_FREQS: list[int]
BUTTONS: dict[int, machine.Pin]
WAKEUP_MASK: int
i2c: machine.I2C
rtc: Any
enable: machine.Pin

def is_wireless(): ...
def woken_by_rtc(): ...
def woken_by_button(): ...
def pressed_to_wake(button): ...
def reset_pressed_to_wake() -> None: ...
def pressed_to_wake_get_once(button): ...
def system_speed(speed) -> None: ...
def turn_on() -> None: ...
def turn_off() -> None: ...
def pico_rtc_to_pcf() -> None: ...
def pcf_to_pico_rtc(): ...
def sleep_for(minutes) -> None: ...

class Badger2040:
    display: PicoGraphics
    def __init__(self) -> None: ...
    def __getattr__(self, item): ...
    def update(self) -> None: ...
    def set_update_speed(self, speed) -> None: ...
    def led(self, brightness) -> None: ...
    def invert(self, invert) -> None: ...
    def thickness(self, thickness) -> None: ...
    def halt(self) -> None: ...
    def keepalive(self) -> None: ...
    def pressed(self, button): ...
    def pressed_any(self): ...
    def icon(self, data, index, data_w, icon_size, x, y) -> None: ...
    def image(self, data, w, h, x, y) -> None: ...
    def status_handler(self, mode, status, ip) -> None: ...
    def isconnected(self): ...
    def ip_address(self): ...
    def connect(self) -> None: ...