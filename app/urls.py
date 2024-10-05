from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AllServices, AllProjects, get_commodity_prices, AllNews, AllTrianings,  contact_form_submission

urlpatterns = [
    path('AllServices/', AllServices.as_view()),

    path('AllProjects/', AllProjects.as_view()),

    path('AllNews/', AllNews.as_view()),

    path('AllTrianings/', AllTrianings.as_view()),

    path('oil-price/', get_commodity_prices, name='get_oil_price'),

    path('submit-contact-form/', contact_form_submission,
         name='submit-contact-form'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
