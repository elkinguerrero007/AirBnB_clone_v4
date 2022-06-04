const dict = {};
$(document).ready(() => {
    $('input').click(function(){
        if ($(this).is(':checked')){
            dict[$(this).attr('data-id')] = $(this).attr('data-name');
        } else {
            delete dict[$(this).attr('data-id')];
        }
        $("div.amenities > h4").text(Object.values(dict).join(', '))
    });

    const uri = "http://localhost:5001/api/v1/status/"


    $.get(uri, (request) =>
{
    const selector = $('#api_status')

    if (request.status === "OK") {
        selector.css("background-color", "#ff545f");
        selector.addClass("available");
    } else {
        selector.css("background-color", "#cccccc");
        selector.removeClass("available");
    }
});
});
