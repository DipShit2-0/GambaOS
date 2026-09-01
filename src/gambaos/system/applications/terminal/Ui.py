from src.gambaos.system.GambaOS import Config
import sverpykit as spk, pygame

def add_layers():
    rect = (
            Config.screen.get_width()/2 - Config.screen.get_width()/4,
            Config.screen.get_height()/2 - Config.screen.get_height()/4,
            Config.screen.get_width()/2,
            Config.screen.get_height()/2
    )
    spk.add_layer(
        layer_type="window",
        rectangle=pygame.Rect(*rect),
        components=[
            spk.TextBlock(
                pygame.Rect(0, 0, rect[2], rect[3]),
                ">>"
            ),
            spk.SearchBar(
                rect=pygame.Rect(
                    0,
                    rect[3]-30,
                    rect[2],
                    30
                ),
                display=Config.screen
            )
        ],
        color=(50, 50, 50)
    )