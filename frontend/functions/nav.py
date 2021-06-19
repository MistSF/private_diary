class Nav :
    
    def  __init__(self):
        self.page = None
        self.url = "http://localhost:8000"
        self.currentUser = 0
        self.currentClient = 0
        self.currentText = 0

    def goTo(self, view) :
        self.page = view

    def getPage(self) :
        return self.page

    def setCurrentUser(self, user) :
        self.currentUser = user
        print("current user : {}".format(self.currentUser))

    def setCurrentClient(self, client) :
        self.currentClient = client
        print("current client : {}".format(self.currentClient))

    def setCurrentText(self, text) :
        self.currentText = text

    def getCurrentText(self) :
        return self.currentText

    def getCurrentUser(self) :
        return self.currentUser

    def getCurrentClient(self) :
        return self.currentClient

    def getUrl(self) :
        return self.url

nav = Nav()