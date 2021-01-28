import django_filters
from django_filters import FilterSet

from .models import Task, Hint


class TaskFilter(FilterSet):
    ''' Filter on date range '''
    start_date = django_filters.DateFilter(name="created", lookup_type='gte')
    end_date = django_filters.DateFilter(name="created", lookup_type='lte')

    class Meta:
        model = Task
        fields = ['start_date', 'end_date']
