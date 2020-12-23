from flask import  Flask,render_template,request, current_app, send_from_directory,make_response
import doc_wenting
from datetime import timedelta
import os

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
download_fils_path=os.getcwd()+'/static/download'
# download_file_list = os.listdir(download_fils_path)

@app.route('/banzheng')
def banzheng():
    return render_template("banzheng.html")

@app.route('/banzhengProcess',methods=['POST','GET'])
def banzhengProcess():
    if request.method=='POST':
        nm=request.form['nm']     #获取姓名文本框的输入值
        files=doc_wenting.process(nm,download_fils_path)
        if files=="success":
            return render_template("success.html")
        else:
            return files



@app.route('/download')
def index():
    download_file_list = os.listdir(download_fils_path)
    download_file_list.sort(reverse=True)
    res = make_response(render_template("download.html",file_list=download_file_list))
    res.headers["Cache-Control"] = "no_store"
    res.headers["max-age"] = 1
    # return render_template("download.html",file_list=download_file_list)
    return res

@app.route("/downloading/<filename>")
def downloading(filename):
    res = make_response(send_from_directory(download_fils_path, filename))
    res.headers["Cache-Control"] = "no_store"
    res.headers["max-age"] = 1
    return res
    # return send_from_directory(download_fils_path, filename)


if __name__=="__main__":
    app.run(port=2020,host="0.0.0.0",debug=False)
