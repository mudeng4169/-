let led2: neopixel.Strip = null
let voltage = 0
let temperature = 0
input.onButtonPressed(Button.A, function () {
    led2 = neopixel.create(DigitalPin.P1, 24, NeoPixelMode.RGB)
    led2.showRainbow(1, 360)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . # . .
        # . . . #
        # # # # #
        `)
    music.playMelody("C C G G A A G - ", 180)
    music.playMelody("F F E E D D C - ", 180)
    music.playMelody("G G F F E E D - ", 180)
    music.playMelody("G G F F E E D - ", 200)
    music.playMelody("C C G G A A G - ", 180)
    music.playMelody("F F E E D D C - ", 180)
    music.play(music.)
})
basic.forever(function () {
    voltage = pins.map(
    pins.analogReadPin(AnalogPin.P2),
    0,
    1023,
    0,
    3300
    )
    temperature = (voltage - 500) / 10
    basic.showNumber(temperature)
})
