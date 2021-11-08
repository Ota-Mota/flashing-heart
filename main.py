def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.SMALL_HEART)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

