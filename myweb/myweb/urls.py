from django.conf.urls import url, include
from django.contrib import admin
from sample import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^$',views.sampleIndex),
]

"""
urlpatterns = [
    url(r'^$', 'sample.views.sampleIndex'),
    # url(r'^([a-z]+)/$', 'sample.views.sampleTemp'),
    url(r'^year/(199[0-9]|2[0-9]{3})/$', 'sample.views.sampleYear'),
    url(r'^month/(0[1-9]|1[0-2])/$', 'sample.views.sampleMonth'),
    url(r'^day/([1-9]|[1-2][0-9]|3[0-1])/$', 'sample.views.sampleDay'),
    url(r'^word/((?:[a-z]+-?)+)/$', 'sample.views.sampleWords'),
    url(r'^html/([a-z0-9]+)/$', 'sample.views.sampleHtml'),
    url(r'^input/$', 'sample.views.sampleInput'),
    url(r'^exam/$', 'sample.views.sampleExam'),
]
"""
# 정규표현식
# ^ : 패턴의 시작
# $ : 패턴의 끝
# [a-z] : 소문자 a ~ z 까지 한 자리
# [A-Z] : 대문자 A ~ Z 까지 한 자리
# [a-zA-Z] : 대소문자 a ~ Z 까지 한 자리
# [0-9] : 숫자 0 ~ 9 까지 한 자리
# {n} : n 자리
# {n,m} : n ~ m 자리 까지
# + : 한 자리 이상
# | : or의 의미를 가진다  a|b
# ? : 0 또는 1 자리      [a-z]?
# (표현식) : 표현식을 그룹화 한다, 표현식에 매치가 되는 값을 함수의 인자로 전달
# (?:표현식) : 표현식을 그룹화 한다, 함수의 인자로 전달하지 않는다.