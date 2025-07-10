import os
from typing import Any, Dict, Optional, TypeVar

import streamlit.components.v1 as components

T = TypeVar("T", str, Dict[str,Any])


parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
_component_func = components.declare_component("sortable_items", path=build_dir)

def sort_items(items: list[T],  header: Optional[str]=None, multi_containers: bool=False, direction: str="horizontal", custom_style: Optional[str]=None, key: Any=None) -> list[T]:
    """Create a new instance of "sortable_items".

    Parameters
    ----------
    items : list[str] or dict[str, list[str]]
    header: str or None
    multi_containers: bool
    direction: str
    custom_style: str or None
        Custom CSS styles to apply to the component. Defaults to None.
        The following selectors can be used:
        - '.sortable-component' for the main container
        - '.sortable-component.vertical' if direction is 'vertical'
        - '.sortable-container' for each container if multi_containers is True
        - '.sortable-container-header' for the header
        - '.sortable-container-boy' for the body
        - '.sortable-item' for each item
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    list[T]
        Sorted version of items. Preserves types of input items.
    """
    if not multi_containers:
        if not isinstance(header, str) and header is not None:
            raise ValueError('header argument must be str or None if multi_containers is False.')
        if not all(map(lambda item: isinstance(item, str), items)):
            raise ValueError('items must be list[str] if multi_containers is False.')

        items = [{'item': item, 'header': header} for item in items]
        default_items = items
    else:
        if not all(map(lambda item: isinstance(item, dict), items)):
            raise ValueError('items must be list[dict[str, Any]] if multi_containers is True.')
        default_items = items

    component_value = _component_func(items=items, direction=direction, customStyle=custom_style, default=default_items, key=key)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    if multi_containers:
        return component_value
    else:
        return component_value

