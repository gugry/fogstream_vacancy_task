  $(document).ready(
      function(){
        $("#clickme").click(function () {
          $.post('/message_for_admin/', $("#message_form").serialize(), function(data){
            $('#message_result').text(data["result"]);
                    });
        alert('/message_for_admin/', $("#message_form").serialize(), function(data){
            $('#message_result').text(data["result"]);
                    })
  });});
