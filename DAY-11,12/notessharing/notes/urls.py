from django.urls import path

from notes import views




urlpatterns = [

	#path('',views.home,name="home"),

	path('addnotes/',views.addnotes,name="addnotes"),

	path('shownotes/',views.shownotes,name="shownotes"),

	path('editnotes/<int:id>/',views.editnotes,name="editnotes"),

	]