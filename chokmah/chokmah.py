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
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),

rx.card(
    rx.inset(
         rx.heading("Rash guards"),
        rx.image(
            src="/unnamed2.png",
            width="100%",
            height="auto",
        ),
        side="top",
        pb="current",
    ),
    rx.text(
        "Reflex is a web framework that allows developers to build their app in pure Python."
    ),
    width="25vw",
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
        "Reflex is a web framework that allows developers to build their app in pure Python."
    ),
    width="25vw",
)

    ),

    
    as_child=True,


app = rx.App()
app.add_page(index)
