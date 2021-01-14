// for the ajax form functionality
$(document).ready(function(){
    $("#sendMessageButton").click(function(){
        
        // form validate script
        handleFormSubmit();

        var serializedData = $("#createInfoForm").serialize();

        const url = $("#createInfoForm").data("url");
        
        $.ajax({
            url: url,
            data: serializedData,
            type: "post",
            dataType: "json",
            success: function(response){
                let container = $('#contact');

                let myInfo = '<br/><div class="text-center"><h2 class="text-capitalize btn btn-info">' + response.contact.name + ': Message sent<span>&#10003;</span></h2></div>'
                container.append(myInfo);

            },
            error: function(response){
                console.log("error", response)
            }
        });
        $("#createInfoForm")[0].reset();
    })
})


// for form validation js
function handleFormSubmit(){
    let form = document.getElementsByTagName('form').value;
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phone').value;
    let message = document.getElementById('message').value;
    if (form == ""){
        alert("Please fill in the form below!")
        document.getElementsByTagName('form').style.borderColor = 'red';
        return false;
    }else if (name == ""){
        alert("Please fill in your name!")
        document.getElementById('name').style.borderColor = 'red';
        return false;
    }else if (email == ""){
        alert("Please fill in your email!")
        document.getElementById('email').style.borderColor = 'red';
        return false;
    }else if (phone == ""){
        alert("Please fill in your phone number!")
        document.getElementById('phone').style.borderColor = 'red';
        return false;
    }else if (message == ""){
        alert("Message can not be empty!")
        document.getElementById('message').style.borderColor = 'red';
        return false;
    }else{
        return true
    }
}
