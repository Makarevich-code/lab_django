from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Worker, Performance, Genre, Role, Award


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def how_to_find(request):
    return render(request, 'how_to_find.html')


def poster(request):
    performances = Performance.objects.all()[:6]
    return render(request, 'poster.html', {'performances': performances})


def troupe(request):
    workers = Worker.objects.all()
    return render(request, 'troupe.html', {'workers': workers})


class WorkerListView(ListView):
    model = Worker
    template_name = 'workers/list.html'
    context_object_name = 'workers'


class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'workers/detail.html'
    context_object_name = 'worker'


class WorkerCreateView(CreateView):
    model = Worker
    template_name = 'workers/form.html'
    fields = '__all__'
    success_url = reverse_lazy('worker_list')


class WorkerUpdateView(UpdateView):
    model = Worker
    template_name = 'workers/form.html'
    fields = '__all__'
    success_url = reverse_lazy('worker_list')


class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'workers/confirm_delete.html'
    success_url = reverse_lazy('worker_list')


# ========== Performance CRUD ==========
class PerformanceListView(ListView):
    model = Performance
    template_name = 'performances/list.html'
    context_object_name = 'performances'


class PerformanceDetailView(DetailView):
    model = Performance
    template_name = 'performances/detail.html'
    context_object_name = 'performance'


class PerformanceCreateView(CreateView):
    model = Performance
    template_name = 'performances/form.html'
    fields = '__all__'
    success_url = reverse_lazy('performance_list')


class PerformanceUpdateView(UpdateView):
    model = Performance
    template_name = 'performances/form.html'
    fields = '__all__'
    success_url = reverse_lazy('performance_list')


class PerformanceDeleteView(DeleteView):
    model = Performance
    template_name = 'performances/confirm_delete.html'
    success_url = reverse_lazy('performance_list')


# ========== Genre CRUD ==========
class GenreListView(ListView):
    model = Genre
    template_name = 'genres/list.html'
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genres/detail.html'
    context_object_name = 'genre'


class GenreCreateView(CreateView):
    model = Genre
    template_name = 'genres/form.html'
    fields = '__all__'
    success_url = reverse_lazy('genre_list')


class GenreUpdateView(UpdateView):
    model = Genre
    template_name = 'genres/form.html'
    fields = '__all__'
    success_url = reverse_lazy('genre_list')


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'genres/confirm_delete.html'
    success_url = reverse_lazy('genre_list')


# ========== Role CRUD ==========
class RoleListView(ListView):
    model = Role
    template_name = 'roles/list.html'
    context_object_name = 'roles'


class RoleDetailView(DetailView):
    model = Role
    template_name = 'roles/detail.html'
    context_object_name = 'role'


class RoleCreateView(CreateView):
    model = Role
    template_name = 'roles/form.html'
    fields = '__all__'
    success_url = reverse_lazy('role_list')


class RoleUpdateView(UpdateView):
    model = Role
    template_name = 'roles/form.html'
    fields = '__all__'
    success_url = reverse_lazy('role_list')


class RoleDeleteView(DeleteView):
    model = Role
    template_name = 'roles/confirm_delete.html'
    success_url = reverse_lazy('role_list')


# ========== Award CRUD ==========
class AwardListView(ListView):
    model = Award
    template_name = 'awards/list.html'
    context_object_name = 'awards'


class AwardDetailView(DetailView):
    model = Award
    template_name = 'awards/detail.html'
    context_object_name = 'award'


class AwardCreateView(CreateView):
    model = Award
    template_name = 'awards/form.html'
    fields = '__all__'
    success_url = reverse_lazy('award_list')


class AwardUpdateView(UpdateView):
    model = Award
    template_name = 'awards/form.html'
    fields = '__all__'
    success_url = reverse_lazy('award_list')


class AwardDeleteView(DeleteView):
    model = Award
    template_name = 'awards/confirm_delete.html'
    success_url = reverse_lazy('award_list')
