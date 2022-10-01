from googlesearch import search


def pdfsearch(keyword):
    name=keyword
# to search
    query = name+" filetype:xls"
    print(query)
    ar = [] 
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        ar.append(j)
    return ar

ar=pdfsearch("python")
