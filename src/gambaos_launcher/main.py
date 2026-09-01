import pygame, sverpykit as spk

screen = spk.set_display(500, 500)
pygame.display.set_caption("GambaOS Launcher")
font = spk.set_font()

def start_gamba_os():
    import src.gambaos.system.GambaOS.main

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
        function=start_gamba_os
    )
]

def frame():
    [part.update() for part in ui]

spk.set_frame_method(frame)
spk.start()