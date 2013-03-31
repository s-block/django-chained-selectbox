django-chained-selectbox
========================

Chained select box widget using AJAX for Django Admin. Chains select boxes together so the values change depending on the parent value.

Installation
------------

pip install -e git+git://github.com/s-block/django-chained-selectbox.git#egg=django-chained-selectbox


Usage
-----

Add `chained_selectbox` to `INSTALLED_APPS`

Form must inherit from ChainedChoicesForm which loads the options when there is already an instance.

`    class StandardModelForm(ChainedChoicesForm):
        field_one = forms.ChoiceField(choices=(('', '------------'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), ))
        field_two = ChainedChoiceField(parent_field='field_one', ajax_url='/chainedselectchoices')
        field_three = ChainedChoiceField(parent_field='field_two', ajax_url='/chainedselectchoices')
`

Ajax call is made whenever the parent field is changed. You must set up the ajax to return json list of lists.

`    class ChainedSelectChoices(BaseDetailView):
        """
        View to handel the ajax request for the field options.
        """

        def get(self, request, *args, **kwargs):
            field = request.GET.get('field')
            parent_value = request.GET.get("parent_value")

            vals_list = []
            for x in range(1,5):
                vals_list.append(x*int(parent_value))

            choices = tuple(zip(vals_list, vals_list))

            response = HttpResponse(
                json.dumps(choices, cls=DjangoJSONEncoder),
                mimetype='application/javascript'
            )
            add_never_cache_headers(response)
            return response
`
