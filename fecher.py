import urllib2
from BeautifulSoup import BeautifulSoup


class Fecher(object):

    def __init__(self):
        pass

    def set_header(self, url):
        pass

    def get(self):
        pass

    def post():
        pass

    def get_htmlpage(self):
        pass

    @classmethod
    def wget(self, url):
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        data = resp.read()

        return data

if __name__ == '__main__':
    data = Fecher.wget('http://weibo.com/liuyanghoho/home')

    import pdb
    pdb.set_trace()
    soup = BeautifulSoup(data, fromEncoding='unicode');
    for i in soup.head:
        print i
        print '\n'
