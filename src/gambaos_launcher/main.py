import pygame, sverpykit as spk

screen = spk.set_display(500, 500)
font = spk.set_font()

ui = [
    spk.Button(
        rect=pygame.Rect(
            screen.get_width()/2 - 100,
            screen.get_height() - 100,
            200, 50
        ),
        button_color=(50, 50, 50),
        surface=spk.render_text("RUN"),
        display=screen,
    )
]

def frame():
    [part.update() for part in ui]

spk.set_frame_method(frame)
spk.start()