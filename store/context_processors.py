from django.db.models import Sum

from .models import OrderItem


def cart_item_count(request):
    if not request.user.is_authenticated:
        return {"cart_item_count": 0}

    cart_count = (
        OrderItem.objects.filter(order__user=request.user, order__paid=False)
        .aggregate(total_quantity=Sum("quantity"))
        .get("total_quantity")
        or 0
    )

    return {"cart_item_count": cart_count}
