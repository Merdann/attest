from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.payment_form_view, name='payment_form_view'),
    # path('red_to_check/', views.red_to_check, name='red_to_check'),
    # path('check/', views.send_check, name='send_check'),
    #
    # path('red_to_ext/'
    #      '<slug:order_no>&'
    #      '<slug:product_name>&'
    #      '<slug:product_count>&'
    #      '<slug:product_price>&'
    #      '<slug:total_sum>',
    #      views.red_to_ext, name='red_to_ext'),

]
