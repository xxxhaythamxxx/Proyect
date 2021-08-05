from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('find', views.find,name='find'),
    path('chaining/', include('smart_selects.urls')),
    path("sparedetails/<str:val>?<str:val2>",views.sparedetails,name="sparedetails"),
    path("brand/<str:val>",views.brand,name="brand"),
    path("name/<str:val>",views.name,name="name"),
    path("manuf/<str:val>",views.manuf,name="manuf"),
    path("allmanu/<str:val>",views.allmanu,name="allmanu"),
    path("allmodel/<str:val>",views.allmodel,name="allmodel"),
    path("model/<str:val>",views.model,name="model"),
    path("engine/<str:val>",views.enginel,name="engine"),
    path('detail',views.detail,name='detail'),
    path("shape/<str:val>",views.shape,name="shape"),
    path("longi/<str:val1>?<str:val2>",views.longi,name="longi"),
    path("atributes/<str:val1>?<str:val2>",views.atributes,name="atributes"),
    path("carBrands",views.carBrands,name="carBrands"),
    # path("categoryi",views.categoryi,name="categoryi"),
    path("categoryi/<str:val>",views.categoryi,name="categoryi"),
    path("chasis/<str:val>",views.chasis,name="chasis"),
    path("prev/<str:val>?<str:val2>",views.prev,name="prev"),
    path("next/<str:val>?<str:val2>",views.next,name="next"),
    path("filldb",views.filldb,name="filldb"),
    path("fillcar",views.fillcar,name="fillcar"),
    path("fillengine",views.fillengine,name="fillengine"),
    path("fillspare/<str:val>",views.fillspare,name="fillspare"),
    path("editspare",views.editspare,name="editspare"),
    path("deletespare/<str:val>",views.deletespare,name="deletespare"),

    # path('getCar/$', views.getCar,name="getCar")
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)