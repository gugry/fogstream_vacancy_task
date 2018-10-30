$(document).ready(function(){
    $("button").click(function () {
      var form = $('#login_form').closest("form");
      $.ajax({
        url: 'username_login/',
        data: form.serialize(),
        dataType: 'json',
        success: function (data) {
          if (data.is_correct) {
            $('#main_block').html(
                'Успешно'+
                '<br/><a href ="/">Отправить сообщение администратору</a>'
          );
          } else {
            $('#error_message').text('Неверное сочитание логина и пароля!');
          }
        }
      });
    });});