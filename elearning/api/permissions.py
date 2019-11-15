from rest_framework import permissions


class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are allowed only to teachers
        return request.user.is_teacher


class CannEnrollToCourse(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.can_enroll_to_course(obj)


# class IsEnrolled(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.students.filter(id=request.user.id).exists()


class CanTakeLesson(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_student

    def has_object_permission(self, request, view, obj):
        return request.user.can_take_lesson(obj)
