from datetime import datetime
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from .models import *


class CustomDateInput(DateInput):
    input_type = "date"


# CKEDITOR BAKILACAK!
class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            "dateofaddition": CustomDateInput(),
            "fixtureDescription": CKEditorWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(FixtureForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # Tüm alanlara form-control sınıfını ekler
            if field_name == "dateofaddition":
                field.widget.attrs["input_type"] = "date"
            field.widget.attrs["class"] = "form-control mb-3 rounded"

            # Alan adına göre etiket ekler
            field.widget.attrs["placeholder"] = field.label

            if field_name == "totalprice":
                field.widget.attrs["input_type"] = "number"
                field.widget.attrs["disabled"] = True

            if field_name == "companyAddress":
                field.widget.attrs["style"] = "height: 124px;"


# set general buluntu form field


class GeneralBuluntuForm(forms.ModelForm):
    class Meta:
        model = SetGeneralBuluntu
        fields = "__all__"
        exclude = ["user"]


# ends


class GeneralInstructionsForm(forms.ModelForm):
    class Meta:
        model = GeneralInstructions
        fields = "__all__"


class BuluntuImagesForm(forms.ModelForm):
    class Meta:
        model = BuluntuImages
        fields = "__all__"
        exclude = ["buluntu"]


class MinorBuluntuForm(forms.ModelForm):
    class Meta:
        model = MinorBuluntu
        fields = "__all__"
        exclude = ["processedBy"]


class AcmaRaporForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(AcmaRaporForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == "rapor_type":
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control mb-3 rounded"
                field.widget.attrs["placeholder"] = field.label

            if field_name == "user":
                field.initial = user
                field.disabled = True

    class Meta:
        model = AcmaRapor
        fields = "__all__"
        widgets = {"rapordate": CustomDateInput(),
                   "rapor_type": forms.RadioSelect()}