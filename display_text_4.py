from sense_hat import SenseHat

sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)

sense.show_message("Hello World!", text_colour=blue, back_colour=yellow, scroll_speed=0.2)