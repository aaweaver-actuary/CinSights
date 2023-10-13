# Import required libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Import layout components
from components import Navbar, Sidebar, MainWorkspace

# Initialize the app
app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                title='CinSights from Small Business Analytics',
                update_title='Loading...',
                external_stylesheets=["https://cdn.jsdelivr.net/npm/tailwindcss@latest/dist/tailwind.min.css", 
                                      "assets/style.css"],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])


# Define the layout
app.layout = html.Div(
    className="""
        bg-linear-gradient-to-r
        from-[var(--cic-color)]
        to-[var(--neutral-color)]
        flex flex-col
        h-full w-full
    """,
    id='app-container',
    children=[
    # This component will read and write the URL
    dcc.Location(id='url', refresh=False),

    # Top level: navbar and main-container
    # Navbar - contains the logo and the navigation buttons
    Navbar.Navbar(),
    
    # Main Container - contains the sidebar and the main workspace
    html.Div(
        className="""
            flex flex-row
            """,
        id='main-container',
        children=[
            Sidebar.Sidebar(),
            MainWorkspace.MainWorkspace()
        ])
    ])

# Define callbacks:

# Update the sidebar based on the current page
@app.callback(
    Output('sidebar', 'children'),
    [Input('url', 'pathname')]
)
def update_sidebar(pathname):
    # Extract the last part of the URL as current_page
    if pathname == '/':
        current_page = 'landing-page'
    else:
        current_page = pathname.split('/')[-1] if pathname else 'landing-page'
    
    # Update the sidebar based on the current page
    return Sidebar.Sidebar(current_page)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
