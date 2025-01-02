def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_string("Button A pressed bruh")
basic.forever(on_forever)
