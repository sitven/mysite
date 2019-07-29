# 第二课<br>
启动本地服务：python36 manage.py runserver<br>
同步数据库文件： python36 manage.py migrate<br>
创建超级管理员：python36 manage.py createsuperuser<br>
账号：lwj      
密码：django123456
邮箱为空<br>
mysite》mysite<br>
        settings.py   全局设置文件<br>

# 第三课<br>
创建一个article应用： python36 manage.py startapp article<br>  
mysite》article<br>
      》admin.py<br>
      》apps.py<br>
      》models.py   模型<br>
      》tests.py<br>
      》views.py<br>
<br>
第四课<br>
使用模版显示内容<br>
添加模板<br>
添加博客列表<br>
添加子路由，主路由包含子路由（总urls包含app中的urls）<br>
<br>
# 第五课<br>
定制admin后台：设置模型__str__  定制admin<br>
修改模型更新数据库<br>
            python36 manage.py makemigrations           # 生成数据库迁移文件<br>
            python36 manage.py migrate                  # 应用<br>
<br>
# 第7课<br>
pip install virtualenv 虚拟环境<br>
创建虚拟环境： virtualenv <mysite_env><br>
启动虚拟环境： Scripts\activate<br>
退出虚拟环境： deactivate<br>
创建博客项目： django-admin startproject mysite<br>
创建博客应用： python manage.py startapp blog<br>
初始化数据库：python36 manage.py migrate<br>
创建超级管理员：python36 manage.py createsuperuser<br>
账号：lwj      
密码：django123456
<br>
创造迁移文件：python36 manage.py makemigrations<br>
应用： python36 manage.py migrate<br>
启动本地服务：python36 manage.py runserver<br>
<br>
一键导出：pip freeze > requirements.txt<br>
一键安装：pip install -r requirements.txt<br>
# 第8课<br>
博客内容新增显示标签时间作者等信息<br>
博客标签分类首页等添加跳转信息<br>
过滤器和字符截取的使用<br>
# 第9课<br>
模板嵌套与通用模板引用(base.html)<br>
# 第10课<br>
通过css美化首页,设置css文件全局变量<br>
# 第11课<br>
