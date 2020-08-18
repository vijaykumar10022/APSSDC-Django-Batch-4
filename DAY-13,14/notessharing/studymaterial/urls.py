from django.urls import path

from studymaterial import views

urlpatterns = [
	path('showmaterials',views.showmaterials,name="showmaterials"),
	path('addmaterial/',views.addmaterial,name="addmaterial"),
	path('editmaterial/<int:id>/',views.editmaterial,name="editmaterial"),
	path('deletematerial/<int:id>/',views.deletematerial,name="deletematerial"),
	]

