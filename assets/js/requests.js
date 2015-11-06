$(document).ready(function() {

    var last_date_time = null;
    var new_records = 0;
    var display = $('#display');

    var f = function() {

        $.getJSON('/hello/requests/', function(data) {

            var elems = [];

            $.each(data.reverse(), function (i, item) {

                var date_time = new Date(item.fields.date_time);

                elems.unshift(
                    '<p>' + 
                    item.fields.remote_addr + ' - ' +
                    '[' + item.fields.date_time + '] ' +
                    '"' + item.fields.request + '" ' +
                    item.fields.status_code +
                    '</p>');

                if (date_time > last_date_time) {
                    last_date_time = date_time;
                    new_records++;
                }

            });

            display.empty();
            display.append(elems);
            document.title = '(' + new_records + ') new records';

            if (!document.hidden) {
                new_records = 0;
            }

        });
    }
    
    f()
    setInterval(f, 2000);

});
