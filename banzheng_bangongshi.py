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
        tijiaoren=request.form['tijiaoren']
        nm=request.form['nm']     #获取姓名文本框的输入值
        flag,file_wang=doc_wenting.process(nm,download_fils_path,tijiaoren)
        if flag=="success":
            name=file_wang.split('/')[-1]
            filePath=file_wang.replace(name,'')
            res = make_response(send_from_directory(filePath,name))
            res.headers["Cache-Control"] = "no_store"
            res.headers["max-age"] = 1
            return res
        else:
            return render_template("chongxintianxie.html",error=flag)


if __name__=="__main__":
    app.run(port=2020,host="0.0.0.0",debug=True)
