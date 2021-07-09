
from django.views.generic import ListView
from .models import PackageItem
from django.db.models import Q

# Create your views here.

class SearchClass(ListView):
    model = PackageItem
    template_name = 'result.html'

    # defining quaryset
    def get_queryset(self):
        query = self.request.GET.get('quary')
        object_list = PackageItem.objects.filter(Q(tracking_number__icontains=query))
        return object_list
