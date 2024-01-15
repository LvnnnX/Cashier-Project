from utils.libs import *
from utils.importer import *
import pages.LoginPage as lg
import pages.DaftarNota as dn
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
            DaftarNota=View(
                    "/DaftarNota",
                    [
                        page.haeder,
                    ],
                )
            page.views.append(DaftarNota)
            dn.main(DaftarNota,page)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def window_event_page(e):
        if e.data in ["resized","unmaximize","maximize"]:
            if page.route in ["/NotaBaru","/DaftarNota","/StokdanProduk","/Analitik","/Admin"]:
                page.haeder.resize_event(page.window_width)
                page.update()


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.on_window_event=window_event_page

app(target=main, view=AppView.WEB_BROWSER)