from flask import Flask, request, render_template
import os
import re

app = Flask(__name__)

def listToString(s): 
    
	# initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    # return string  
    return str1

	
@app.route('/')
def index():
	return render_template('index.html')
	
#extract all the files in folder
@app.route('/files',methods=['POST'])
def files():
	files = os.listdir(request.form['iname'])
	with open(request.form['outname'],"w") as wfile:
		wfile.write("<AR-PACKAGES>\n")
		wfile.write("	<AR-PACKAGE UUID=\"c93500b2-3e2b-40bb-b666-d1993f701457\">\n")
		for infile in files:
			if infile.endswith(".arxml"):
				with open(infile) as rfile:
					losd='<SHORT-NAME>'
					enddel='</ELEMENTS>'
					block=re.findall('(?:' + losd + r')([\s\S]*?)'+enddel, rfile.read())
					wfile.write("	  <SHORT-NAME>")
					wfile.write(listToString(block))
					wfile.write("</ELEMENTS>\n")
		wfile.write("	</AR-PACKAGES>\n")
		wfile.write("</AR-PACKAGES>\n")
	
	return "ok"
    
	
	
@app.route('/my-link/')
def my_link():
	return 'Click.'
	
	
  
	
if __name__ == '__main__':
	app.debug=True
	app.run('0.0.0.0', port = 65432 )
	
    
  
	