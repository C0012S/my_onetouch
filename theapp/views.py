from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math

# Create your views here.
def index(requests):
    return render(requests, 'index.html')

def error(requests):
    return render(requests, '404.html')

def blank(requests):
    return render(requests, 'blank.html')

def buttons(requests):
    return render(requests, 'buttons.html')

def cards(requests):
    return render(requests, 'cards.html')

def charts(requests):
    return render(requests, 'charts.html')

def password(requests):
    return render(requests, 'forgot-password.html')

def login(requests):
    return render(requests, 'login.html')

def register(requests):
    return render(requests, 'register.html')

def tables(requests):
    return render(requests, 'tables.html')

def animation(requests):
    return render(requests, 'utilities-animation.html')

def border(requests):
    return render(requests, 'utilities-border.html')

def color(requests):
    return render(requests, 'utilities-color.html')

def other(requests):
    return render(requests, 'utilities-other.html')

# 마이 페이지
def mypage(requests):
    return render(requests, 'mypage.html')

# 공지사항
def notice(requests):
    notice = Notice.objects
    return render(requests, 'notice.html',{'notice':notice})

# 공지사항 내용
def notice_content(requests,pk):
    notice = get_object_or_404(Notice,pk=pk)
    return render(requests, 'notice_content.html',{'notice':notice})

# 투표에 관한 건의사항
def suggest_vote(requests):
    sgvote = SuggestVote.objects
    return render(requests, 'suggest_vote.html',{'sgvote':sgvote})


# 기타 건의사항
def suggest_other(requests):
    sgother = SuggestOther.objects
    return render(requests, 'suggest_other.html',{'sgother':sgother})

# 투표 건의사항 내용
def suggest_vote_content(requests,pk):
    sgvote = get_object_or_404(SuggestVote,pk=pk)
    return render(requests, 'suggest_vote_content.html',{'sgvote':sgvote}) 

# 기타 건의사항 내용
def suggest_other_content(requests,pk):
    sgother = get_object_or_404(SuggestOther,pk=pk)
    return render(requests, 'suggest_other_content.html',{'sgother':sgother})           

 #건의사항 작성 투표
def new_suggest_vote(requests):
    return render(requests, 'new_suggest_vote.html')   

 #건의사항 작성 기타
def new_suggest_other(requests):
    return render(requests, 'new_suggest_other.html')     

# 메인 페이지
def main(requests):
    return render(requests, 'main.html')

# 참여 가능한 투표 페이지
def participate(requests):
    return render(requests, 'participating-vote.html')

#참여 가능한 투표 페이지 -학교
def participate_school(requests):
    return render(requests, 'participating-vote_school.html')

#참여 가능한 투표 페이지 -학부
def participate_college(requests):
    return render(requests, 'participating-vote_college.html')   

#참여 가능한 투표 페이지 -학고
def participate_dept(requests):
    return render(requests, 'participating-vote_dept.html')       

# 참여 완료한 투표 페이지
def completion_participate(requests):
    return render(requests, 'completion-participating.html')

# 참여 완료한 투표 페이지-학교
def completion_participate_school(requests):
    return render(requests, 'completion-participating_school.html')

# 참여 완료한 투표 페이지-학부
def completion_participate_college(requests):
    return render(requests, 'completion-participating_college.html')

# 참여 완료한 투표 페이지-학과
def completion_participate_dept(requests):
    return render(requests, 'completion-participating_dept.html')

# 학교 투표 페이지
def school_vote(requests):
    return render(requests,'school_vote.html')

# 단과대/학부 투표 페이지
def college_vote(requests):
    return render(requests, 'college_vote.html')

# 학과 투표 페이지
def department_vote(requests):
    dept_vote = MajorVote.objects
    return render(requests, 'department_vote.html',{'dept_vote':dept_vote})

# 투표 만들기 페이지
def make_vote(requests):
    return render(requests, 'make_vote.html')

# 학교-투표하기 페이지
def school_voting(requests):
    return render(requests, 'school-voting.html')

# 학교-공약 페이지
def school_pledge(requests):
    return render(requests, 'school-pledge.html')

# 학부-투표하기 페이지
def college_voting(requests):
    return render(requests, 'college-voting.html')

# 학부-공약 페이지
def college_pledge(requests):
    return render(requests, 'college-pledge.html')

# 학과-투표하기 페이지
def department_voting(requests, pk):
    dept_vote = get_object_or_404(MajorVote,pk=pk)
    return render(requests, 'department-voting.html',{'dept_vote':dept_vote})

# 학과-공약 페이지
def department_pledge(requests):
    return render(requests, 'department-pledge.html')

# 투표 결과 페이지
def result(requests):
    return render(requests, 'vote_result.html')

# 새로 만든 로그인 페이지
def login_new(requests):
    return render(requests, 'login_new.html')

#주석