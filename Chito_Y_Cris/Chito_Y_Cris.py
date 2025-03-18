import reflex as rx
from Chito_Y_Cris.views.navbar import navbar
from Chito_Y_Cris.views.header import header
from Chito_Y_Cris.views.links import links
from Chito_Y_Cris.views.footer import footer
from Chito_Y_Cris.styles.styles import Size, MAX_WIDTH, BASE_STYLE
import Chito_Y_Cris.styles.styles as style



def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                rx.divider(),
                links(),
                rx.divider(),
                footer(),
                max_width=style.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                spacing="6"
            ),
        ),
    )


app = rx.App(
    style=BASE_STYLE,
    stylesheets=style.STYLESHEETS
)
app.add_page(
    index,
    image="/logo.jpg",
    description="La web de Chito y Cris remasterizada y mejor optimizada, con un diseño más limpio y moderno.",
    title="Chito y Cris",
    
    )
