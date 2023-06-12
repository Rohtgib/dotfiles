from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Dracula(ColorScheme):
    progress_bar_color = 13

    def __init__(self):
        super(Dracula, self).__init__()

        # Define the colors
        self.colors = {
            'default': default,
            'normal': default,
            'bold': bold,
            'reverse': reverse,

            'foreground': white,
            'background': black,
            'cursor': white,

            'color0': black,
            'color1': red,
            'color2': green,
            'color3': yellow,
            'color4': blue,
            'color5': magenta,
            'color6': cyan,
            'color7': white,
            'color8': black,
            'color9': red,
            'color10': green,
            'color11': yellow,
            'color12': blue,
            'color13': magenta,
            'color14': cyan,
            'color15': white,
        }

        # Apply the colors to the elements
        self.colorize()

default_colorscheme = Dracula()

