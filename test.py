
from docx import Document
from docxcompose.composer import Composer

def hebing(files,final_docx):
    new_document = Document()
    composer = Composer(new_document)
    for index, fn in enumerate(files):
        sub_doc=Document(fn)
        if index < len(files)-1:
           sub_doc.add_page_break()
        composer.append(sub_doc)
    composer.save(final_docx)

if __name__ == "__main__":
    dir="/Users/jingmo/PycharmProjects/web2020/static/download"
    a1=dir+"/"+"2020-12-14 13:29:21赵文婷2.doc"
    a2=dir+"/"+"2020-12-14 13:29:21赵文婷1.doc"
    res=dir+"/"+"2020-12-14 13:29:21赵文婷.doc"
    hebing([a1,a2],res)