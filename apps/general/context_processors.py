from apps.general.models import General, GeneralSocialMedia
from apps.wishlist.models import Wishlist


def general_context(request):
    from apps.products.models import Product
    context = {
        'general': General.objects.all(),
        'general_social_media': GeneralSocialMedia.objects.all(),
        'wishlist': Wishlist.objects.all(),
        'currency' : request.session.get('currency', Product.DEFAULT_CURRENCY),
        'currency_list': Product.Currency.values
    }
    return context