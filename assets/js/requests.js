function datetime_format(d) {
    var month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    return ('0' + d.getUTCDate()).slice(-2) + '/' +
           month[d.getUTCMonth()] + '/' +
           d.getUTCFullYear() + ' ' +
           ('0' + d.getUTCHours()).slice(-2) + ':' +
           ('0' + d.getUTCMinutes()).slice(-2) + ':' +
           ('0' + d.getUTCSeconds()).slice(-2);
}

function requests(url) {

    var last_date_time = null;
    var new_records = 0;
    var display = $('#display');

    var f = function() {

        $.getJSON(url, function(data) {

            var elems = [];

            $.each(data.reverse(), function (i, item) {

                var date_time = new Date(item.fields.date_time);

                elems.unshift(
                    '<p>' +
                    item.fields.remote_addr + ' - ' +
                    '[' + datetime_format(date_time) + '] ' +
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

}
