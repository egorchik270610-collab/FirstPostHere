from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/hello", response_class=HTMLResponse)
def hi():
    return """
    <html>
        <head>
            <title>Site on html</title>
        </head> 
        <style>
        body {text-align: center;}  
        body { background-color: #000080; 
        text-size: 32px;
        color: #00FF7F; }
        </style>
        <body>
            <h1>Hello</h1>
            <p>Its my html code which i wrote on python</p>
        </body>
    </html>
    """

