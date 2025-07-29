import os
from typing import Optional, Literal, Callable, List, Union

import streamlit.components.v1 as components

# Toggle this to False when developing locally with npm start
_RELEASE = True

# Declare component - either use local dev server or built frontend
if not _RELEASE:
    _component_func = components.declare_component(
        name="st_smart_text_input",
        url="http://localhost:3001",
    )
else:
    # Use the path to the built frontend directory
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend", "build")
    if not os.path.isdir(build_dir):
        raise FileNotFoundError(
            f"Streamlit component build directory not found: {build_dir}"
        )
    _component_func = components.declare_component(
        name="st_smart_text_input",
        path=build_dir,
    )

def st_smart_text_input(
    label: str,
    options: List[str],
    index: Optional[int] = None,
    format_func: Optional[Callable[[str], str]] = None,
    placeholder: Optional[str] = None,
    disabled: bool = False,
    delay: int = 300,
    key: Optional[str] = None,
    label_visibility: Literal["visible", "hidden", "collapsed"] = "visible",
) -> Union[str, None]:
    """Smart Text Input component for Streamlit."""

    if not isinstance(options, list):
        raise ValueError("`options` must be a list of strings.")

    if format_func is not None:
        options = [format_func(option) for option in options]

    if index is not None:
        if not (0 <= index < len(options)):
            raise ValueError("`index` must be within the range of options.")

    if label_visibility not in ["visible", "hidden", "collapsed"]:
        raise ValueError("`label_visibility` must be 'visible', 'hidden', or 'collapsed'.")

    # Call the frontend component
    component_value = _component_func(
        label=label,
        options=options,
        index=index,
        placeholder=placeholder,
        disabled=disabled,
        delay=delay,
        label_visibility=label_visibility,
        key=key,
    )

    return component_value
