from lib import db
import datetime


class User(db.Model):
    __tablename__ = 'user'
    '''
    用户表
    '''
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    nickname = db.Column(db.String(50))
    password = db.Column(db.String(255))
    email = db.Column(db.String(50))
    birthday = db.Column(db.DateTime)
    address = db.Column(db.String(500))
    sex = db.Column(db.String(10))
    authority = db.Column(db.String(60))
    Picture = db.Column(db.String(160))
    register_date = db.Column(db.DateTime, default=datetime.datetime.now)
    user_freezeState = db.Column(db.Integer(), default=1)
    user_freezeday = db.Column(db.DateTime)
    user_freezeinfo = db.Column(db.String(180))
    art_user = db.Column(db.String(180))
    art_id = db.relationship('Article',uselist=False,backref='user')

 
class Article(db.Model):
    __tablename__ = 'article'
    '''
        id                  文章的id
        art_title           文章的标题
        art_type            文章的类型 [1:图文 2:照片 3:视频]
        art_content         文章内容
        art_add_time        文章发布时间
        art_cat             文章分类
        arg_info            文章描述
        art_count           文章阅读统计
        art_from            文章来源，0:原创 1:转载
        art_tag             文章标签
        art_support         文章赞数
        art_commint_count   文章留言数
        art_status          文章状态[0:正常 1:推荐 2:置顶]
        
    '''
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    art_title = db.Column(db.String(50))
    art_content = db.Column(db.Text)
    art_add_time = db.Column(db.DateTime, default=datetime.datetime.now)
    arg_info = db.Column(db.String(260))
    art_count = db.Column(db.Integer())
    art_from = db.Column(db.Integer())
    art_tag = db.Column(db.String(200))
    art_support = db.Column(db.Integer())
    art_commint_count = db.Column(db.Integer())
    art_status = db.Column(db.Integer())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    cat_name = db.Column(db.Integer,db.ForeignKey('category.id'))


class Apps(db.Model):
    __tablename__ = 'apps'

    id = db.Column(db.Integer(), primary_key=True,  autoincrement=True)
    app_name = db.Column(db.String(50))
    field_name = db.Column(db.String(255))
    field_value = db.Column(db.String(60))
    add_date = db.Column(db.DateTime, default=datetime.datetime.now)


class Category(db.Model):
    __tablename__ = 'category'
    '''
        id         分类ID
        category_name       分类名称
        alias_name          分类别名
        description         分类描述
        parennt_id          父级id
        create_time         创建时间
        seo_title           SEO标题
        seo_keywords        SEO关键字
        seo_description     SEO描述
        category_type       分类类型
    '''
    id = db.Column(db.Integer(),  autoincrement=True, primary_key=True)
    category_name = db.Column(db.String(50), unique=True)
    alias_name = db.Column(db.String(50))
    description = db.Column(db.String(128))
    parennt_id = db.Column(db.Integer())
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    seo_title = db.Column(db.String(80))
    seo_keywords = db.Column(db.String(80))
    seo_description = db.Column(db.String(200))
    category_type = db.Column(db.String(80))
    # 关联字段
    category_name = db.relationship('Article', backref='category', lazy='dynamic')
    


class Models(db.Model):
    __tablename__ = 'models'
    '''
        id                  模型ID
        name                模型名称
        alias_name          模型别名
        description         模型描述
        create_time         创建时间
    '''
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    alias_name = db.Column(db.String(50))
    model_type = db.Column(db.String(50))
    description = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)



class Links(db.Model):
    __tablename__ = 'links'
    '''
        id                  链接ID
        name                链接名称
        alias_name          链接别名
        description         链接描述
        create_time         创建时间
        Picture             链接图片
        nofollow            是否开启nofollow [0:不添加, 1:添加]
        target              链接打开方式 [0:新窗口, 1:当前窗口]
    '''
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    alias_name = db.Column(db.String(50))
    url = db.Column(db.String(50))
    description = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    Picture = db.Column(db.String(128))
    nofollow = db.Column(db.Integer()) 
    target  = db.Column(db.Integer())
    
class Options(db.Model):
    __tablename__ = 'options'
    
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    value = db.Column(db.String(255))