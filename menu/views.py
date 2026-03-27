from django.db.models import Prefetch
from rest_framework.generics import ListAPIView
from .models import FoodCategory, Food, FoodListSerializer


class FoodListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.filter(
            food__is_publish=True
        ).distinct()

        queryset = queryset.prefetch_related(
            Prefetch(
                'food',
                queryset=Food.objects.filter(is_publish=True).order_by('internal_code')
            )
        )

        queryset = queryset.order_by('order_id', 'name_ru')
        
        return queryset
