"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...




def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Chokmah", size="9"),
            rx.text(
                "ELITE PERFORMANCE SPORTSWEAR!",
                size="5",
            ),
            rx.link(
                rx.button("Contact us!"),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),

        rx.box(
        rx.vstack(

            rx.image(
                src="/unnamed2.png",
                width="100%",
                height="auto",
            ),
                side="top",
                pb="current",
            ),

            rx.heading(
                "ELITE PERFORMANCE SPORTSWEAR", 
                font_size="3em", 
                color="white", 
                text_align="center"
            ),
            rx.text(
                "Unleash Your Athletic Potential",
                font_size="1.5em",
                color="white",
                margin_top="10px"
            ),
      
            align="center",
            justify="center",
            height="70vh",
            width="100%",
            background_image="url('/images/hero_background.jpg')",
            background_size="cover",
            background_position="center",
            background_color="rgba(0,0,0,0.5)",
            padding="2em",
        ),
    
        rx.card(
            rx.inset(
                rx.heading("Shorts"),
                rx.image(
                    src="/unnamed5.png",
                    width="100%",
                    height="auto",
                ),
                side="top",
                pb="current",
            ),
            rx.text(
                "Unleash Your Athletic Potential"
            ),
            width="25vw",
        )
    )


app = rx.App()
app.add_page(index)