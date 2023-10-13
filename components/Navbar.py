from dash import html

# Import navbar buttons from ../data/navbar_buttons.py
from data.navbar_buttons import navbar_buttons

def Navbar():
    bar = []
    for i, (k, v) in enumerate(navbar_buttons().items()):
        bar.append(html.A(k,
                          href=v['href'],
                          className=f"{v['className']} button"))
        if i != len(navbar_buttons()) - 1:
            bar.append(html.Div(className='divider', children=[" "]))

    return html.Nav(id='navbar',
                    children=[
                        html.Div(
                            className="navbar-logo",
                            children=[
                                html.A(children=["CinSights"],
                                       href="/"),
                            ])] + bar)