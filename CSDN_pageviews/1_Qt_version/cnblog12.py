import sys
import time

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time

class WebView(QWebEngineView):
    def __init__(self):
        super(WebView, self).__init__()
        url = 'https://blog.csdn.net/qq_44847636/article/details/113741948'
        self.load(QUrl(url))
        self.show()
        QTimer.singleShot(1000 * 3, self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    web = WebView()
    print('### exec succeed !')
    sys.exit(app.exec_())