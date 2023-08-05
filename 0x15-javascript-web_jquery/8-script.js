$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        var movies = data.results;
        var html = '';
        for (var i = 0; i < movies.length; i++) {
          html += '<li>' + movies[i].title + '</li>';
        }
        $('#list_movies').html(html);
      },
      error: function(xhr, status, error) {
        $('#list_movies').html('Error fetching movie titles.');
      }
    });
  });
