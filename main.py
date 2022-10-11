led2: neopixel.Strip = None
voltage = 0
temperature = 0

def on_button_pressed_a():
    global led2
    led2 = neopixel.create(DigitalPin.P1, 24, NeoPixelMode.RGB)
    led2.show_rainbow(1, 360)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . # . .
                # . . . #
                # # # # #
    """)
    music.play_melody("C C G G A A G - ", 180)
    music.play_melody("F F E E D D C - ", 180)
    music.play_melody("G G F F E E D - ", 180)
    music.play_melody("G G F F E E D - ", 200)
    music.play_melody("C C G G A A G - ", 180)
    music.play_melody("F F E E D D C - ", 180)
    music.play(music.)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global voltage, temperature
    voltage = pins.map(pins.analog_read_pin(AnalogPin.P2), 0, 1023, 0, 3300)
    temperature = (voltage - 500) / 10
    basic.show_number(temperature)
basic.forever(on_forever)
