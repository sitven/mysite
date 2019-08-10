# 第二课 搭建Django环境<br>
启动本地服务：python36 manage.py runserver<br>
同步数据库文件： python36 manage.py migrate<br>
创建超级管理员：python36 manage.py createsuperuser<br>
账号：lwj      
密码：django123456
邮箱为空<br>
mysite》mysite<br>
        settings.py   全局设置文件<br>
#
# 第三课 Django基本应用结构<br>
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
#
# 第五课 定制后台和修改模型<br>
定制admin后台：设置模型__str__  定制admin<br>
修改模型更新数据库<br>
            python36 manage.py makemigrations           # 生成数据库迁移文件<br>
            python36 manage.py migrate                  # 应用<br>
<br>
#
# 第7课 虚拟环境运行django项目<br>
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
#
# 第8课 常用的模版标签和过滤器<br>
博客内容新增显示标签时间作者等信息<br>
博客标签分类首页等添加跳转信息<br>
过滤器和字符截取的使用<br>
#
# 第9课 模板嵌套<br>
模板嵌套与通用模板引用(base.html)<br>
#
# 第10课<br>
通过css美化首页,设置css文件全局变量<br>
#
# 第11课 CSS框架协助前端布局<br>
引入bootstrap-3.3.7框架， file => static/bootstrap-3.3.7<br>
引入jquery-1.12.4.min.js 和 优化导航栏样式与大小格局<br>
#
# 第12课 Bootstrap响应式布局<br>
1.博客列表新增博客分类与模板得引用, 通过css对模板和列表响应式布局，屏幕分辨率自适应<br>
2.博客内容页优化标签、间距和内容缩进等<br>
#
# 第13课 分页器<br>
博客列表分页与添加分页器<br>
#
# 第14课 优化分页显示<br>
页面分页组件居中, 添加首尾页与当前页之间添加...按钮并删除点击响应,同步更新博客分类页<br>
#
# 第15课 上下篇博客和按月分类<br>
博客列表页面添加博客分档模块,年月归档<br>
优化views中重复代码,新增通用方法放置通用模板<br>
#
# 第16课 博客分类统计<br>
