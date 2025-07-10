import streamlit as st
from streamlit_sortables import sort_items

st.title('Sortables')

st.write('Sort items in a single container.')
items = [
  { 'item': 'item1', 'color': 'blue' },
  { 'item': 'item2', 'color': 'red' },
  { 'item': 'item3', 'color': 'black' },
  { 'item': 'item4' },
  { 'item': 'item5' },
  { 'item': 'item6' }
]
sorted_items = sort_items(items)
st.write(sorted_items)


st.write('----')
st.write('Sort items in multiple containers.')
items = \
[
  { 'item': 'item1', 'header': 'container1', 'color': 'blue' },
  { 'item': 'item2', 'header': 'container1', 'color': 'red' },
  { 'item': 'item3', 'header': 'container1', 'color': 'black' },
  { 'item': 'item4', 'header': 'container2' },
  { 'item': 'item5', 'header': 'container2' },
  { 'item': 'item6', 'header': 'container2' }
]
sorted_items = sort_items(items, colors=[{'Red': 'red'}])
st.write(sorted_items)

st.write('----')
st.write('Lots of items in a single container.')

sorted_items = sort_items(items, direction='vertical')
st.write(sorted_items)

st.write('----')
st.write('Custom style.')
original_items = [
  { 'item': 'item1', 'header': 'container1', 'color': 'blue' },
  { 'item': 'item2', 'header': 'container1', 'color': 'red' },
  { 'item': 'item3', 'header': 'container1', 'color': 'black' },
  { 'item': 'item4', 'header': 'container2' },
  { 'item': 'item5', 'header': 'container2' },
  { 'item': 'item6', 'header': 'container2' }
]

custom_style = """
.sortable-component {
    border: 3px solid #6495ED;
    border-radius: 10px;
    padding: 5px;
}
.sortable-container {
    background-color: #F0F0F0;
    counter-reset: item;
}
.sortable-container-header {
    background-color: #FFBFDF;
    padding-left: 1rem;
}
.sortable-container-body {
    background-color: #F0F0F0;
}
.sortable-item, .sortable-item:hover {
    background-color: #6495ED;
    font-color: #FFFFFF;
    font-weight: bold;
}
.sortable-item::before {
    content: counter(item) ". ";
    counter-increment: item;
}
"""
sorted_items = sort_items(original_items, custom_style=custom_style)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')
