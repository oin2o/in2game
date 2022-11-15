from django_filters import FilterSet, NumberFilter
from django_filters.filters import OrderingFilter

from .models import Game


class GameFilter(FilterSet):
    # add condition field that is not equal condition
    state__lte = NumberFilter(field_name="state", lookup_expr="lte")
    # add order fileds
    order_by_field = 'ordering'
    ordering = OrderingFilter(
        fields=(
            'created_at',
        )
    )
    
    class Meta:
        model = Game
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(GameFilter, self).__init__(*args, **kwargs)
