from web.base.selenium_driver import SeleniumDriver
import logging
import web.utilities.custom_logger as cl

class CreatePlaylist(SeleniumDriver):

    Log = cl.customLogger(logging.DEBUG)

    def __init__(self, Driver):
        self.Driver=Driver
    #Locators
    Playlist="/html/body/div/div/div/div[1]/div[2]/div/div[1]/div/span"
    Create="/html/body/div[3]/div/div/div/div/div/div[3]/div[2]/button"
    Cancel="/html/body/div[3]/div/div/div/div/div/div[3]/div[1]/button"
    NameOfPlaylist="input-holder"
    WindowClick="/html/body/div[3]"
    Exit="/html/body/div[3]/div/div/div/div/div/div[1]/button/svg"
    Library="/html/body/div/div/div/div[1]/div[1]/div[3]/a/div"
    def ClickWindow(self):
        self.ElementClick(self.WindowClick,"xpath")
    def ClickLibrary(self):
        self.ElementClick(self.Library,"xpath")
    def ClickCreatePlaylist(self):
        self.ElementClick(self.Playlist, "xpath")
    def NamingPlaylist(self,Name):
        self.SendKeys(Name, self.NameOfPlaylist, "id")
        return Name
    def Create_Playlist(self):
        self.ElementClick(self.Create, "xpath")
    def CancelCreatingPlaylist(self):
        self.ElementClick(self.Cancel, "xpath")
    def VerifyPlaylistMadeSuccesfull(self,Name):
        result=self.IsElementPresent(Name,"link")
        return result
    def VerifyPlaylistMadeFailed(self,Name):
        result = self.IsElementPresent(Name, "link")
        return not result

