function validate(){
    var first_name = document.forms["Form"]["first_name"].value;
    var last_name = document.forms["Form"]["last_name"].value;
    var phone = document.forms["Form"]["phone"].value;
    var email = document.forms["Form"]["email"].value;
    var city = document.forms["Form"]["city"].value;
    var address = document.forms["Form"]["address"].value;
    var street = document.forms["Form"]["street"].value;
    var postalcode = document.forms["Form"]["postalcode"].value;
    var description = document.forms["Form"]["description"].value;

    if (first_name == "" || last_name == "" || phone == "" || email == "" || city == "" || address == "" || street == "" || postalcode == "" || description == "") {
        console.log("false")
        document.getElementById('msgChk').classList.remove('d-none')
    }
    else{
        console.log("true")
        document.getElementById('payment-buttonKhalti').classList.add('d-none')
        document.getElementById('payment-box').classList.remove('d-none')   
}
}


function getPmValue(){
    let paymentMethod = document.getElementById('pm')
    switch(paymentMethod.value) {
        case "Khalti":
            document.getElementById('payment-buttonCOD').classList.add('d-none')
            document.getElementById('payment-buttonKhalti').classList.remove('d-none')

            
            
            break;
            case "Cash on Delivery":
                document.getElementById('payment-buttonCOD').classList.remove('d-none')
                document.getElementById('payment-buttonKhalti').classList.add('d-none')
                document.getElementById('payment-box').classList.add('d-none')   
                break;
                }
        }


