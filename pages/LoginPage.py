import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import load_colors


def login_page(page: Page):
    page.title = "Login Page"
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = False
    page.window_title_bar_buttons_hidden = True
    # page.theme = colors['White']
    colors = load_colors()

    login = Container(
        width=380,
        height=600,
        # border_radius=10,
        bgcolor=colors["White"],
        content=Column(
            width=380,
            controls=[
                # Container(
                #     width=360,
                #     margin=margin.only(left=200, right=10, top=10),
                #     content=TextButton(
                #         'Register',
                #         style=ButtonStyle(
                #             color=colors['B_Bg'],
                #         )
                #     )
                # ),
                Container(
                    width=360,
                    margin=margin.only(left=50, right=10, top=150),
                    content=Text(
                        "Login", size=30, color=colors["Black"], weight="bold"
                    ),
                ),
                Container(
                    width=360,
                    margin=margin.only(left=50, right=10, top=-10),
                    content=Text(
                        "Login untuk menggunakan aplikasi",
                        size=12,
                        color=colors["blackAlpha/500"],
                        weight="bold",
                    ),
                ),
                Container(
                    width=360,
                    margin=margin.only(left=50, right=50, top=10),
                    content=TextField(
                        label="Username",
                        border_color=colors["Primary/500"],
                        text_style=TextStyle(color=colors["Primary/500"]),
                    ),
                ),
                Container(
                    width=360,
                    margin=margin.only(left=50, right=50, top=10),
                    content=TextField(
                        label="Password",
                        border_color=colors["Primary/500"],
                        password=True,
                        can_reveal_password=True,
                        text_style=TextStyle(color=colors["Primary/500"]),
                    ),
                ),
                Container(
                    width=360,
                    margin=margin.only(left=50, right=50, top=10),
                    content=ElevatedButton(
                        "Login",
                        style=ButtonStyle(
                            color=colors["White"],
                            bgcolor=colors["Primary/500"],
                            shape={
                                MaterialState.FOCUSED: RoundedRectangleBorder(radius=2),
                                MaterialState.HOVERED: RoundedRectangleBorder(radius=2),
                            },
                            padding=20,
                        ),
                    ),
                ),
            ],
        ),
    )

    foto = Container(
        width=380,
        height=600,
        bgcolor=colors["Gray/50"],
        # border_radius=10,
        content=Stack(
            [
                Image(
                    src=IMGPATH / "kopi_bg.png",
                )
            ]
        ),
    )

    body = Container(
        width=800,
        height=600,
        bgcolor=colors["White"],
        content=Row(
            controls=[
                foto,
                login,
            ]
        ),
    )

    page.add(body)

if __name__ == "__main__":
    app(target=login_page)
