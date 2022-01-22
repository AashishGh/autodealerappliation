from django.shortcuts import render
from django.db.models import Sum
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models.functions import TruncMonth
from django.db.models import Count

from customer.models import Customer
from vehicle.models import Vehicle
from sale.models import Sale
from purchase.models import Purchase


class IndexView(TemplateView):
    template_name = "home/index.html"


@method_decorator(login_required, name="dispatch")
class DashboardView(TemplateView):
    template_name = "home/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "dashboard"
        context["customers"] = Customer.objects.all()[:5]
        context["vehicle_count"] = Vehicle.objects.count()
        context["sale_count"] = Sale.objects.count()
        context["customer_count"] = Customer.objects.count()
        sale = Sale.objects.aggregate(total=Sum("amount"))
        purchase = Purchase.objects.aggregate(total=Sum("price"))
        if sale["total"] and purchase["total"]:
            context["revenue"] = sale["total"] - purchase["total"]
        else:
            context["revenue"] = 0
        objs = Sale.objects.filter(sale_date__contains=2020).annotate(month=TruncMonth('sale_date')).values('month').annotate(total=Count('id'))
        
        return context


def error_404(request, exception):
    data = {}
    return render(request, "home/404.html", data)


def error_403(request, exception):
    data = {}
    return render(request, "home/403.html", data)


def error_500(request):
    data = {}
    return render(request, "home/500.html", data)


def error_400(request, exception):
    data = {}
    return render(request, "home/500.html", data)
