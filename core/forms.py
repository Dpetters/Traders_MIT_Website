from django import forms
from django.forms.widgets import HiddenInput

from core.models import ApplicantPoll, Applicant

APPLICANT_RATING = (
('', "select one"),
(3, "I've know this person for a long time and think they'd make a good fit"),
(2, "I've gotten to spent some time with the person and I think they'd make a good fit"),
(1, "I've gotten to interview the person and I think they'd make a good fit"),
(0, "I don't feel like I know enough about hte persn to make a decision"),
(-1, "I've gotten to interview the person and I don't think they'd make a good fit"),
(-2, "I've gotten to spent some time with the person and I don't think they'd make a good fit"),
(-3, "I've know this person for a long time and don't think they'd make a good fit")
)

class ApplicantForm(forms.Form):
    id = forms.IntegerField(widget = HiddenInput)

    positive1 = forms.CharField(label = "Reason for", required = False, max_length = 100)
    positive2 = forms.CharField(label="Reason for", max_length = 100, required=False)
    positive3 = forms.CharField(label="Reason for", max_length = 100, required=False)

    negative1 = forms.CharField(label="Reason against", required = False, max_length = 100)
    negative2 = forms.CharField(label="Reason against", max_length = 100, required=False)
    negative3 = forms.CharField(label="Reason against", max_length = 100, required=False)

    rating = forms.ChoiceField(label="Overall Rating", choices=APPLICANT_RATING, required=True)
