from django.shortcuts import render
from profiles.models import UserProfile


def staffindex(request):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        numusers = len(UserProfile.objects.all())
        return render(request, 'staff/staffindex.html', {'numusers': numusers})
