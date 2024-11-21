document.addEventListener('DOMContentLoaded', () => {
  const redHeaderElement = document.querySelector('#red_header');
  const headerElement = document.querySelector('header');

  redHeaderElement.addEventListener('click', () => {
    headerElement.classList.add('red');
  });
});
