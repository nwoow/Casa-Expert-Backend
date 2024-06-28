from django.contrib import admin
from .models import User,Booking,Address,RejectReason,ProductReview,BookingProduct,BookingHistory
# Register your models here.


admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Address)
admin.site.register(RejectReason)
admin.site.register(ProductReview)
admin.site.register(BookingProduct)
admin.site.register(BookingHistory)