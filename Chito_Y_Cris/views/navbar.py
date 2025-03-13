import reflex as rx
from Chito_Y_Cris.styles.colors import Colors as Color
from Chito_Y_Cris.styles.styles import Size
import Chito_Y_Cris.styles.styles as style


def navbar() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.text(
                rx.text.strong("Chito ", style=style.title_style),"y", rx.text.strong(" Cris", style=style.title_style),
            )
        ),
        positions="sticky",
        bg=Color.BLACK.value,
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0",
    )



