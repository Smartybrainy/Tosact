from django import forms


class ContactEnquiriesForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(
                               attrs={
                                   "class": "form-control",
                                   "id": "name",
                                   "placeholder": "Please enter your name."
                               }))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "email",
            "placeholder": "Your Email"
        }))
    phone_number = forms.CharField(
        max_length=16,
        widget=forms.NumberInput(
            attrs={
                # "type": "number",
                "class": "form-control",
                "id": "phone",
                "placeholder": "Please enter your phone number."
            }))
    message = forms.CharField(max_length=1500,
                              widget=forms.Textarea(
                                  attrs={
                                      'rows': 5,
                                      'cols': 12,
                                      "class": "form-control",
                                      "id": "message",
                                      "placeholder": "Your Message."
                                  }))
