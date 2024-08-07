from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


topic_choices = (
        ('enquiry', 'Enquiry'),
        ('sales', 'Sales'),
        ('support', 'Support'),
    )

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255,required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=255,required=True)
    topic = forms.ChoiceField(choices=topic_choices,required=True)
    company = forms.CharField(max_length=255, required=False)  # Optional field  # Optional field
    message = forms.CharField(required=True,widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-contactForm'
        self.helper.form_class = 'form-control'
        self.helper.form_method = 'post'
        self.helper.form_action = 'website:contacts'

        self.helper.add_input(Submit('submit', 'Submit'))