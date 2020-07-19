
from wtforms import Form, StringField, SelectField, validators

class SearchForm(Form):
    search = StringField('')
