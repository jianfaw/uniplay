/* Javascript for UniPlayerXBlock. */
function uniPlayInitEdit(runtime, element) {
    var handlerUrl = runtime.handlerUrl(element, 'save_video');

    // Create IE + others compatible event handler
    var eventMethod = window.addEventListener ? "addEventListener" : "attachEvent";
    var eventer = window[eventMethod];
    var messageEvent = eventMethod == "attachEvent" ? "onmessage" : "message";
    // Listen to message from child window
    eventer(messageEvent, function (e) {
        var msg = e.data;
        if (msg != null) {
            $("#play_id").val(e.data.id);
            $("#play_url").val(e.data.url);
        } else {
            $("#play_id").val("");
            $("#play_url").val("");
        }
    }, false);

    $(element).find('.action-cancel').bind('click', function () {
        page_return_scroll();
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function () {
        page_return_scroll();
        var data = {
            'display_name': $('#display_name').val(),
            'play_id': $('#play_id').val(),
            'play_url': $('#play_url').val()
        };

        runtime.notify('save', {state: 'start'});

        $.post(handlerUrl, JSON.stringify(data)).done(function (response) {
            if (response.result === 'success') {
                runtime.notify('save', {state: 'end'});
            } else {
                runtime.notify('error', {msg: response.message})
            }
        });
    });
}

function page_return_scroll() {
    document.documentElement.style.overflow = '';
}
