import reflex as rx
from Chito_Y_Cris.components.heading import heading
from Chito_Y_Cris.components.icon_link import icon_link
from Chito_Y_Cris.components.info import info
import Chito_Y_Cris.styles.styles as style
import Chito_Y_Cris.constants.conts as const
from Chito_Y_Cris.components.info_text import info_text
from Chito_Y_Cris.styles.colors import Colors as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/avatar.jpg",
                radius="full",
                size="8",
                style={
                    "border": "3px solid #393d42",
                    "box-shadow": "#19191a",
                    "transition": "0.3s",
                    "_hover": {
                        "box-shadow": f"0 0 25px {Color.TERCIARY.value}",
                        "border": f"3px solid {Color.TERCIARY.value}",
                    }
                }
                ),
                rx.vstack(
                heading("Chito y Cris"),
                rx.text("@chito2.1.2", style=style.text_style),
                rx.hstack(
                    icon_link(
                        "icons/tiktok.svg",
                        const.TIKTOK
                    ),
                    icon_link(
                        "icons/instagram.svg",
                        const.IG
                    ),
                    icon_link(
                        "icons/twitch.svg",
                        const.TWITCH
                    ),
                    icon_link(
                        "icons/github.svg",
                        const.GITHUB
                    ),
                    icon_link(
                        "icons/youtube.svg",
                        const.YOUTUBE
                    ),
                    spacing="5"
                ),
                ),
            ),
            rx.flex(
                info_text("+45k ", "Seguidores"),
                rx.spacer(),
                info_text("+600k ", "Likes"),
                rx.spacer(),
                info_text("+50 ", "Recetas"),
                width="100%",
                spacing="2",
                style=style.text_style,
                flex_direction="row",
            ),
            rx.text(
                """
                ¡Bienvenidos a la página oficial de Chito y Cris! En este espacio encontrarás un poco de nuestro contenido...
                El contenido estará dividido en varias secciones para que encuentres fácilmente lo que buscas.
                Si tienes alguna duda o sugerencia, no dudes en contactarnos a través de nuestras redes sociales. ¡Estamos aquí para ayudarte!
                """,
                text_wrap="wrap",
                style=style.text_style
            ),
        align_items="start",
        spacing="6",
        width="100%"
    )


