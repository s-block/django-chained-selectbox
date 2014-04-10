from chained_selectbox.forms import ChainedChoicesForm
from django import forms
from example.models import StandardModel, StandardModelTwo
from chained_selectbox.form_fields import ChainedChoiceField


class StandardModelForm(ChainedChoicesForm):
    class Meta:
        model = StandardModel

    field_one = forms.ChoiceField(choices=(('', '------------'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), ))
    field_two = ChainedChoiceField(parent_field='field_one', ajax_url='/chainedselectchoices')
    field_three = ChainedChoiceField(parent_field='field_two', ajax_url='/chainedselectchoices')


class StandardModelTwoForm(ChainedChoicesForm):
    class Meta:
        model = StandardModelTwo

    field_one = forms.ChoiceField(choices=(('', '------------'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), ))
    field_two = ChainedChoiceField(parent_field='field_one', ajax_url='/chainedselectchoices')
    field_three = ChainedChoiceField(parent_field='field_two', ajax_url='/chainedselectchoices')
