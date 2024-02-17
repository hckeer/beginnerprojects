import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #SetNavBar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)
        forward_button = QAction('forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)
        reload_button = QAction('reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)


        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())






app = QApplication(sys.argv)
QApplication.setApplicationName('My own Brower which consumes less ram')
window = Mainwindow()
app.exec_()