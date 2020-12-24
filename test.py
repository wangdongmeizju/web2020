if __name__=="__main__":
    a='/Users/jingmo/PycharmProjects/web2020/static/download/2020-12-24 11:45:12王冬梅.doc'
    name=a.split('/')[-1]
    filePath=a.replace(name,'')
    print(name)