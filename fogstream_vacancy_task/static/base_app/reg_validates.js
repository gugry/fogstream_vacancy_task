// $("#id_username").change(function () {
//       var form = $(this).closest("form");
//       $.ajax({
//         url: 'reg_username_validate/',
//         data: form.serialize(),
//         dataType: 'json',
//         success: function (data) {
//           if (data.is_taken) {
//             $('#error_message').text(data.error_message);
//           }
//           else if (data.is_free) {
//             $('#error_message').text('');
//           }
//         }
//       });
//
//     });
//
//
// $("#id_password2").change(function () {
//     if ($('#id_password1').val() != $('#id_password2').val()) {
//         $('#error_message').text('пароли не совпадают');
//     }
// });
//
//
