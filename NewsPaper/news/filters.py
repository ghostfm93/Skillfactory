from django_filters import FilterSet, DateFilter
from .models import Post
import django.forms

class NewsFilter(FilterSet):
    creation_time = DateFilter(
        lookup_expr='gte',
        widget=django.forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    class Meta:
        model = Post
        fields = {
            'head':['icontains'],
            'author':['exact'],
            'creation_time':[],
        }

