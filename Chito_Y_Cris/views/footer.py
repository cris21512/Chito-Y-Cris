import reflex as rx
from Chito_Y_Cris.styles.styles import Size
import datetime
import Chito_Y_Cris.constants.conts as const
from Chito_Y_Cris.styles.colors import Colors as Color



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.jpg",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="logo chito y cris"
        ),
        rx.link(
            rx.box(
                f"© 2023-{datetime.date.today().year} ",
                rx.text(
                    "Chito y Cris",
                    as_="span",
                    color=Color.SECONDARY.value
                ),
                padding_top=Size.DEFAULT.value
            ),
            href=const.TIKTOK,
            is_external=True,
            font_size=Size.MEDIUM.value,
        ),
        rx.link(
            rx.hstack(
                rx.text(
                    "| Todos los derechos Reservados",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                )
            ),
            href=const.TIKTOK,
            is_external=True,
        ),
        align="center",
        width="100%",
    )