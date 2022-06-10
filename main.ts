input.onGesture(Gesture.FreeFall, function () {
    basic.showLeds(`
        # . . . #
        . . . . .
        # # # # #
        # . . . #
        # # # # #
        `)
})
input.onGesture(Gesture.LogoDown, function () {
    soundExpression.spring.play()
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        # . . . #
        `)
    basic.pause(2000)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    soundExpression.hello.playUntilDone()
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showNumber(input.temperature())
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    soundExpression.hello.playUntilDone()
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    basic.clearScreen()
    basic.showString("OH!")
    soundExpression.sad.play()
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        `)
    basic.pause(5000)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    soundExpression.hello.playUntilDone()
})
input.onGesture(Gesture.Shake, function () {
    soundExpression.twinkle.play()
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . # .
        # . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # . . .
        . . . . #
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . # .
        # . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # . . .
        . . . . #
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    soundExpression.hello.playUntilDone()
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(1000)
    basic.clearScreen()
    basic.showString("for salah")
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    soundExpression.hello.playUntilDone()
})
input.onButtonPressed(Button.B, function () {
    soundExpression.soaring.play()
    basic.showLeds(`
        . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        # . . . .
        # . . . .
        # # . . .
        # . . . .
        # . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # . . .
        . # . . .
        # # # . .
        . # . . .
        . # . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . . # . .
        # # # # .
        . . # . .
        . . # . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . # .
        . . . # .
        # # # # #
        . . . # .
        . . . # .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . #
        . . . . #
        . # # # #
        . . . . #
        . . . . #
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # # #
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . # #
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(500)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    soundExpression.hello.playUntilDone()
})
input.onGesture(Gesture.ThreeG, function () {
    soundExpression.happy.play()
    basic.showIcon(IconNames.Heart)
    basic.pause(5000)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    soundExpression.hello.playUntilDone()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    soundExpression.happy.play()
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    basic.pause(5000)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    soundExpression.hello.playUntilDone()
})
soundExpression.hello.play()
basic.showString("Hello")
basic.pause(1000)
basic.showLeds(`
    # . . . #
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    `)
basic.forever(function () {
	
})
