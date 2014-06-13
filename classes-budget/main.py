
import webapp2
from pages import Page #from package import class

class MainHandler(webapp2.RequestHandler):
    def get(self):


     #Bobby's Bills
        b = budget()
        b.rent = 500
        b.cell_phone = 100
        b.cable = 75
        b.car_note = 300
        b.food = 100
        b.calc_budget()

        cash_left = "Bobby Has " + "$" + str(b.money_left) + " left to spend for the month"

        p = Page()
        p.title = "My Budget"
        p.css = "css/styles.css"
        p.body = '''
<a href=?money=cash_left>ShowMoney</a>
        '''

        self.response.write(p.whole_page)

        if self.request.GET:
            money = self.request.GET['money']
            self.response.write(money)


class budget(object):
    def __init__(self):
        self.rent = 0  # no undersocres = public
        self.cell_phone = 0
        self.cable = 0
        self.car_note = 0
        self.food = 0
        self.__money_left = 0  # two underscores = private
        self.__money_left = 1300 - int((self.rent + self.cell_phone + self.cable + self.car_note + self.food))

    @property
    def money_left(self):

        return self.__money_left

    @money_left.setter
    def money_left(self, new_money_left):
        self.__money_left = new_money_left

    def calc_budget(self):
        #calculate final grade
        self.__money_left = 1300 - int((self.rent + self.cell_phone + self.cable + self.car_note + self.food))





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
