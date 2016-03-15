/* Javascript for UniPlayerXBlock. */
function uniPlayInitEdit(runtime, element) {
    var handlerUrl = runtime.handlerUrl(element, 'save_video');

    $(element).find('.action-cancel').bind('click', function () {
        page_return_scroll();
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function () {
        page_return_scroll();
        var data = {
            'display_name': $('#display_name').val(),
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
