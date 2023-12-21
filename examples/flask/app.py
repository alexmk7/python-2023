from flask import Flask, Response

app = Flask(__name__)
 
@app.route("/test")
def home():
    # html = """<html>
    #             <title>Hello from Docker</title>
    #             <body>
    #                 <h3>Hello from Docker</h3>
    #             </body>
    #          </html>    
    # """
    # return Response(html, mimetype='text/html')
    
    return "Hello from Flask!"
 
app.run('0.0.0.0', port=8989, debug=True)
