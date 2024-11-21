document.addEventListener('DOMContentLoaded', () => {
  const addItemElement = document.querySelector('#add_item');
  const listElement = document.querySelector('ul.my_list');

  addItemElement.addEventListener('click', () => {
    const newListItem = document.createElement('li');
    newListItem.textContent = 'Item';
    listElement.appendChild(newListItem);
  });
});
