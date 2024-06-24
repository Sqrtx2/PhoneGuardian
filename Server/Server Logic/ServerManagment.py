from flask import Flask, render_template
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, '..', 'html_templates')
site = Flask(__name__, template_folder=template_dir)


@site.route('/')
def welcome():
    return render_template(template_name_or_list='welcome.html')

if __name__ == "__main__":
    site.run(host='0.0.0.0', port=5555, debug=True)
    print (current_dir)
    print(template_dir)