def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_icon(IconNames.SKULL)
    else:
        basic.show_icon(IconNames.COW)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global MODE
    MODE = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global MODE
    MODE = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

Distance = 0
MODE = 0
radio.set_group(97)
basic.show_icon(IconNames.YES)

def on_forever():
    global Distance
    pins.digital_write_pin(DigitalPin.P1, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P1, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P1, 0)
    Distance = pins.pulse_in(DigitalPin.P2, PulseValue.HIGH) / 58
    basic.pause(2000)
    basic.show_number(Distance)
basic.forever(on_forever)

def on_forever2():
    if MODE == 1:
        basic.show_icon(IconNames.NO)
    elif MODE == 2:
        basic.show_icon(IconNames.YES)
basic.forever(on_forever2)
