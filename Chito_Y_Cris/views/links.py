import reflex as rx
from Chito_Y_Cris.components.heading import heading
from Chito_Y_Cris.components.link_button import link_button
import Chito_Y_Cris.constants.conts as const
import Chito_Y_Cris.styles.styles as style

def links() -> rx.Component:
    return rx.vstack(
        heading("Comunidades"),
        link_button(
            "WhatsApp", 
            "Unete a nuestro canal de WhatsApp",
            "icons/whastapp.svg",
            const.CDW,
            "#76ee94"
        ),
        link_button(
            "YouTube", 
            "Nuestro canal principal de YouTube",
            "icons/youtube.svg",
            const.YOUTUBE,
            "#FF0000"
        ),
        link_button(
            "Twitch", 
            "Directos de todo tipo!",
            "icons/twitch.svg",
            const.TWITCH,
            "#9F8CE8"
        ),
        link_button(
            "TikTok", 
            "Directos todos los dias!",
            "icons/tiktok.svg",
            const.TIKTOK,
            "#020202"
        ),
        heading("Recetas"),
        rx.text("""A continuación, te presentamos una lista de nuestras recetas dividas
                por sus respectivas categorias. ¡Hechales un vistazo!""", style=style.text_style),
        heading("Res"),
        link_button(
            "Carne asada",
            "Asado a nuestro estilo",
            "icons/meat.png",
            const.ASADO,
            "#020202"
        ),
        link_button(
            "Tacos de Birria",
            "Especial 20k de seguidores!",
            "icons/meat.png",
            const.BIRRIA,
            "#020202"
        ),
        link_button(
            "Hamburguesas",
            "Hamburguesas repletas de sabor",
            "icons/meat.png",
            const.BURGUERS,
            "#020202"
        ),
        heading("Pollo"),
        link_button(
            "Pepian",
            "Un platillo guatemalteco muy sabroso",
            "icons/chicken.png",
            const.PEPIAN,
            "#020202"
        ),
        link_button(
            "Arroz chino",
            "El arroz chino mas delicioso que probaras",
            "icons/chicken.png",
            const.ARROZCHINO,
            "#020202"
        ),
        link_button(
            "Chaomin",
            "Nuestra forma sencilla de preparar chaomin",
            "icons/chicken.png",
            const.CHAOMEIN,
            "#020202"
        ),
        heading("Cerdo"),
        link_button(
            "Carnitas",
            "Carnitas a nuestro estilo!",
            "icons/pig.png",
            const.CARNITAS,
            "#020202"
        ),
        link_button(
            "Pupusas",
            "De todo tipo! Chicharron o queso?",
            "icons/pig.png",
            const.PUPUSAS,
            "#020202"
        ),
        link_button(
            "Chicharron colorado",
            "Un estilo parecido al frijol colorado",
            "icons/pig.png",
            const.CHICHACOLORAO,
            "#020202"
        ),
        heading("Mariscos"),
        link_button(
            "Ceviche",
            "Ceviche Guatemalteco muy delicioso!",
            "icons/camaron.png",
            const.CEVICHE,
            "#020202"
        ),
        link_button(
            "Aguachile",
            "Seraz capaz de aguantar el picante?",
            "icons/camaron.png",
            const.AGUACHILE,
            "#020202"
        ),
        link_button(
            "Mojarras",
            "Una mojarra frita nunca queda mal!",
            "icons/camaron.png",
            const.MOJARRA,
            "#020202"
        ),
        heading("No encuentras lo que buscas?"),
        rx.text("Hechale un vistazo a nuestro tiktok para encontrar mas recetas!", style=style.text_style),
        link_button(
            "TikTok",
            "Encuentra todos nuestros videos aqui!",
            "icons/tiktok.svg",
            const.TIKTOK,
            "#020202"
        ),
        width="100%",    
        spacing="4"
    )

