from django import forms
from django.conf import settings

class LotteryTicketForm(forms.Form):
    numbers = forms.MultipleChoiceField(
        label="number selection",
        choices=[(str(n), str(n)) for n in settings.LOTTERY_NUMBER_RANGE],
        widget=forms.CheckboxSelectMultiple,
    )

    def clean_numbers(self):
        numbers = self.cleaned_data["numbers"]
        if len(set(numbers)) != settings.LOTTERY_TICKET_NUMBERS:
            raise forms.ValidationError(
                "You must select {} different numbers".format(settings.LOTTERY_TICKET_NUMBERS),
            )
        return numbers
