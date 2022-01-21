let updateBtns = document.getElementsByClassName('update-cart')

for(let i=0; i < updateBtns.length; i++){

    updateBtns[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        // console.log('productId:', productId , 'action', action)


        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })

}

function updateUserOrder(productId,action){
    console.log('User Logged in,','Sending data...')

    let url = '/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' :  csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()

    })

}

$('.cartinput-number-increment').click(function() {
    var $input = $(this).parents('.cartinput-number-group').find('.cartinput-number');
    var val = parseInt($input.val(), 10);
    $input.val(val + 1);
    });

    $('.cartinput-number-decrement').click(function() {
    var $input = $(this).parents('.cartinput-number-group').find('.cartinput-number');
    var val = parseInt($input.val(), 10);
    $input.val(val - 1);
    })
