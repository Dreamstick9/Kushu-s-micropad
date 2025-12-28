import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)


encoder_handler.pins = (
    (board.D0, board.D1, None), # Left Encoder
    (board.D2, board.D3, None), # Right Encoder
)

keyboard.col_pins = (board.D6, board.D7, board.D8, board.D9, board.D10, board.D29)
keyboard.row_pins = (board.D4,) 
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    # Layer 0: The 6 Keys
    [
        KC.A, KC.B, KC.C,   # Top Row
        KC.D, KC.E, KC.F,   # Bottom Row
    ]
]

# Encoder Map (Left Rotate, Right Rotate, Press)
encoder_handler.map = [
    (
        (KC.VOLU, KC.VOLD, KC.MUTE), # Left Encoder: Volume Up/Down
        (KC.PGUP, KC.PGDN, KC.ENTER), # Right Encoder: Scroll Page
    ),
]

if __name__ == '__main__':
    keyboard.go()