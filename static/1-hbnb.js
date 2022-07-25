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
});
