from PageObject.Objects.BasePage import BasePage

class TeachOnlinePage(BasePage):

    def url(self):
        return super(TeachOnlinePage, self).url() + '/teaching/?ref=teach_header'
