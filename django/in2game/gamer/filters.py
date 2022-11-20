from django_filters import FilterSet
from django_filters.filters import OrderingFilter

from .models import Gamer


class GamerFilter(FilterSet):
    # add order fileds
    order_by_field = 'ordering'
    ordering = OrderingFilter(
        fields=(
            'position',
            'status',
            'game__created_at',
        )
    )
    
    class Meta:
        model = Gamer
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(GamerFilter, self).__init__(*args, **kwargs)
