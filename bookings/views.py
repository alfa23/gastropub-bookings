from django.shortcuts import render, reverse, redirect
# Import Django generic library, import Template View from views.generic
# from django.views import generic
from django.views.generic import TemplateView
from django.views import View
# Import Booking & User models from .models
# from .models import Booking, UserReg


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class MenuView(TemplateView):
    template_name = 'menu.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html',)


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html',)


class Booking(View):
    """ This class handles all booking through POST & GET requests. """

    def get(self, request):
        return render(request, 'bookings/create.html', {})

    # def post(self, request):
    #     booking_covers = request.POST.get("booking_covers")
    #     booking_date = request.POST.get("booking_date")
    #     booking_time = request.POST.get("booking_time")
    #     booking_comment = request.POST.get("booking_comment")
    #     booking_id = request.POST.get("booking_id")

    #     web_booking = Booking.objects.create(
    #         booking_covers=booking_covers,
    #         booking_date=booking_date,
    #         booking_time=booking_time,
    #         booking_comment=booking_comment,
    #         booking_id=request.booking_id
    #     )

    #     web_booking.save()

    #     # return redirect(reverse(''))

