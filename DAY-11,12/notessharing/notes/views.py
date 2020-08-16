from django.shortcuts import render,redirect

from django.http import HttpResponse

from datetime import date

from notes.models import Materials

# Create your views here.
def addnotes(request):
	if request.method=="POST":
		b=request.POST['branch']
		sub=request.POST['subject']
		notes=request.FILES['notes']
		desc=request.POST['description']
		Materials.objects.create(branch=b,subject=sub,
			notes=notes,description=desc,uploadingdate=date.today())
		return HttpResponse('successfully added..')
	return render(request,'notes/addnotes.html')


def shownotes(request):
	data=Materials.objects.all()
	return render(request,'notes/shownotes.html',{'notes':data})


def editnotes(request,id):
	notes=Materials.objects.get(id=id)
	if request.method == 'POST':
		br = request.POST['branch']
		sub = request.POST['subject']
		desc= request.POST['description']
		mat = request.FILES['material']
		notes.notes = mat
		notes.branch=br
		notes.subject=sub
		notes.description=desc
		notes.save()
		return redirect('shownotes')
	return render(request, 'notes/editnotes.html',{'docs':notes})

