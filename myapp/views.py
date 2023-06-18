
from django.shortcuts import render, redirect
from .forms import IssueForm

def create_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = IssueForm()
    return render(request, 'create_issue.html', {'form': form})




