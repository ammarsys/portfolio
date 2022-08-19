function validateEmail(email) {
    let re = /\S+@\S+\.\S+/;
    return re.test(email);
}

function contactMe() {
    let data = {
        "email": document.getElementById("email").value,
        "content": document.getElementById("message").value,
        "name": document.getElementById("name").value
    };

    if (validateEmail(data["email"])) {
        fetch("http://127.0.0.1:5000/api/contact", {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        })

        Swal.fire({
            title: 'Success!',
            text: 'Your message has been sent.',
            icon: 'success',
            confirmButtonText: 'Yerr',
            confirmButtonColor: 'hsl(204, 14%, 29%)',
        })

    } else {
        Swal.fire({
            title: 'M8 wot tf!',
            text: 'yerr fookin cunt what is man giving me false email like "low it"',
            icon: 'error',
            confirmButtonText: 'bruvit',
            confirmButtonColor: 'hsl(204, 14%, 29%)',
        })
    }
}