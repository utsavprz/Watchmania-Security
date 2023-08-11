$('.qty-input i').click(function() {
    val = parseInt($('.qty-input input').val());

    if ($(this).hasClass('less')) {
            val = val - 1;
    } else if ($(this).hasClass('more')) {
            val = val + 1;
    }

    if (val < 1) {
            val = 1;
    }

    $('.qty-input input').val(val);
})