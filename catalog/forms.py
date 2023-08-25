from django import forms
from django.core.exceptions import ValidationError

from catalog.models.products import Product
from catalog.models.version import Version


class StyleForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'sign_current_version':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_id'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        tags = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        name = self.cleaned_data['name']

        for tag in tags:
            if name in tag:
                raise ValidationError('Недопустимое значение')
        return name

    def clean_desc(self):
        tags = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        desc = self.cleaned_data['desc']

        for tag in tags:
            if desc in tag:
                raise ValidationError('Недопустимое значение')
        return desc


class VersionForm(StyleForm, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
