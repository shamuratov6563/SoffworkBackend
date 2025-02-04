from rest_framework import permissions


# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to allow only the owner of a post to edit it.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request (safe methods)
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Write permissions are only allowed to the owner of the post
#         return obj.owner == request.user




from rest_framework import permissions

class IsPortfolioOwnerOrSuperuser(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
            return True
       return obj.seller == request.user or request.user.is_superuser
   
   
   


class IsCommentOwnerOrSuperuser(permissions.BasePermission):
    
   def has_object_permission(self, request, view, obj):
         
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.commentator == request.user or request.user.is_superuser

   
