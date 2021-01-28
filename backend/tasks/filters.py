import django_filters
from django_filters import FilterSet

from .models import Hint, Task


class TaskFilter(FilterSet):
    """ Filter on date range """

    start_date = django_filters.DateFilter("created", "gte")
    end_date = django_filters.DateFilter("created", "lte")

    class Meta:
        model = Task
        fields = ["start_date", "end_date"]
