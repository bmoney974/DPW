
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
        b.id = 1
        b.calc_budget()


        #John's Bills
        j = budget()
        j.rent = 500
        j.cell_phone = 60
        j.cable = 75
        j.car_note = 300
        j.food = 100
        j.check = 2500
        j.id = 2
        j.calc_budget()

        #Sara's Bills
        s = budget()
        s.rent = 900
        s.cell_phone = 50
        s.cable = 50
        s.car_note = 0
        s.food = 175
        s.check = 5000
        s.id = 3
        s.calc_budget()

        #"Bobby Has " + "$" + str(b.money_left) + " left to spend for the month"

        p = Page()
        p.title = "My Budget"
        p.css = "css/styles.css"
        p.body = '''
<a href=?user1=Bobby>Bobby's Money Left</a><br />
<a href=?user2=John>John's Money Left</a><br />
<a href=?user3=Sara>Sara's Money Left</a>
        '''

        self.response.write(p.whole_page)

        if self.request.GET:
            user1 = self.request.GET['user1']
            self.response.write("<br />" + user1 + " Has " + "$" + str(b.money_left) + " left to spend for the month")
        elif self.request.GET:
            user2 = self.request.GET['user2']
            self.response.write("<br />" + user2 + " Has " + "$" + str(j.money_left) + " left to spend for the month")
        elif self.request.GET:
            user3 = self.request.GET['user3']
            self.response.write("<br />" + user3 + " Has " + "$" + str(s.money_left) + " left to spend for the month")
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
        #calculate final grade
        self.__money_left = int(self.check - (self.rent + self.cell_phone + self.cable + self.car_note + self.food))





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
