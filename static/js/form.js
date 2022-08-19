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
    console.log(Object.values(data).includes(''));

    if (Object.values(data).includes('')) {
        Swal.fire({
            text: 'Looks like one of the fields is empty, please fill them in.',
            background: "#3a435e",
            color: "#fff"
        })
    } else {
        if (validateEmail(data["email"])) {
            fetch("/api/contact", {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            }).then(_ =>
                Swal.fire({
                    text: 'Successfully sent your message.',
                    icon: "success",
                    background: "#3a435e",
                    color: "#fff"
                })
            )


        } else {
            Swal.fire({
                title: 'Bad Information',
                text: "Looks like your email doesn't seem right, could you double check it?",
                icon: 'error',
                background: "#3a435e",
                color: "#fff"
            })
        }
    }
}