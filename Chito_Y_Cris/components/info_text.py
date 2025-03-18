import reflex as rx
from Chito_Y_Cris.styles.colors import Colors as Colors, TextColor
from Chito_Y_Cris.styles.styles import Size


def info_text(title: str, body:str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=Colors.TERCIARY.value
        ),
        f"{body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.SUBTITLE.value,
    )