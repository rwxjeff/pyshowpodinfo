from flask import Flask
import os

NODE_NAME = os.environ.get('MY_NODE_NAME')
POD_NAME = os.environ.get('MY_POD_NAME')
POD_NAMESPACE = os.environ.get('MY_POD_NAMESPACE')
POD_IP = os.environ.get('MY_POD_IP')

app = Flask(__name__)

@app.route('/')
def home():
	#return "Hello World!"
 	return ([{"Node_Name":NODE_NAME}, {"Pod_Name":POD_NAME}, {"Pod_IP":POD_IP}, {"Namespace":POD_NAMESPACE}])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
