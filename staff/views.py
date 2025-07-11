from django.shortcuts import render, redirect

from .forms import StaffForm


def create_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            print(f"staff valid data: {form.cleaned_data}")
            form.save()
            return redirect('post_list')
    else:
        form = StaffForm()
    return render(request, 'staff/create.html', {'form': form})
