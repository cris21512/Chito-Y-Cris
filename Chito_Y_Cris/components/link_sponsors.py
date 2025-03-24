import reflex as rx
from Chito_Y_Cris.styles.styles import Size

def link_sponsor(image:str, url:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            height="auto",
            aspect_ratio="5 / 2",
            alt=alt
        ),
        href=url,
        is_external=True
    )
