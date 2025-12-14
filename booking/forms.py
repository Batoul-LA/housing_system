from django import forms
from .models import Booking,Payment

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['student', 'room', 'start_date', 'end_date', 'status', 'payment_status']
    
    def clean(self):
            cleaned_data = super().clean()
            start_date = cleaned_data.get("start_date")
            end_date = cleaned_data.get("end_date")

            if start_date and end_date and end_date < start_date:
                raise forms.ValidationError("تاريخ الانتهاء يجب أن يكون بعد أو يساوي تاريخ البداية.")
            return cleaned_data
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'status']
