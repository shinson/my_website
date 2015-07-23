from wtforms import Form, TextAreaField, StringField, validators


# A simple contact form with four fields.
class ContactForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=25)])
	email = StringField('Email Address', [validators.Length(min=6, message= u'Little short for an email address, eh?'),validators.Email(message= u'That\'s not a valid email address.')])
	subject = StringField('Subject', [validators.Length(min=1, max=25)])
	message = TextAreaField('Message')
	