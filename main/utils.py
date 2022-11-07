from django.db.models import Max
from main.models import Composition


def get_max_order() -> int:
    existing_compositions = Composition.objects.all()
    if not existing_compositions.exists():
        return 1
    else:
        current_max = existing_compositions.aggregate(max_order=Max('order'))['max_order']
        return current_max + 1
