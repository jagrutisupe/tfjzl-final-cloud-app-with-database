from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission
# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2  # Number of empty extra forms displayed
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
# <HINT> Register Question and Choice models here
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # Allows editing choices on the question page
    list_display = ['content']  # Columns displayed in admin list view
admin.site.register(Course, CourseAdmin)  # Assuming CourseAdmin exists
admin.site.register(Lesson, LessonAdmin)  # Assuming LessonAdmin exists
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
