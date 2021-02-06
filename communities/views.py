import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from friends.models import CustomNotification
from friends.serializers import NotificationSerializer

from .models import *
from friends.models import Friend


# class PostCreateView(CreateView):
#     model = Post
#     http_method_names = ['post']
#     form_class = PostCreateForm
#     template_name = 'home.html'
#     success_url = reverse_lazy('communities:community')
#     def form_valid(self, form):
#         if self.request.user.is_authenticated:
#             form.instance.community = Community.objects.get(community_name = self.request.community.community_name)
#             form.instance.user = self.request.user
#         return super(PostCreateView, self).form_valid(form)

#     def form_invalid(self, form):
#         """If the form is invalid, render the invalid form."""
#         print(form.errors)
#         return redirect(reverse_lazy('communities:community'))

#     def post(self, *args, **kwargs):
#         form = self.get_form()
#         self.object = None
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


def create_comment(request, post_id=None):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        comment = post.comments.create(user=request.user, content=request.POST.get('content'))
        notification = CustomNotification.objects.create(type="comment", recipient=post.user, actor=request.user, verb="commented on your post")
        channel_layer = get_channel_layer()
        channel = "comment_like_notifications_{}".format(post.user.username)
        print(json.dumps(NotificationSerializer(notification).data))
        async_to_sync(channel_layer.group_send)(
            channel, {
                "type": "notify",
                "command": "new_like_comment_notification",
                "notification": json.dumps(NotificationSerializer(notification).data)
            }
        )
        return redirect(reverse_lazy('communities:communityfeed'))
    else:
        return redirect(reverse_lazy('communities:communityfeed'))

def communityfeed(request, community_name):
    community = Community.objects.get(community_name = community_name)
    if request.method == 'POST':
        body = request.POST.get('body')
        user = request.user
        post = Post.objects.create(user = user, body = body)
        post.save()
        community.posts.add(post)
    allPosts = community.posts.all()
    friends_one = Friend.objects.filter(friend=request.user).filter(status='friend')
    friends_two = Friend.objects.filter(user=request.user).filter(status='friend')
    friends_list_one = list(friends_one.values_list('user_id', flat=True))
    friends_list_two = list(friends_two.values_list('friend_id', flat=True))
    friends_list_id = friends_list_one + friends_list_two + [request.user.id]
    friends = friends_one.union(friends_two)
    context1 = {'community_name':community_name, 'allPosts':allPosts, 'friends': friends}
    return render(request,'home.html',context1)
    
def communities(request):
    allCommunities = Community.objects.all()
    context2 = {'allCommunities' : allCommunities}
    return render(request, 'communities/community_list.html', context2)
    