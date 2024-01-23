from django.shortcuts import render
from testapp.forms import FeedBackForm

# Create your views here.
def feedback_view(request):
    form = FeedBackForm()
    submitted = False
    name = ''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print('Form calidation succes and printing feedback information')
            print('*'*58)
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rollno'])
            print('MailID:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted = True
            name = form.cleaned_data['name']
        else:
            print('some field validate fails')

    return render(request,'testapp/feedback.html',{'form':form,'submitted':submitted,'name':name})
