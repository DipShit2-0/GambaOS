import screeninfo, pygame, sverpykit as spk

monitors = screeninfo.get_monitors()
primary_monitor = None
for monitor in monitors:
    if monitor.is_primary:
        primary_monitor = monitor
if not primary_monitor:
    primary_monitor = monitors[0]

pygame.quit()
pygame.init()

screen = spk.set_display(primary_monitor.width, primary_monitor.height, pygame.FULLSCREEN)
font = spk.set_font()