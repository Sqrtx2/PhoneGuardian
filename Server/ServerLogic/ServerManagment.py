from flask import Flask, render_template, request
import os
from LookUp.Search import search



current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, '..', 'html_templates')
site = Flask(__name__, template_folder=template_dir)


@site.route('/')
def welcome():
    return render_template(template_name_or_list='welcome.html')

@site.route('/search', methods=['POST'])
def search_number():
    try:
        if 'phone_number' in request.form.keys():
            pnumber = request.form['phone_number']
            if pnumber[0:4] == "+972":
                pnumber = "0" + pnumber[4:]
            print(search(pnumber))
            response = search(pnumber)
            response_html = response.replace('\n', '<br>')
            return response_html, 200, {'Content-Type': 'text/html'}
        else:
            return "Please provide a valid phone number", 500 ,{'Content-Type': 'text/html'}
    except:
        return "Please provide a valid phone number", 500 ,{'Content-Type': 'text/html'}

@site.route('/search_via_url/<phonenumber>')
def search_number_via_url(phonenumber):
    try:
        print(phonenumber)
        # I need to find a way to get all the phone numbers in the same standard instead of using this if block
        if phonenumber[0:4] == "+972":
            phonenumber = "0" + phonenumber[4:]
        print("sliced number", phonenumber)
        response = search(phonenumber)
        return response, 200, {'Content-Type': 'text/plain'}
    except:
        return "Please provide a valid phone number", 500 ,{'Content-Type': 'text/html'}


if __name__ == "__main__":
    context = ('Server/ServerLogic/SSL_certificate/cert.pem', 'Server/ServerLogic/SSL_certificate/key.pem') # certificate and key files
    site.run(host='0.0.0.0', port=5555, debug=True, ssl_context=context)
    # for creating a self signed cetificate run this in CMD in the desired directory
    # "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 3650