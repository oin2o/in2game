from django_filters import FilterSet
from django_filters.filters import OrderingFilter

from .models import User


class UserFilter(FilterSet):
    # add order fileds
    order_by_field = 'ordering'
    ordering = OrderingFilter(
        fields=(
            'username',
        )
    )
    
    class Meta:
        model = User
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(UserFilter, self).__init__(*args, **kwargs)
