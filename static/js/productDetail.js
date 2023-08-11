$('.input-number-increment').click(function() {
    var $input = $(this).parents('.input-number-group').find('#qtyinputGet');
    var val = parseInt($input.val(), 10);
           $input.val(val + 1);
    });

    $('.input-number-decrement').click(function() {
    var $input = $(this).parents('.input-number-group').find('#qtyinputGet');
    var val = parseInt($input.val(), 10);
    if (val >0){
        $input.val(val - 1);
    }

    })

    