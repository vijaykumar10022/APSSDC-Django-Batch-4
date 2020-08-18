from django.shortcuts import render,redirect

from django.http import HttpResponse

from datetime import date

from notes.models import Materials
from notes.forms import updatenotesForm

from django.contrib import messages

# Create your views here.
def addnotes(request):
	if request.method=="POST":
		b=request.POST['branch']
		sub=request.POST['subject']
		notes=request.FILES['notes']
		desc=request.POST['description']
		Materials.objects.create(branch=b,subject=sub,
			notes=notes,description=desc,uploadingdate=date.today())
		messages.success(request,'%s subject is successfully added..!'%(sub))
		return redirect('/')
	return render(request,'notes/addnotes.html')


def shownotes(request):
	data=Materials.objects.all()
	return render(request,'notes/shownotes.html',{'notes':data})


def editnotes(request,id):
	current_notes=Materials.objects.get(id=id)
	form=updatenotesForm(request.POST,request.FILES,instance=current_notes)
	if form.is_valid():
	 	form.save()
	 	return redirect('/')
	return render(request, 'notes/editnotes.html',{'docs':current_notes})


def deletenotes(request,id):
	data=Materials.objects.get(id=id)
	if request.method=="POST":
		data.delete()
		messages.error(request,'successfully deleted')
		return redirect('/')
	return render(request,'notes/deletenotes.html',{'data':data})




# def editnotes(request,id):
# 	notes=Materials.objects.get(id=id)
# 	if request.method == 'POST':
# 		br = request.POST['branch']
# 		sub = request.POST['subject']
# 		desc= request.POST['description']
# 		mat = request.FILES['material']
# 		# notes.notes = mat
# 		# notes.branch=br
# 		# notes.subject=sub
# 		# notes.description=desc
# 		updatenotes=notes(notes=mat,branch=br,subject=sub,description=desc)
# 		updatenotes.save()
# 		return redirect('shownotes')
# 	return render(request, 'notes/editnotes.html',{'docs':notes})

