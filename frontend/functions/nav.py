class Nav :
    def  __init__(self):
        page = None
        currentUser = 0
        currentClient = 0

    def goTo(self, view) :
        self.page = view

    def getPage(self) :
        return self.page

    def setCurrentUser(self, user) :
        self.currentUser = user

    def setCurrentClient(self, client) :
        self.currentUser = client

nav = Nav()