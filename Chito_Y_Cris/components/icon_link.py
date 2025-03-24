import reflex as rx


def icon_link(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width="30px",
            height="30px",
            style={
                "transition": "0.3s",
                "_hover": {
                    "transform": "scale(1.1)",
                    "transition": "0.3s"
                }
            },
        ),
        href=url,
        is_external=True,
    )
