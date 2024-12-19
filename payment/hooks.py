from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
import time
from .models import Order

@receiver(valid_ipn_received)
def paypal_payment_recived(sender, **kwargs):
    time.sleep(10)
    paypal_obj = sender

    # Grab invoice

    my_invoice = str(paypal_obj.invoice)

    # let match the invoice to the paypal invoice
    my_order =Order.objects.get(invoice = my_invoice)

    my_order.paid = True

    my_order.save()


    # print(paypal_obj)
    # print(paypal_obj.mc_gross)