# MVC模式
# controller层

from flask import Flask, render_template, flash, request, abort, redirect, url_for, session
# from models import User
# 导入数据库操作工具类
from mysqlUtils import MysqlUtils
# 导入json包
import json

# MVC模式model层
from models.readerModel import readerModel
from models.recordModel import recordModel
from models.bookModel import bookModel

util = MysqlUtils('localhost', 'root', '55555y', 'library', 'utf8')
# 所有书籍信息
# u=util.query_all_book()

app = Flask(__name__)
app.secret_key = '123'  # flash加密


@app.route('/')
def hello_world():
    flash("")  # 登陆注册提示信息
    content = "hello world"
    # return render_template("login.html", content=content)
    return render_template("login.html", content=content)


# 注册
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        form = request.form
        username = form.get('username')
        password = form.get('password')
        password2 = form.get('password2')
        # 前端完成判断内容是否为空
        if not username:
            flash("请输入用户名")
            return render_template("register.html")
        if not password:
            flash("请输入密码")
            return render_template("register.html")
        if not password2:
            flash("请输入确认密码")
            return render_template("register.html")
        if not password == password2:
            flash("两次密码不一致")
            return render_template("register.html")
        else:  # 注册信息无误，写入数据库
            util.register_Admin(username, password)
            flash("注册成功")
            return render_template("register.html")
    else:
        return render_template("register.html")


# 登录界面路由
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        form = request.form
        username = form.get('username') + ""
        password = form.get('password') + ""
        if not username:
            flash("请输入用户名")
            return render_template("login.html", password=password)
        if not password:
            flash("请输入密码")
            return render_template("login.html", username=username)
        password2 = util.query_Password(username)  # 根据账号查询的密码
        if (password == password2):
            return render_template("addbook.html")
        else:
            flash("用户名或密码错误")
            return render_template("login.html", username=username, password=password)
    else:  # 请求方式为GET时
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    flash("您已成功退出登录")
    return redirect(url_for('login'))

# MVC模式代码重构
# 增加书籍界面
@app.route('/addbook', methods=['POST', 'GET'])
def addbook():
    if request.method == "POST":
        form = request.form
        number = form.get('number') + ""
        name = form.get('bookname') + ""
        author = form.get('author') + ""
        publicationdate = form.get('pdate') + ""
        location = form.get('address') + ""
        remark = form.get('description') + ""
        isborrow = form.get('isborrow', 0)  # 获取isborrow值，默认为0
        if not number:
            flash("请输入id")
            return render_template("addbook.html", number=number)
        if not name:
            flash("请输入书名")
            return render_template("addbook.html", number=number, name=name)
        if not location:
            flash("请输入位置")
            return render_template("addbook.html", number=number, name=name, location=location)
        m = bookModel()
        m.add_book(number, name, author, publicationdate, location, remark)

        flash("添加图书成功")
        return render_template("addbook.html")
    else:
        return render_template("addbook.html")


# 删除书籍界面
@app.route('/deletebook', methods=['GET', 'POST'])
def deletebook():
    # u = util.query_all_book()
    # MVC模式重构
    m = bookModel()
    books = m.get_all_book_data()
    return render_template("deletebook.html", books=books)


# 负责删除书籍的路由 带参数：书籍名称
@app.route('/deletebook2/<bookid>', methods=['GET'])
def deletebook2(bookid):
    # 先删除所选书籍后查询
    # util.delete_book(bookid)
    # u = util.query_all_book()
    # MVC模式重构
    m = bookModel()
    m.delete_one_book_by_id(bookid)
    books = m.get_all_book_data()
    flash(bookid)
    return render_template("deletebook.html", books=books)



# 修改书籍界面
@app.route('/changebook', methods=['POST', 'GET'])
def changebook():
    # u = util.query_all_book()
    # MVC模式重构
    m = bookModel()
    books = m.get_all_book_data()
    return render_template("changebook.html", books=books)


# 修改书籍界面 详细界面
@app.route('/changebookinfor/<bookid>', methods=['POST', 'GET'])
def changebookinfor(bookid):
    detail = util.query_one_book_byid(bookid)
    if request.method == "POST":
        form = request.form  # 若点击修改 则先删除 后添加
        number = form.get('number') + ""
        name = form.get('bookname') + ""
        author = form.get('author') + ""
        publicationdate = form.get('pdate') + ""
        location = form.get('address') + ""
        remark = form.get('description') + ""
        if not number:
            flash("请输入id")
            return render_template("changebookinfor.html")
        if not name:
            flash("请输入书名")
            return render_template("changebookinfor.html", number=number)
        if not location:
            flash("请输入位置")
            return render_template("changebookinfor.html", number=number, name=name)
        util.delete_book(bookid)
        util.add_book(number, name, author, publicationdate, location, remark)
        flash("修改图书成功")
        return render_template("changebookinfor.html", detail=detail)
    else:
        return render_template("changebookinfor.html", detail=detail)


# 查询界面
@app.route('/querybook', methods=['POST', 'GET'])
def querybook():
    # u = util.query_all_book()
    # MVC模式重构
    m = bookModel()
    books = m.get_all_book_data()
    if request.method == "POST":
        name = request.values.get('bookname')
        # onebook=util.query_one_book(name)
        # MVC模式重构
        onebook = m.get_one_book_data(name)
        return render_template("querybook.html", books=onebook, name=name)
    else:
        return render_template("querybook.html", books=books)


# 图书借阅信息界面
@app.route('/borrowrecord', methods=['POST', 'GET'])
def borrowrecord():
    # u = util.query_borrowrecord()
    # MVC模式重构
    m = recordModel()
    records = m.get_record_data()
    return render_template("borrowrecord.html", records=records)


# 读者信息信息界面
@app.route('/readerinfor', methods=['POST', 'GET'])
def readerinfor():
    # u = util.query_readerinfor()
    # MVC模式重构
    m = readerModel()
    readers = m.get_reader_data()
    return render_template("readerinfor.html", readers=readers)


# 错误界面（异常处理）
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)
