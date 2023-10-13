from dash import html
from components.Button import Button
from data.sidebar_buttons import sidebar_buttons

def Sidebar(current_page='landing-page'):
    return html.Div(
        className="""
            bg-cic-primary  
            text-[var(--neutral-color)] 
            z-9 p-10 
            flex flex-row absolute top-0 left-0 
            h-[100vh] w-[20rem] 
            border-black border-[1px] 
        """,
        id='sidebar',
        children=[
            html.H2(sidebar_buttons()[current_page]['title']),
            html.Ul(
                className='''
                    flex flex-col border-blue border-[1px] p-2
                ''',
                children=[
                    Button(k, id=v) for k, v in sidebar_buttons()[current_page]['buttons'].items()
            ])
        ])