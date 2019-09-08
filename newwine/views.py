from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import RegistrationForm
import csv
from django.http import HttpResponse


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="members.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Surname', 'Email', 'Gender', 'Date Of Birth', 'Course', 'Year',
                     'Hall Or Hostel', 'Room', 'Department', 'Covenant Family', 'Home temple', 'Phone'])
    members = RegisteredMembers.objects.all().values_list('first_name', 'surname', 'email', 'gender', 'date_of_birth',
                                                          'course', 'year', 'hall_or_hostel', 'room', 'department',
                                                          'covenant_family', 'home_temple', 'phone')
    for member in members:
        writer.writerow(member)
    return response


class IndexView(generic.ListView):
    template_name = 'newwine/index.html'
    context_object_name = 'home_list'
    queryset = Carousel.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['carousel'] = Carousel.objects.all()
        context['mainevent'] = MainEvent.objects.all().order_by("-added")[:1]
        context['sermons'] = LatestSermons.objects.all()
        context['quotes'] = Quote.objects.all().order_by("-added")[:1]
        context['announcements'] = Announcements.objects.all().order_by("-added")[:5]
        context['family'] = Family.objects.all()
        return context


class AboutView(generic.ListView):
    template_name = 'newwine/about.html'
    context_object_name = 'about_list'
    queryset = Initiators.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        context['initiators'] = Initiators.objects.all()
        return context


class ExecutiveView(generic.ListView):
    template_name = 'newwine/executives.html'
    context_object_name = 'all'
    queryset = ExecutivesThumbnail.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ExecutiveView, self).get_context_data(**kwargs)
        context['thumbnail'] = ExecutivesThumbnail.objects.all()
        context['details'] = ExecutivesDetails.objects.all()
        context['family'] = Family.objects.all()
        return context


class DocumentsView(generic.ListView):
    template_name = 'newwine/documents.html'
    context_object_name = 'all'
    queryset = Family.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DocumentsView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        return context


class ImagesView(generic.ListView):
    template_name = 'newwine/pictures.html'
    context_object_name = 'all'
    queryset = Gallery.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ImagesView, self).get_context_data(**kwargs)
        context['albums'] = Gallery.objects.all().order_by("-added")
        context['images'] = Images.objects.all()
        context['family'] = Family.objects.all()
        return context


class SermonsView(generic.ListView):
    template_name = 'newwine/sermons.html'
    context_object_name = 'all_sermons'
    queryset = Sermons.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SermonsView, self).get_context_data(**kwargs)
        context['sermons'] = Sermons.objects.all()
        context['family'] = Family.objects.all()
        return context


class VideosView(generic.ListView):
    template_name = 'newwine/videos.html'
    context_object_name = 'all'
    queryset = Family.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VideosView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        return context


class RegistrationFormView(generic.ListView):
    form_class = RegistrationForm
    template_name = 'newwine/registration.html'
    context_object_name = 'family'
    queryset = Family.objects.all()
    

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'family': self.queryset})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            userdata = form.save(commit=False)

            # cleaned data
            first_name = form.cleaned_data['first_name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            date_of_birth = form.cleaned_data['date_of_birth']
            course = form.cleaned_data['course']
            year = form.cleaned_data['year']
            hall_or_hostel = form.cleaned_data['hall_or_hostel']
            room = form.cleaned_data['room']
            department = form.cleaned_data['department']
            covenant_family = form.cleaned_data['covenant_family']
            home_temple = form.cleaned_data['home_temple']
            phone = form.cleaned_data['phone']

            if RegisteredMembers.objects.filter(first_name=form.cleaned_data['first_name']).exists() \
                    and RegisteredMembers.objects.filter(surname=form.cleaned_data['surname']).exists():
                return render(request, 'newwine/form_exists.html', {'family': Family.objects.all()})
            else:
                userdata.save()
                return render(request, 'newwine/registration_confirmation.html', {'family': Family.objects.all()})
        return render(request, 'newwine/registration_error.html', {'family': Family.objects.all()})
    


class DepartmentView(generic.DetailView):
    model = Departments
    template_name = "newwine/department.html"

    def get_context_data(self, **kwargs):
        context = super(DepartmentView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        return context


class ArticlesListView(generic.ListView):
    model = Articles
    template_name = "newwine/articles.html"
    queryset = Articles.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ArticlesListView, self).get_context_data(**kwargs)
        context['articles'] = Articles.objects.all()
        context['family'] = Family.objects.all()
        return context


class ArticlesDetailView(generic.DetailView):
    model = Articles
    template_name = "newwine/article-details.html"

    def get_context_data(self, **kwargs):
        context = super(ArticlesDetailView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        return context


class TestimonyListView(generic.ListView):
    model = Testimonies
    template_name = "newwine/testimonies.html"
    queryset = Testimonies.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TestimonyListView, self).get_context_data(**kwargs)
        context['testimonies'] = Testimonies.objects.all()
        context['family'] = Family.objects.all()
        return context


class TestimonyDetailView(generic.DetailView):
    model = Testimonies
    template_name = "newwine/testimony-details.html"

    def get_context_data(self, **kwargs):
        context = super(TestimonyDetailView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        return context


class NoteListView(generic.ListView):
    model = Notes
    template_name = "newwine/teachings.html"
    queryset = Notes.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        context['notes'] = Notes.objects.all()
        context['family'] = Family.objects.all()
        return context


class NoteDetailView(generic.DetailView):
    model = Notes
    template_name = "newwine/teaching-details.html"

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        return context


class OutlineListView(generic.ListView):
    model = Outlines
    template_name = "newwine/outlines.html"
    queryset = Outlines.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OutlineListView, self).get_context_data(**kwargs)
        context['outlines'] = Outlines.objects.all()
        context['family'] = Family.objects.all()
        return context


class OutlineDetailView(generic.DetailView):
    model = Outlines
    template_name = "newwine/outline-details.html"

    def get_context_data(self, **kwargs):
        context = super(OutlineDetailView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        return context


class TeamsListView(generic.DetailView):
    model = Teams
    template_name = "newwine/team.html"

    def get_context_data(self, **kwargs):
        context = super(TeamsListView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        return context


class CoordinatorListView(generic.DetailView):
    model = Coordinator
    template_name = "newwine/coordinators.html"

    def get_context_data(self, **kwargs):
        context = super(CoordinatorListView, self).get_context_data(**kwargs)
        context['family'] = Family.objects.all()
        return context


class GenderListView(generic.ListView):
    model = Gender
    template_name = "newwine/gender-coordinators.html"
    queryset = Gender.objects.all()

    def get_context_data(self, **kwargs):
        context = super(GenderListView, self).get_context_data(**kwargs)
        context['gender'] = Gender.objects.all()
        context['family'] = Family.objects.all()
        return context


class ThemeListView(generic.ListView):
    model = Theme
    template_name = "newwine/theme.html"
    queryset = Theme.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ThemeListView, self).get_context_data(**kwargs)
        context['theme'] = Theme.objects.all()
        context['family'] = Family.objects.all()
        return context
