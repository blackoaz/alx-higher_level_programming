$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        var characterName = data.name;

        $('#character').text(characterName);
      },
      error: function(xhr, status, error) {
        $('#character').text('Error fetching character name.');
      }
    });
  });
