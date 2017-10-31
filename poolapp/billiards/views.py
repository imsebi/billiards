from django.shortcuts import render

def index(request):
    return render(request, 'poolapp/index.html')
    
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.rank = '2'
    user.save()


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, _('Your rank was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
    })
