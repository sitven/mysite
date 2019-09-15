#### 2019-07-24 搭建Django环境<br>
启动本地服务：python36 manage.py runserver<br>
同步数据库文件： python36 manage.py migrate<br>
创建超级管理员：python36 manage.py createsuperuser<br>
#### 2019-07-26 Django基本应用结构介绍<br>
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
#### 2019-07-28 定制后台和修改模型<br>
定制admin后台：设置模型__str__  定制admin<br>
修改模型更新数据库<br>
            python36 manage.py makemigrations           # 生成数据库迁移文件<br>
            python36 manage.py migrate                  # 应用<br>
### 2019-07-31 虚拟环境运行django项目<br>
pip install virtualenv 虚拟环境<br>
pip install django-ckeditor 安装依赖包<br>
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
#### 2019-08-05 新增模板标签和过滤器<br>
博客内容新增显示标签时间作者等信息<br>
博客标签分类首页等添加跳转信息<br>
过滤器和字符截取的使用<br>
模板嵌套与通用模板引用(base.html)<br>
通过css美化首页,设置css文件全局变量<br>

# 学习与持续更新中...

#### 2019-08-08  引入bootstrap-3.3.7框架，CSS协助前端布局<br>
引入bootstrap-3.3.7框架， file => static/bootstrap-3.3.7<br>
引入jquery-1.12.4.min.js 和 优化导航栏样式与大小格局<br>
#### 2019-08-09 Bootstrap响应式布局<br>
1.博客列表新增博客分类与模板得引用, 通过css对模板和列表响应式布局，屏幕分辨率自适应<br>
2.博客内容页优化标签、间距和内容缩进等<br>
#### 2019-08-10 博客列表添加分页器与新增博客归档模块并优化views中重复代码<br>
1.博客列表分页与添加分页器<br>
2.页面分页组件居中, 添加首尾页与当前页之间添加...按钮并删除点击响应,同步更新博客分类页<br>
3.博客列表页面添加博客归档模块,年月归档<br>
4.优化views中重复代码,新增通用方法放置通用模板<br>
#### 2019-08-11 博客分类统计与博客后台添加富文本编辑器<br>
1.对博客列表的博客分类与日期归档模块添加博客数量统计<br>
2.对博客后台添加富文本编辑器,对富文本编辑器新增图片本地上传功能<br>
#### 2019-08-12 博客阅读简单计数<br>
1.博客阅读简单计数,通过设置cookie控制统计数量<br>
2.博客阅读计数优化 ==> 阅读统计字段(ReadNum)单独显示<br>
#### 2019-08-13 博客阅读计数优化<br>
优化计数统计,解决后台编辑博客影响数据的问题<br>
#### 2019-08-14 阅读计数统计和显示<br>
1.每日阅读添加阅读计数统计，优化阅读统计代码<br>
2.每日阅读统计通过线型图显示与首页, 调整首页文案位置<br>
#### 2019-08-15 热门阅读博客排行及缓存提速<br>
1.添加今天、昨天和7天热门博客<br>
2.设置7天热门博客过期时间为3600缓存<br>
创建缓存表：python manage.py createcachetable<br>
#### 2019-08-20 评论功能设计和用户登录<br>
1.创建评论库：python manage.py startapp comment<br>
2.新增评论功能,设置评论门槛,评论增加登录方法<br>
#### 2019-08-21 html表单提交评论<br>
1.添加评论(评论对象、内容、时间和作者)<br>
2.无权限评论或者登录异常跳转error.html页并设置返回按钮<br>
#### 2019-08-27 使用Django Form表单<br>
1.优化登录成功跳转回博客<br>
2.新增注册功能能,注册用户名、邮箱和密码验证<br>
3.登录or注册功能引用面板优化显示、博客页登录or注册按钮colour等优化<br>
#### 2019-08-28 富文本编辑和ajax提交评论<br>
1.评论框使用富文本编辑器<br>
2.评论内容通过ajax提交数据<br>
3.更正日期过滤器,切换时区为亚洲-上海<br>
#### 2019-08-29 回复功能设计和树结构<br>
1.添加回复功能与回复设置树状结构<br>
2.设置评论倒叙与设置回复评论正序显示<br>
#### 2019-08-30 获取评论数和细节处理<br>
1.解决回复评论内容显示NaN刷新正常问题<br>
2.优化评论时间显示格式与异步优化<br>
3.添加博客页与博客列表获取方法评论数<br>
#### 2019-09-03 实现点赞与未登录点赞登录功能<br>
1.实现博客点赞与取消点赞功能<br>
2,实现评论与回复实现点赞与取消点赞功能<br>
3.博客点赞统计于博客列表<br>
4.完善未登录点赞跳转登录&修复评论与回复不能立即点赞功能<br>
#### 2019-09-04 导航栏添加用户操作<br>
1.导航栏右侧添加"登录/注册"或用户信息功能<br>
2.添加用户绑定邮箱与昵称和修改等功能<br>
3.模板全局变量<br>
#### 2019-09-10 自定义用户模型与修复登录注册无法跳转回首页bug<br>
1.自定义用户模型<br>
2.修复登录页与注册页叠层状态登录后跳到注册页情况,修复跳转回首页<br>
#### 2019-09-14 新增用户信息修改、邮箱绑定和登录，密码重置等功能<br>
1.新增用户信息编辑-用户昵称修改功能<br>
2.添加用户账号绑定邮箱功能,授权发送邮件账号,添加验证邮箱验证码等功能<br>
3.添加邮箱注册、邮箱登录功能与密码重置功能<br>
#### 2019-09-15 增加评论邮箱通知功能<br>
1.增加评论邮箱通知博主功能<br>
2.解决发送html邮件显示html标签bug<br>