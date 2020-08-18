from django.shortcuts import render,redirect

from django.http import HttpResponse

from studymaterial.forms import AddNotesForm

from django.contrib import messages

from studymaterial.models import Notes

# Create your views here.

def showmaterials(request):
	data=Notes.objects.all()
	return render(request,'studymaterial/showmaterials.html',{'data':data})



def addmaterial(request):
	if request.method=="POST":
		form=AddNotesForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			subject=form.cleaned_data.get('subject')
			messages.success(request,'%s is successfully added'%(subject))
			return redirect('showmaterials')
	form=AddNotesForm()
	return render(request,'studymaterial/addnotes.html',{'form':form})


def editmaterial(request,id):
	mat=Notes.objects.get(id=id)
	if request.method=="POST":
		form=AddNotesForm(request.POST,request.FILES,instance=mat)
		if form.is_valid():
			form.save()
			messages.info(request,'successfully updated..!')
			return redirect('showmaterials')
	form=AddNotesForm(instance=mat)
	return render(request,'studymaterial/editmaterial.html',{'form':form})

def deletematerial(request,id):
	data=Notes.objects.get(id=id)
	if request.method=="POST":
		data.delete()
		messages.warning(request,'successfully deleted')
		return redirect('showmaterials')
	return render(request,'studymaterial/deletematerial.html',{'data':data})
