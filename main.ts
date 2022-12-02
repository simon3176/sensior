radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        basic.showIcon(IconNames.Skull)
    } else {
        basic.showIcon(IconNames.Cow)
    }
})
input.onButtonPressed(Button.A, function () {
    MODE = 1
})
input.onButtonPressed(Button.B, function () {
    MODE = 2
})
let Distance = 0
let MODE = 0
radio.setGroup(97)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P1, 0)
    control.waitMicros(2)
    pins.digitalWritePin(DigitalPin.P1, 1)
    control.waitMicros(10)
    pins.digitalWritePin(DigitalPin.P1, 0)
    Distance = pins.pulseIn(DigitalPin.P2, PulseValue.High) / 58
    basic.pause(2000)
    basic.showNumber(Distance)
})
basic.forever(function () {
    if (MODE == 1) {
        basic.showIcon(IconNames.No)
    } else if (MODE == 2) {
        basic.showIcon(IconNames.Yes)
    }
})
