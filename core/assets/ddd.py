import markdown,codecs

with codecs.open("help2.md",'r',encoding="utf-8")as a :
    html=markdown.markdown(a.read(),extensions=['markdown.extensions.fenced_code','markdown.extensions.tables',])
with open("aaa.html",'w',encoding="utf-8")as b:
    b.write(html)