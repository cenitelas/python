$(document).ready(()=>{
    $('#search_form').submit((e)=>{
        e.preventDefault()
        e.stopImmediatePropagation();
        $.post('/search',$('#search_form').serialize(),function (data) {
            $("#modal .content").html(data);
            $("#modal").css("display",'flex');
        })
    })

    $("#modal").click((e)=>{
        if(e.target.id=='modal'){
            $('#modal').hide();
            clearInterval(window.chat_timer);
        }
    })

    $("#modal .close").click((e)=>{
            $('#modal').hide();
            clearInterval(window.chat_timer);
    })

    $('#change_profile').click(()=>{
        $.get('/change_profile', function (data) {
            $("#modal .content").html(data);
            $("#modal").css("display",'flex');
        })
    })

    $('.messages_link').click((e)=>{
        e.preventDefault()
        $.get('/chats', function (data) {
            $("#modal .content").html(data);
            $("#modal").css("display",'flex');
        })
    })


    $('#message_form').submit((e)=>{
        e.preventDefault()
        e.stopImmediatePropagation();
        $.post('/send_message',$('#message_form').serialize(),function (data) {
            $('#message_form input[name="message"]').val('')
        })
    })

    $('#message_send').click((e)=>{
        get_message($('#message_send').data('user'))
    })
})

function get_message(id) {
    clearInterval(window.chat_timer);
    $("#modal").css("display", 'flex');
    $.get(`/chat/${id}`, function (data) {
            $("#modal .content").html(data);
    })
    window.chat_timer = setInterval(()=>{
        $.get(`/messages/${id}`, function (data) {
            $("#chat").html(data);
            $("#chat .messages").scrollTop($("#chat .messages")[0].scrollHeight);
        })
    },1000)
}