from flask import Flask, request, make_response, render_template
import pandas as pd
 
app = Flask(__name__,template_folder='templates')





@app.route("/", methods =['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')


        if username == 'neuraline' and password == 'password':
            return "Success"
        else:
            return 'Failure'

    
@app.route("/file_upload", methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
















# @app.route("/hello")
# def hello ():
#     response = make_response('Hello World\n')
#     response.status_code = 202
#     response.headers['content-type'] = 'application/octet-stream'
#     return response


# @app.route("/greet/<name>")
# def greet(name):
#     return f"hello {name}"

# @app.route("/add/<int:number1>/<int:number2>")
# def add(number1,number2):
#     return f"result is {number1+number2}"

# @app.route("/handle_url_params")
# def handle_params():
#     if 'greeting' in request.args.keys() and 'name' in request.args.keys():

#         greeting = request.args['greeting']
#         name = request.args.get('name')
#         return f"{greeting}, {name}"
#     else:
#         return "one params are missing"
   


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)