from utils.libs import *
from utils.importer import *
import pages.LoginPage as lg
import pages.DaftarNota as dn
import component.Navbar as nv
import pages.admin as ad
import pages.Order as nb

def main(page: Page):
    COLOUR_JSON=load_colors()
    page.title = "Routes Example"
    page.expand = True
    theme=ColorScheme(
        # primary="#FFFFFF",
        # on_primary="#FFFFFF",
        # primary_container="#FFFFFF",
        # on_primary_container="#FFFFFF",
        # on_secondary_container="#FFFFFF",
        # secondary="#FFFFFF",
        # on_secondary="#FFFFFF",
        # secondary_container="#FFFFFF",
        # tertiary="#FFFFFF",
        # tertiary_container="#FFFFFF",
        # on_tertiary="#FFFFFF",
        background=COLOUR_JSON["Gray/50"],
        # on_background="#FFFFFF",
        # surface="#FFFFFF",
        # on_surface="#FFFFFF",
        # surface_variant="#FFFFFF",
        #ngatur warna button
        on_surface_variant=COLOUR_JSON["Primary/500"],
        # outline="#FFFFFF",
        # outline_variant="#FFFFFF",
        # shadow="#FFFFFF",
        # scrim="#FFFFFF",
        # inverse_surface="#FFFFFF",
        # inverse_primary="#FFFFFF",
        #ngatur warna bg overlay
        surface_tint=COLOUR_JSON["White"],
    )
    page.theme=Theme(color_scheme=theme)
    page.theme_mode = ThemeMode.LIGHT
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
        regex=r"(^/)?([^/]*)(/|$)"
        match = re.search(regex, page.route)
        route=match.group(2)
        if route == "DaftarNota":
            DaftarNota=View(
                    "/DaftarNota/:UserId",
                    [
                        page.haeder,
                    ],
                )
            page.views.append(DaftarNota)
            dn.main(DaftarNota,page)
        elif route == "Admin":
            Admin=View(
                    "/Admin",
                    [
                        page.haeder,
                    ],
                )
            page.views.append(Admin)
            ad.admin_page(Admin,page)
        elif route == "NotaBaru":
            NotaBaru=View(
                    "/NotaBaru",
                    [
                        page.haeder,
                    ],
                )
            page.views.append(NotaBaru)
            nb.main(NotaBaru,page)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def window_event_page(e):
        # page.width = OS_WIDTH
        # page.height = OS_HEIGHT
        if e.data in ["resized","unmaximize","maximize"]:
            if page.route in ["/NotaBaru","/DaftarNota","/StokdanProduk","/Analitik","/Admin"]:
                page.haeder.resize_event(page.window_width)
                OS_WIDTH, OS_HEIGHT = get_screen_size()
                
        page.go(page.route)
        page.update()


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.on_window_event=window_event_page

app(target=main, view=AppView.WEB_BROWSER,route_url_strategy="hash")