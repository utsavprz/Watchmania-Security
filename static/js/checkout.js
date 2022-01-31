function KhaltiAPI(){
        var config = {
            // replace the publicKey with yours
            "publicKey": "test_public_key_dc74e0fd57cb46cd93832aee0a390234",
            "productIdentity": "1234567890",
            "productName": "Dragon",
            "productUrl": "http://gameofthrones.wikia.com/wiki/Dragons",
            "paymentPreference": [
            "KHALTI",
            "EBANKING",
            "MOBILE_BANKING",
            "CONNECT_IPS",
            "SCT",
            ],
            "eventHandler": {
                onSuccess (payload) {
            // hit merchant api for initiating verfication
                console.log(payload);
            },
            onError (error) {
                console.log(error);
            },
            onClose () {
                console.log('widget is closing');
            }
            }
            };
        
            var checkout = new KhaltiCheckout(config);
            var btn = document.getElementById("payment-button");
            // minimum transaction amount must be 10, i.e 1000 in paisa.
                checkout.show({amount: 1000});

}


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


