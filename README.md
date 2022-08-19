<div align="center">
    <h1>Portfolio - novusys</h1>
    <i>
        Built with Flask & TailwindCSS
    </i>
</div>
<br>

This is my portfolio which I've built with Matts (@MattLawz) help. It utilises a Python Flask backend and a TailwindCSS
frontend. The site is currently running over at Pythonanywhere, specifically [here](https://novusys.pythonanywhere.com/).


## Installing & running

> Please ensure you have Python 3.10+

In case you want to run a local version of this website, please follow these steps,

```
git clone https://github.com/novusys/portfolio
cd portfolio
py -m pip install requirements.txt -r
npm init
npm run watch
```

For the contact feauture to work, you must create a `.env` file at the root directory containing the following variables,

```
PORTFOLIO_PASSWORD=...
PORTFOLIO_EMAIL=..
```


After that, you can navigate to the Flask localhost (should be localhost:5000/) to see it in action.