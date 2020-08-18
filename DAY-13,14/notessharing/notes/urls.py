from django.urls import path

from notes import views




urlpatterns = [

	path('',views.shownotes,name="shownotes"),
	
	path('addnotes/',views.addnotes,name="addnotes"),

	
	path('editnotes/<int:id>/',views.editnotes,name="editnotes"),
  
  	path('deletenotes/<int:id>/',views.deletenotes,name="deletenotes"),
	]