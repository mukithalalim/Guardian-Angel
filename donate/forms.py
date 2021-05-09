from django.forms import ModelForm
from .models import Payment


class PaymentForm(ModelForm):
    """
	This class takes a helper class ModelForm that 
    lets you create a Form class from a Django model.
	"""
    class Meta:
        model = Payment
        fields = '__all__'