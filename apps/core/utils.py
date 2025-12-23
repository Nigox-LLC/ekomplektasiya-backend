def environment_callback(request):
    """
    Callback to return the environment label for Unfold Admin.
    """
    return ["Production", "success"] # Label, Color (primary, success, danger, warning, info)
