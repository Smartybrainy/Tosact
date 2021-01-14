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
