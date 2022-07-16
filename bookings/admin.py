from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking, UserReg


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = (
        'user', 'booking_date', 'booking_time', 'booking_covers',
        'booking_confirmed', 'booking_id', 'created_on')
    search_fields = ('booking_id', 'user')
    list_filter = ('booking_confirmed', 'booking_time', 'booking_date')
    readonly_fields = ('booking_id',)
    summernote_fields = ('booking_comment')
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(booking_confirmed=True)


# @admin.register(UserReg)
# class UserRegAdmin(admin.ModelAdmin):
#     list_display = ('email', 'first_name', 'last_name', 'contact_no')
#     search_fields = ('email', 'contact_no')
