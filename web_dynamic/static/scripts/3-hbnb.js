$(document).ready(() => {
  const dict = {};
  $('input').click(function () {
    if ($(this).is(':checked')) {
      dict[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete dict[$(this).attr('data-id')];
    }
    $('div.amenities > h4').text(Object.values(dict).join(', '));
  });
  const uri = 'http://localhost:5001/api/v1/status/';
  $.get(uri, (request) => {
    const selector = $('#api_status');

    if (request.status === 'OK') {
      selector.css('background-color', '#ff545f');
      selector.addClass('available');
    } else {
      selector.css('background-color', '#cccccc');
      selector.removeClass('available');
    }
  });

  const api = 'http://localhost:5001/api/v1/places_search';

  function fillPlaceArticle (data) {
    for (let i = 0; i < data.length; i++) {
      const place = data[i];

      const template = ['<article>',
        '<div class="title_box">',
        '<h2>' + place.name + '</h2>',
        '<div class="price_by_night">$' + place.price_by_night + '</div>',
        '</div>',
        '<div class="information">',
        '<div class="max_guest">' + place.max_guest + 'Guest(s)</div>',
        '<div class="number_rooms">' + place.number_rooms + 'Bedroom(s)</div>',
        '<div class="number_bathrooms">' + place.number_bathrooms + 'Bathroom(s)</div>',
        '</div>',
        '<div class="user"><b>Owner: </b>' + place.Owner + '</div>',
        '<div class="description">',
        place.description,
        '</div>',
        '</article>'];
      $('section.places').append(template.join(''));
    }
  }

  $.ajax({
    type: 'POST',
    url: api,
    data: JSON.stringify({}),
    contentType: 'application/json',
    success: (data) => fillPlaceArticle(data)
  });
});
