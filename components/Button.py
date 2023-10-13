from dash import html

def Button(text:str = None, id:str = None, additional_classes:str = None):
    """
    Creates a reusable button component.

    Parameters
    ----------
    text : str, optional
        Text to display on the button. The default is None, which will display no text.
    id : str, required
        The id of the button. This is required for Dash to be able to recognize
        the button to attach callbacks to it. The default is None, which will raise
        an error.
    additional_classes : str, optional
        Additional CSS classes to add to the button. The default is None, which
        will not add any additional classes. The expectation is that this will be
        used for TailwindCSS utility classes.

    Returns
    -------
    html.Button
        A customized Dash Button component.

    Raises
    ------
    ValueError
        If the id parameter is not provided.
    """
    # Handle id (required)
    if id is None:
        raise ValueError("An id must be provided to the Button component. Please \
provide an id.")

    # Handle additional classes (optional)
    base_classes = "button"
    if additional_classes is not None:
        className = f"{base_classes} {additional_classes}"
    else:
        className = base_classes

    # Handle text (optional)
    if text is None:
        label = ""
    else:
        label = text

    # Return the button
    return html.Button(label, id=id, className=className)