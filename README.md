# in2game
Django-4.0.6
gunicorn-20.1.0
djangorestframework-3.13.1
django_cors_headers-3.13.0
django-filter-22.1

npm install -g @vue/cli
vue create in2game
 > vue 2
vue add vuetify
vue add axios
vue add router

npm install @mdi/font -D
npm install @mdi/js -D
npm install vue-float-menu -D

# node version update
node -v             # node version 확인
npm cache clean -f  # clear npm cache
npm install -g n    # Node.js 버전을 관리할 수 있는 n이라는 모듈을 설치합니다.
n stable            # n 모듈을 사용해 node.js 를 설치합니다.



npm run serve
manage.py collectstatic
manage.py runserver
 > gunicorn --bind 0:18080 in2game.wsgi:application --timeout 60

nginx
brew services start nginx
brew services stop nginx
brew services restart nginx

lintOnSave: false, 