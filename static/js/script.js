$(document).ready(function(){

    $('#apply').on('click', function(){

        $coupon = $('#coupon').val();
        // $lastname = $('#lastname').val();

        if($coupon == ""){
            alert("No coupon added")
        }else{
            // alert("The coupon added succesfully");
            $.ajax({
                url: 'coupon_apply/',
                type: 'POST',
                data: {
                    coupon: $coupon,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken').val()
                },
                // success: function(){
                //     Read();
                //     $('#coupon').val('');
                //     alert("The coupon added succesfully");
                // }
            });
        }

    });

});