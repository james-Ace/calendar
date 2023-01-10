from lib import app


@app.route('/admin/login')
def a_login():
    ''' 登录 '''
    return 'Hello user!'


@app.route('/admin/index')
def a_index():
    ''' 后台首页 '''
    return 'Hello user!'


@app.route('/admin/posts')
def a_posts():
    ''' 后台文章页 '''
    return 'Hello user!'


@app.route('/admin/index')
def hello_user():
    ''' 后台文章页 '''
    return 'Hello user!'


@app.route('/admin/index')
def hello_user():
    return 'Hello user!'
