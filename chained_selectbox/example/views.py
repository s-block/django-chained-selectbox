from django.utils.cache import add_never_cache_headers
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views.generic.detail import BaseDetailView


class ChainedSelectChoices(BaseDetailView):
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

