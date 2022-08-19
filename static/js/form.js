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
        fetch("/api/contact", {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        }).then(_ =>
            Swal.fire({
                text: 'Successfully sent your message.',
            })
        )


    } else {
        Swal.fire({
            title: 'Bad Information',
            text: "Looks like your email doesn't seem right, could you double check it?",
            icon: 'error',
        })
    }
}