window.onload = () => {
  const helloDiv = document.getElementById('hello');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      helloDiv.textContent = data.hello;
    })
    .catch((error) => {
      console.error('Fetch error:', error);
      helloDiv.textContent = 'Error fetching greeting.';
    });
};
