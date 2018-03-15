#VUE+Django => 个人blog
###环境：
        VUE==2.5
        Django==2.0
        djangotramework==3.7
        PyMySQL==0.8

###开始：
####【后端】：
    新建一个项目: <code>django-admin startproject backend</code>
    创建APP: <code>cd backend</code>
             <code>django-admin startapp blog</code>
    配置sitting：
            --如果要把多个app放到一个文件夹apps，则要添加如下代码--
           <code>import sys
             BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
             sys.path.insert(0,os.path.join(BASE_DIR,'apps'))</code>

            ---INSTALLED_APPS ---
            'blog',
            'rest_framework', --》api框架，配合django食用
            'corsheaders', --》跨域

                      ------MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'corsheaders.middleware.CorsMiddleware',  --》跨域
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',]

                      ----DATABASES = {
                        'default': {
                            'ENGINE': 'django.db.backends.mysql',
                            'NAME': '数据库名称',
                            'USER': '数据库服务器名称',
                            'PASSWORD': '数据库密码',
                            'HOST': 'localhost',
                            'PORT': '3306',
                        }
                    }
            中文设置：
            LANGUAGE_CODE = 'zh-hans'
            TIME_ZONE = 'Asia/Shanghai'     
            跨域：
            CORS_ORIGIN_ALLOW_ALL = True
     配置pymysql，在backend->backend下的__init__.py：
            import pymysql
            pymysql.install_as_MySQLdb()   
    配置超级用户：
        python manage.py createsuperuser


#####建立数据库模型
    限制函数传入的关键字参数
    通过使用**kwargs，在函数中配合使用kwargs.pop(key, False)实现获取限制关键字参数值，如果未传入则设置默认值，当所有需要的关键字参数都pop完毕，如果kwargs还有其它内容则raise ValueError.
    
    django 排序通常采用如下方式：
      1.使用QuerySet的order_by指定查询排序
            modelname.objects.filter('updated_time')  #ASC 升序
            modelname.objects.filter('-updated_time')  #DESC 降序

       2.在model定义的class Meta添加属性：
             class Meta: 
                ordering = ['-updated_time']
    通常在需要排序的model中添加ordering属性，在特定在查询中需要改变排序再使用QuerySet order_by

    File "C:\Python\lib\site-packages\django\urls\conf.py", line 39, in include
    'Specifying a namespace in include() without providing an app_name '
    -》在app下面的urls.py 内添加app_name

    You are trying to add a non-nullable field 'pub_date' to article without a default; we can't do that (the database needs something to populate existing rows).
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows)
     2) Quit, and let me add a default in models.py
    这段话的意思是 pub_date 字段没有默认值，而且非Null 那么 
    1) 指定一个一次性的值供更改数据库时使用。
    2) 停止当前操作，在 models.py 中给定默认值，然后再来migrate。
    我们选择第一个，输入 1
    Select an option: 1
    Please enter the default value now, as valid Python
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now()
    >>> timezone.now()
    Migrations for 'news':
      0002_auto_20150728_1232.py:
        - Add field pub_date to article
        - Add field update_time to article
    这样是生成了一个对表进行更改的 py 文件在 news/migrations 文件夹中，我们要执行更改
    1
    python manage.py migrate