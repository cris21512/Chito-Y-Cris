import reflex as rx
from Chito_Y_Cris.styles.styles import Size, Spacing
import Chito_Y_Cris.styles.styles as style
import Chito_Y_Cris.styles.colors as Colors
from Chito_Y_Cris.styles.colors import Colors, TextColor




def link_button(
        title:str, 
        body:str, 
        image:str, 
        url: str, 
        hover_color: str,
        hover_box:str
    ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(
                        title,
                        size=Spacing.SMALL.value,
                        style=style.text_style
                    ),
                    rx.text(
                        body,
                        size=Spacing.VERY_SMALL.value,
                        style=style.sub_title_style
                    ),
                    align_items="start",
                    spacing=Spacing.VERY_SMALL.value
                )
            ),
            style={
                "width": "100%",
                "height": "100%",
                "display": "block",
                "box-shadow": f"3px 3px 0px 0px {hover_box}",
                "border": f"2px solid {hover_color}",
                "border-radius": Size.DEFAULT.value,
                "padding": Size.SMALL.value,
                "background_color": Colors.PRIMARY.value,
                "transition": "0.1s",
                "_hover": {
                    "background-color": Colors.SECONDARY.value,
                    "border": "2px solid #175AF4",
                    "box_shadow": "none",
                    "transform": "translate(3px, 3px)"
                }
            }
        ),
        href=url,
        is_external=True,
        width="100%",
    )

