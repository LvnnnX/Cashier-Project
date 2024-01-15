from utils.libs import *
from utils.importer import *
import pages.LoginPage as lg
import component.Navbar as nv

def main(page: Page):
    page.title = "Routes Example"
    def route_change(route): 
        page.views.clear()
        page.haeder=nv.Navbar(page.window_width,page)  
        page.views.append(
            View(
                "/",
                [
                    page.haeder
                ],
            )
        )
        if page.route == "/DaftarNota":
            page.views.append(
                View(
                    "/DaftarNota",
                    [
                        page.haeder
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def window_event_page(e):
        if e.data=="resized":
            if page.route in ["/NotaBaru","/DaftarNota","/StokdanProduk","/Analitik","/Admin"]:
                page.haeder.controls[0].resize_event(page.window_width)
            page.update()


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.on_window_event=window_event_page

app(target=main, view=AppView.WEB_BROWSER)