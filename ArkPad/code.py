import board
import digitalio
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys


led_connected = digitalio.DigitalInOut(board.GP26)  
led_connected.direction = digitalio.Direction.OUTPUT
led_connected.value = True  # Always on

led_pressed = digitalio.DigitalInOut(board.GP27)   
led_pressed.direction = digitalio.Direction.OUTPUT
led_pressed.value = False

class MyMacropad(KMKKeyboard):
    def __init__(self):
        self.row_pins = (board.GP10, board.GP11, board.GP12)
        self.col_pins = (board.GP13, board.GP14, board.GP15, board.GP16)
        self.diode_orientation = "COL2ROW"  # Test ROW2COL if no keys

        self.keymap = [
            [
                KC.LALT(KC.F4), KC.LWIN(KC.DOT), KC.CTRL(KC.SHIFT(KC.ESC)), KC.NO,     # Row 1
                KC.CTRL(KC.Z),  KC.CTRL(KC.Y),      KC.F5,                 KC.LWIN(KC.PRINT_SCREEN),  # Row 2
                KC.CTRL(KC.C),  KC.CTRL(KC.V),      KC.LWIN(KC.V),         KC.NO,                     # Row 3
            ]
        ]

    def before_matrix_scan(self, sandbox):
        led_pressed.value = any(sandbox.key_matrix)

keyboard = MyMacropad()
keyboard.modules = [Layers(), MediaKeys()]

keyboard.go()