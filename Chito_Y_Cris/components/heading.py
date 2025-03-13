import reflex as rx
from Chito_Y_Cris.styles.styles import Size
import Chito_Y_Cris.styles.styles as style

def heading(text: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            text,
            size="7",
            style=style.title_style
        )
    )
