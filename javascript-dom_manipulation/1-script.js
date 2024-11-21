document.addEventListener('DOMContentLoaded', () => {
  const redHeaderElement = document.querySelector('#red_header');
  const headerElement = document.querySelector('header');

  redHeaderElement.addEventListener('click', () => {
    headerElement.style.color = '#FF0000';
  });
});
