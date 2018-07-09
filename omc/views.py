from django.shortcuts import render, redirect, reverse
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
# 登入登出相关函数
def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登录了')
                    return redirect(reverse('index', args=[]))
                else:
                    messages.add_message(request, messages.WARNING, '账号尚未启用')
            else:
                messages.add_message(request, messages.WARNING, '登录失败')
        else:
            messages.add_message(request, messages.INFO, '请检查输入的字段内容')
    else:
        form = forms.LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "成功注销了")
    return render(request, 'accounts/logged_out.html')


# 功能模块相关函数
def index(request):
    return render(request,
                  'functions/index.html')


def us_ui_elements(request):
    return render(request,
                  'functions/ui-elements.html')


def us_chart(request):
    return render(request,
                  'functions/chart.html')


def us_tab_panel(request):
    return render(request,
                  'functions/tab-panel.html')


def us_table(request):
    return render(request,
                  'functions/table.html')


def us_form(request):
    return render(request,
                  'functions/form.html')


def empty(request):
    test = request.path
    return render(request,
                  'functions/empty.html',
                  locals())
