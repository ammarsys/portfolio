/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.{html,js}"],
    theme: {
        screens: {
            sm: '480px',
            md: '768px',
            lg: '976px',
            xl: '1440px',
        },
        letterSpacing: {
            '1': '0.2em',
        },
        extend: {
            colors: {
                regBlue: "hsl(204, 14%, 29%)",
                regBlueHover: "hsl(204, 15%, 24%)",
                lightBlue: "hsl(212, 61%, 77%)",
                backgroundBlue: "hsl(228, 27%, 11%)",
                buttonText: "hsl(191, 10%, 79%)",
                textdecBlue: "hsl(198, 89%, 28%)",
            },
        },
        plugins: [],
    }
};
