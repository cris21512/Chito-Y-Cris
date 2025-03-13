from enum import Enum
import reflex as rx 
from Chito_Y_Cris.styles.colors import Colors, TextColor


#MAX WIDTHS
MAX_WIDTH = "600px"

#Enums
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Montserrat:wght@400;700&family=Raleway:ital,wght@1,500&display=swap"
    "https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;600&display=swap"
]


BASE_STYLE = {
    "background": "#19191a",
#
    rx.link:{
        "text_decoration": "none",
        "_hover":{}
    }
}

title_style = {
    "font_family": "'Raleway', sans-serif",
    "font_weight": "600",
    "font_style": "italic",
    "color": TextColor.TITLE.value,
}

sub_title_style = {
    "font_family": "'Montserrat', sans-serif",
    "font_weight": "400",
    "font-size": "1em",
    "color": TextColor.SUBTITLE.value,
}

text_style = {
    "font-family": "Poppins",
    "color": TextColor.BODY.value,
    "font-size": "1.2em",
}

