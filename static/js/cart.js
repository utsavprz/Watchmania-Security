
$('.cartinput-number-increment').click(function() {
    var $input = $(this).parents('.cartinput-number-group').find('.cartinput-number');
    var val = parseInt($input.val(), 10);
    $input.val(val + 1);

    });

    $('.cartinput-number-decrement').click(function() {
    var $input = $(this).parents('.cartinput-number-group').find('.cartinput-number');
    var val = parseInt($input.val(), 10);
    if (val >0){
        $input.val(val - 1);

    }
    })

let updateBtns = document.getElementsByClassName('update-cart')
for(let i=0; i < updateBtns.length; i++){

    updateBtns[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        let qty = this.dataset.qty

        
 
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
                if (qty == null){
                    qty="false"
                    updateUserOrder(productId, action,qty)
                }
                else{
                    qty= $('#qtyinputGet').val()
                    updateUserOrder(productId, action,qty)
                }
        }
        // console.log('DataToSend:', productId)
        // console.log('DataToSend:', action)
        // console.log('DataToSend:', qty)
    })

}

function updateUserOrder(productId,action,qty){
    // console.log('User Logged in,','Sending data...')
    // console.log('productId:', productId , 'action:', action,'qty:', qty)
    let url = '/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' :  csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action, 'qty':qty})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })

}



    function validateForCheckout(){

        let price = document.getElementById("totalOrderPrice").innerText;

        if (price == "रु0"){
            if ($('#msgChk').hasClass('hide')){
                $('#msgChk').removeClass('hide')
                // setInterval(() => {
                //     $('#msgChk').addClass('hide')
                // }, 7000);
             }
        }
        else{
            location.href="/checkout/"
        }
    }