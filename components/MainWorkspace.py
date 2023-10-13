from dash import html

# Import page components
from pages import data_page, \
                    univariate_page, \
                    feature_engineering_page, \
                    feature_importance_page, \
                    feature_selection_page, \
                    model_page, \
                    testing_page


def MainWorkspace():
    return html.Div(
        className="""
            
            """, 
        id='main-workspace',
        children=[
            data_page.DataPage(),
            univariate_page.UnivariatePage(),
            feature_engineering_page.FeatureEngineeringPage(),
            feature_importance_page.FeatureImportancePage(),
            feature_selection_page.FeatureSelectionPage(),
            model_page.ModelPage(),
            testing_page.TestingPage()
        ])