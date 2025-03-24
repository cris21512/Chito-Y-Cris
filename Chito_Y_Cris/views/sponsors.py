import reflex as rx
from Chito_Y_Cris.components.link_sponsors import link_sponsor
from Chito_Y_Cris.constants import conts
from Chito_Y_Cris.styles.styles import Size, Spacing
from Chito_Y_Cris.components.heading import heading


def sponsors() -> rx.Component:
    return rx.vstack(
        heading("Con el apoyo de:"),
        rx.flex(
            link_sponsor(
                "/logoM.svg",
                conts.GITHUB,
                "Logo de Master"
            ),
            link_sponsor(
                "/logoCC.svg",
                conts.TIKTOK,
                "Logotipo de ChitoyCris"
            ),
            spacing="5",
            flex_direction=["column", "row"]
        ),
        width="100%",
        align_items="start",
        spacing="5"
    )
