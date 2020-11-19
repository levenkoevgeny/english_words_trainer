let dictionary_id = $("#dictionary_id").val();

const trainingSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/training/'
    + dictionary_id
    + '/'
);


trainingSocket.onmessage = function(e) {
    data = JSON.parse(e.data);
    console.log(data);
    $('#id_foreign_word').attr('value', data['native']);
    $('#id_native_word_true').attr('value', data['foreign']);
};

trainingSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

$("#check_answer_button").click(function() {
    let right_answer = $('#id_native_word_true').val();
    let typed_answer = $('#id_native_word').val();
    if (right_answer != typed_answer) {
        alert('Неверный ответ!!!!');
        $('#id_native_word').focus();
    } else {
        window.location.href = '/dictionary/' + dictionary_id + '/words/training/';
    }
});

$("#show_answer_button").click(function() {
    $('#id_native_word').attr('value', $('#id_native_word_true').val());
});