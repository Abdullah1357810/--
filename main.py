def on_pin_pressed_p0():
    basic.show_number(input.sound_level())
    music.set_built_in_speaker_enabled(True)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_gesture_free_fall():
    basic.show_leds("""
        # . . . #
                . . . . .
                # # # # #
                # . . . #
                # # # # #
    """)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_gesture_logo_down():
    soundExpression.spring.play()
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                # . . . #
    """)
    basic.pause(2000)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    soundExpression.hello.play_until_done()
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_a():
    basic.clear_screen()
    basic.show_number(input.temperature())
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    soundExpression.hello.play_until_done()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_long_pressed():
    basic.clear_screen()
    basic.show_string("OH!")
    soundExpression.sad.play()
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
    """)
    basic.pause(5000)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    soundExpression.hello.play_until_done()
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_gesture_shake():
    soundExpression.twinkle.play()
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . # .
                # . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . # . . .
                . . . . #
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . # .
                # . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . # . . .
                . . . . #
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    soundExpression.hello.play_until_done()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_icon(IconNames.HEART)
    basic.pause(1000)
    basic.clear_screen()
    basic.show_string("for salah")
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    soundExpression.hello.play_until_done()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    soundExpression.soaring.play()
    basic.show_leds("""
        . . . . .
                . . . . .
                # . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        # . . . .
                # . . . .
                # # . . .
                # . . . .
                # . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . # . . .
                . # . . .
                # # # . .
                . # . . .
                . # . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
                . . # . .
                # # # # .
                . . # . .
                . . # . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . # .
                . . . # .
                # # # # #
                . . . # .
                . . . # .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . #
                . . . . #
                . # # # #
                . . . . #
                . . . . #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # # #
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . # #
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . #
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(500)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    soundExpression.hello.play_until_done()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_three_g():
    soundExpression.happy.play()
    basic.show_icon(IconNames.HEART)
    basic.pause(5000)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    soundExpression.hello.play_until_done()
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

def on_logo_pressed():
    soundExpression.happy.play()
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    basic.pause(5000)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    soundExpression.hello.play_until_done()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

soundExpression.hello.play()
basic.show_string("Hello")
basic.pause(1000)
basic.show_leds("""
    # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
""")

def on_forever():
    pass
basic.forever(on_forever)
