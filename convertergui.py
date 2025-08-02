from flask import render_template
from converter import generate_currency_options

def get_converter_content():
    return render_template("converter.html")