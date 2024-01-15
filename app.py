from utils.libs import *
from utils.importer import *
import pages.LoginPage as lg

def main(page: Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [],
            )
        )
        lg.login_page(page.views[0])
        if page.route == "/store":
            page.views.append(
                View(
                    "/store",
                    [
                        AppBar(title=Text("Store"), bgcolor=colors.SURFACE_VARIANT),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

app(target=main, view=AppView.WEB_BROWSER)