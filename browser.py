import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class NoHistoryWebEngineHistory(QWebEngineHistory):
    def addHistoryEntry(self, item):
        pass

class NoHistoryWebEngineProfile(QWebEngineProfile):
    def history(self):
        return NoHistoryWebEngineHistory(self)

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dewsverse Private Browser")
        self.resize(1134, 702)
        # Set the window icon
        self.setWindowIcon(QIcon("./media/logo.jpeg"))
        # Create a custom web engine profile without history tracking
        self.profile = NoHistoryWebEngineProfile()
        def add_new_tab():
            self.add_tab("https://superurl.pythonanywhere.com/0c31Yx")

        # Create a tab widget to hold multiple tabs
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_widget.currentChanged.connect(self.switch_tab)
        self.tab_widget.tabBar().setTabButton(0, QTabBar.RightSide, QToolButton(self.tab_widget.tabBar(), text="+", clicked=add_new_tab))

        self.add_tab("https://superurl.pythonanywhere.com/0c31Yx")

        # Create the address bar
        # self.address_bar = QLineEdit()
        # self.address_bar.returnPressed.connect(self.load_page)

        # Create a layout for the address bar and tab widget
        layout = QVBoxLayout()
        # layout.addWidget(self.address_bar)
        layout.addWidget(self.tab_widget)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_tab(self, url="https://superurl.pythonanywhere.com/0c31Yx"):
        # Create a new web view for the tab
        web_view = QWebEngineView()
        web_view.setPage(QWebEnginePage(self.profile, web_view))
        if url:
            web_view.load(QUrl(url))

        # Add the web view to a new tab in the tab widget
        self.tab_widget.addTab(web_view, "New Tab")
        self.tab_widget.setCurrentWidget(web_view)

    def close_tab(self, index):
        # Close the tab at the given index, except for the last tab
        if index >= 0 and self.tab_widget.count() > 1:
            self.tab_widget.widget(index).deleteLater()
            self.tab_widget.removeTab(index)


    def switch_tab(self, index):
        # Update the address bar when switching tabs
        if index >= 0:
            current_web_view = self.tab_widget.widget(index)
            current_url = current_web_view.page().url().toString()
            # self.address_bar.setText(current_url)

    def load_page(self):
        url = self.address_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        current_web_view = self.tab_widget.currentWidget()
        current_web_view.load(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = BrowserWindow()
    browser.show()
    sys.exit(app.exec_())
