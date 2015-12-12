from django import forms

class LotteryTicketForm(forms.Form):
    numbers = forms.MultipleChoiceField(
        label="number selection",
        choices=[(str(n), str(n)) for n in range(1, 43)],
        widget=forms.CheckboxSelectMultiple,
    )
