document.addEventListener('DOMContentLoaded', () => {
  const listMovies = document.getElementById('list_movies');
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const movies = data.results;
      movies.forEach((movie) => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMovies.appendChild(listItem);
      });
    })
    .catch((error) => {
      console.error('Fetch error:', error);
      listMovies.innerHTML = '<li>Error fetching movie titles.</li>';
    });
});
