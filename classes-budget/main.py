
import webapp2
from pages import Page #from package import class

class MainHandler(webapp2.RequestHandler):
    def get(self):


     #Bobby's Bills
        b = budget()
        b.rent = 655
        b.cell_phone = 100
        b.cable = 60
        b.car_note = 440
        b.food = 150
        b.check = 4500
        b.calc_budget()


        #John's Bills
        j = budget()
        j.rent = 500
        j.cell_phone = 60
        j.cable = 75
        j.car_note = 300
        j.food = 100
        j.check = 2500
        j.calc_budget()

        #Sara's Bills
        s = budget()
        s.rent = 900
        s.cell_phone = 50
        s.cable = 50
        s.car_note = 0
        s.food = 175
        s.check = 5000
        s.calc_budget()

        #Mikes's Bills
        m = budget()
        m.rent = 450
        m.cell_phone = 30
        m.cable = 50
        m.car_note = 250
        m.food = 100
        m.check = 3000
        m.calc_budget()

        #Ashley's Bills
        a = budget()
        a.rent = 700
        a.cell_phone = 60
        a.cable = 50
        a.car_note = 300
        a.food = 125
        a.check = 3500
        a.calc_budget()


        #"Bobby Has " + "$" + str(b.money_left) + " left to spend for the month"

        p = Page()
        p.title = "My Budget"
        p.css = "css/styles.css"
        p.body = '''
<a href=?user=Bobby>Bobby's Money Left</a><br />
<a href=?user=John>John's Money Left</a><br />
<a href=?user=Sara>Sara's Money Left</a></br />
<a href=?user=Mike>Sara's Money Left</a><br />
<a href=?user=Ashley>Ashley's Money Left</a>
        '''

        self.response.write(p.whole_page)

        if self.request.GET and self.request.GET["user"] == "Bobby":
            user = self.request.GET['user']
            self.response.write("<br />" + user + " Has " + "$" + str(b.money_left) + " left to spend for the month")
        elif self.request.GET and self.request.GET["user"] == "John":
            user = self.request.GET['user']
            self.response.write("<br />" + user + " Has " + "$" + str(j.money_left) + " left to spend for the month")
        elif self.request.GET and self.request.GET["user"] == "Sara":
            user = self.request.GET['user']
            self.response.write("<br />" + user + " Has " + "$" + str(s.money_left) + " left to spend for the month")
        elif self.request.GET and self.request.GET["user"] == "Mike":
            user = self.request.GET['user']
            self.response.write("<br />" + user + " Has " + "$" + str(m.money_left) + " left to spend for the month")
        elif self.request.GET and self.request.GET["user"] == "Ashley":
            user = self.request.GET['user']
            self.response.write("<br />" + user + " Has " + "$" + str(a.money_left) + " left to spend for the month")
        else:
            pass












class budget(object):
    def __init__(self):
        self.rent = 0  # no undersocres = public
        self.cell_phone = 0
        self.cable = 0
        self.car_note = 0
        self.food = 0
        self.check = 0
        self.id = 0
        self.__money_left = 0  # two underscores = private
        self.__money_left = int(self.check - (self.rent + self.cell_phone + self.cable + self.car_note + self.food))

    @property
    def money_left(self):

        return self.__money_left

    @money_left.setter
    def money_left(self, new_money_left):
        self.__money_left = new_money_left

    def calc_budget(self):
        #calculate money left
        self.__money_left = int(self.check - (self.rent + self.cell_phone + self.cable + self.car_note + self.food))





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
