  var _ = function($) {
        $(function () {
            $('button').click(function() {
                var form = $('form');
                $.post(form.attr('action'), form.serialize(), function(data){
                    $('#message_result').text(data["result"]);
                });
            });
        })
    }(jQuery);
