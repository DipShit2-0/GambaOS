import pygame, sverpykit as spk
import src.gambaos.system.GambaOS.Config as Config

welcome_text = spk.render_text("Welcome To GambaOS!!!")
def frame():
    spk.draw_surface(welcome_text, (0, 0))

spk.set_frame_method(frame)
spk.start()