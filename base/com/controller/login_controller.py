from flask import render_template, request, redirect, flash
from base.com.dao.login_dao import LoginDAO
from base.com.dao.video_dao import VideoDAO
from base.com.vo import login_vo
from base.com.vo.login_vo import LoginVO
from base import app


@app.route('/')
def login():
    return render_template('admin/login.html')

@app.route('/about')
def about():
    return render_template('admin/about.html')


@app.route('/validate_login', methods=['POST', 'GET'])
def view_login():
    login_username = request.form.get("username")
    login_password = request.form.get("password")

    login_dao = LoginDAO()

    login_vo_list = login_dao.view_login()
    login_list = [i.as_dict() for i in login_vo_list]
    # print('login_list+++++', login_list[1])
    # print('login_list------', login_list[2])
    if login_list[0]['user_name'] == login_username and login_list[0]['password'] == login_password:
        return render_template("admin/index.html")



    else:
        error_message = 'Username or Password is incorrect!!'
        flash(error_message)
        return redirect("/")


@app.route('/index', methods=['POST', 'GET'])
def total_count():
    video_dao = VideoDAO()

    total_count = video_dao.total_count()
    video_list = [i.as_dict() for i in total_count]

    # total entry count
    total_entry_count = []
    for i in video_list:
        count = int(i.get('entry_count'))
        total_entry_count.append(count)
    sum_entry = sum(total_entry_count)

    # total exit count
    total_exit_count = []
    for i in video_list:
        count = int(i.get('exit_count'))
        total_exit_count.append(count)
    sum_exit = sum(total_exit_count)

    print(">>>>>>>>>>>>>>>>>>>>>>>", video_list)

    return render_template('admin/index.html', entry=sum_entry, exit=sum_exit)




