from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Choice, Question

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(admin.StackedInline):  # You can also use admin.StackedInline
    model = Choice
    extra = 3  # Number of empty choice forms to display

class QuestionInline(admin.StackedInline):  # You can also use admin.TabularInline
    model = Question
    #extra = 3  # Number of empty question forms to display

class LessonInline(admin.StackedInline):
    model = Lesson
    #extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
   # inlines = [QuestionInline]
    list_display = ['title']


# <HINT> Register Question and Choice models here
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('id', 'course', 'questiontext', 'questiongrade')
    search_fields = ('questiontext',)
    ordering = ('id',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choicecontent', 'is_correct')
    list_filter = ('question',)
    search_fields = ('choicecontent', 'question__questiontext')
    ordering = ('question', 'id')   

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
