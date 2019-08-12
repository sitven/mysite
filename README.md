### 2019-07-24 搭建Django环境<br>
启动本地服务：python36 manage.py runserver<br>
同步数据库文件： python36 manage.py migrate<br>
创建超级管理员：python36 manage.py createsuperuser<br>
### 2019-07-26 Django基本应用结构介绍<br>
创建一个article应用： python36 manage.py startapp article<br> 
mysite》article<br>
      》admin.py<br>
      》apps.py<br>
      》models.py   模型<br>
        settings.py   全局设置文件<br>
      》tests.py<br>
      》views.py<br>
使用模版显示内容、添加模板，添加博客列表<br>
添加子路由，主路由包含子路由（总urls包含app中的urls）<br>
### 2019-07-28 定制后台和修改模型<br>
定制admin后台：设置模型__str__  定制admin<br>
修改模型更新数据库<br>
            python36 manage.py makemigrations           # 生成数据库迁移文件<br>
            python36 manage.py migrate                  # 应用<br>
### 2019-07-31 虚拟环境运行django项目<br>
pip install virtualenv 虚拟环境<br>
创建虚拟环境： virtualenv <mysite_env><br>
启动虚拟环境： Scripts\activate<br>
退出虚拟环境： deactivate<br>
创建博客项目： django-admin startproject mysite<br>
创建博客应用： python manage.py startapp blog<br>
初始化数据库：python36 manage.py migrate<br>
创建超级管理员：python36 manage.py createsuperuser<br>
创造迁移文件：python36 manage.py makemigrations<br>
应用： python36 manage.py migrate<br>
启动本地服务：python36 manage.py runserver<br>
一键导出：pip freeze > requirements.txt<br>
一键安装：pip install -r requirements.txt<br>
### 2019-08-05 新增模板标签和过滤器<br>
博客内容新增显示标签时间作者等信息<br>
博客标签分类首页等添加跳转信息<br>
过滤器和字符截取的使用<br>
模板嵌套与通用模板引用(base.html)<br>
通过css美化首页,设置css文件全局变量<br>

# 学习与持续更新中...

### 2019-08-08  引入bootstrap-3.3.7框架，CSS协助前端布局<br>
引入bootstrap-3.3.7框架， file => static/bootstrap-3.3.7<br>
引入jquery-1.12.4.min.js 和 优化导航栏样式与大小格局<br>
### 2019-08-09 Bootstrap响应式布局<br>
1.博客列表新增博客分类与模板得引用, 通过css对模板和列表响应式布局，屏幕分辨率自适应<br>
2.博客内容页优化标签、间距和内容缩进等<br>
### 2019-08-10 博客列表添加分页器与新增博客归档模块并优化views中重复代码<br>
1.博客列表分页与添加分页器<br>
2.页面分页组件居中, 添加首尾页与当前页之间添加...按钮并删除点击响应,同步更新博客分类页<br>
3.博客列表页面添加博客归档模块,年月归档<br>
4.优化views中重复代码,新增通用方法放置通用模板<br>
### 2019-08-11 博客分类统计与博客后台添加富文本编辑器<br>
1.对博客列表的博客分类与日期归档模块添加博客数量统计<br>
2.对博客后台添加富文本编辑器,对富文本编辑器新增图片本地上传功能<br>
### 2019-08-12 博客阅读简单计数<br>
1.博客阅读简单计数,通过设置cookie控制统计数量
2.博客阅读计数优化 ==> 阅读统计字段(ReadNum)单独显示(未完)