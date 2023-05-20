# Django

ReDjango

DJANGO기본 시작을 위한 순서

1. 마음을 단단히 먹고 폴더 생성하기!
2. 터미널에서 가상환경 만들기 - > “python -m venv 가상환경명”
3. 가상환경 실행 -> source 가상환경명/Scripts/activate
4. 장고 설치 -> “pip install django” //이미지 필드도 사용하려면 , pip install pillow
5. 프로젝트 생성 -> “django-admin startproject 프로젝트명 .” 
6. 서버 실행해보기 -> “python [manage.py](http://manage.py/) runserver” 
7. 앱 생성 -> “python [manage.py](http://manage.py/) startapp ‘앱명’” 
8. 앱 폴더 안에 ‘templates’ 폴더 생성한 후, ‘###.html’ 파일 생성
9. 프로젝트 폴더 안 ‘[settings.py](http://settings.py/)’에 앱 존재 알려주기 INSATLLED_APPS = [ ‘djangoapp’ ,]
