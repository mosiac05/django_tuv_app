from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    message = forms.CharField(
                        max_length=254,
                        required=True,
                        widget=forms.Textarea(
                            attrs={
                                'class':"form-control w-100",
                                'id':"message",
                                'cols':"30",
                                'rows':"9",
                                'onfocus':"this.placeholder = ''",
                                'onblur':"this.placeholder = 'Enter Message'",
                                'placeholder':'Enter Message',
                                'required':'required'

                            }
                        ),
                        help_text = '*Required'
                    )

    name = forms.CharField(
                        max_length=50,
                        required=True,
                        widget=forms.TextInput(
                            attrs={
                                'class':"form-control",
                                'id':"name",
                                'onfocus':"this.placeholder = ''",
                                'onblur':"this.placeholder = 'Enter your name'",
                                'placeholder':'Enter your name',
                                'required':'required',
                            }
                        ),
                        help_text='*Required'
                        )

    email = forms.EmailField(
                        max_length=254,
                        required=True,
                        widget=forms.EmailInput(
                            attrs={
                                'class':"form-control",
                                'id':"email",
                                'onfocus':"this.placeholder = ''",
                                'onblur':"this.placeholder = 'Enter email address'",
                                'placeholder':'Enter email address',
                                'required':'required'
                            }
                        ),
                        help_text='*Required'
                    )

    subject = forms.CharField(
                        max_length=254,
                        required=True,
                        widget=forms.TextInput(
                            attrs={
                                'class':"form-control",
                                'id':"subject",
                                'onfocus':"this.placeholder = ''",
                                'onblur':"this.placeholder = 'Enter subject'",
                                'placeholder':'Enter subject',
                                'required':'required'
                            }
                        ),
                        help_text='*Required'
                    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')
        if not name and not email and not subject and not message:
            raise forms.ValidationError('You have to write something')
        return cleaned_data


class NewsLetterForm(forms.Form):

    user_email = forms.EmailField(
                        max_length=254,
                        required=True,
                        widget=forms.EmailInput(
                            attrs={
                                'placeholder':"Enter your mail"
                            }
                        ),
                        help_text='*Required'
                    )
