from django.shortcuts import render
from .models import MyProfile


def my_profile(request):
    """
    Renders the My Profile page
    """
    profile = MyProfile
    
    return render(
        request,
        "profile/profile.html",
        {"profile": profile},
    )

# def my_profile(View):
#     """
#     Renders the My Profile view.
#     """
#     # my_profile = MyProfile.objects.all()

#     # return render(
#     #     request,
#     #     "my_profile/my_profile.html",
#     #     {"my_profile": my_profile},
#     # )
    
#     def getprofile(self, request):
#         if request.user.is_authenticated:
#             users_profile = get_object_or_404(
#                 MyProfile,
#                 user=request.user
#             )
#             return render(
#                 request,
#                 'my_profile/my_profile.html',
#                 {'users_profile': users_profile,}
#             )
#         else:
#             return render(
#                 request,
#                 'account/login.html'
#             )
