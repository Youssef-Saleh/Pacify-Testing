from base.selenium_driver import SeleniumDriver
import time

class LikedPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.Driver =driver

    Likedsongs = "Liked Songs"
    Libray = "Library"
    Song1 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div"
    Song2 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div"
    Song3 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div"
    Song4 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[4]/div"
    Song5 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[5]/div"
    Song6 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[6]/div"
    Song7 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[7]/div"
    Song8 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[8]/div"
    Song9 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[9]/div"
    Song10 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[10]/div"
    Song11 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[11]/div"
    Song12 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[12]/div"
    Song13 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[13]/div"
    Song14 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[14]/div"
    Song15 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[15]/div"
    Song16 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[16]/div"
    Song17 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[17]/div"
    Song18 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[18]/div"
    Song19 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[19]/div"
    Song20 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[20]/div"
    Song21 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[21]/div"
    Song22 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[22]/div"
    Song23 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[23]/div"
    Song24 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[24]/div"
    Song25 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[25]/div"
    Song26 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[26]/div"
    Song27 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[27]/div"
    Song28 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[28]/div"
    Song29 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[29]/div"
    Song30 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[30]/div"
    Song31 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[31]/div"
    Song32 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[32]/div"
    Song33 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[33]/div"
    Song34 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[34]/div"
    Song35 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[35]/div"
    Song36 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[36]/div"
    Song37 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[37]/div"
    Song38 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[38]/div"
    Song39 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[39]/div"
    Song40 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[40]/div"
    Song41 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[41]/div"
    Song42 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[42]/div"
    Song43 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[43]/div"
    Song44 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[44]/div"
    Song45 = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[45]/div"
    Loginlink = "Login"  # link text
    EmailField = "email"  # name
    PasswordField = "password"  # name
    LoginButton = "/html/body/div/div/div[2]/div[5]/form/div[5]/button"  # xpath
    BarButton = "/html/body/div/div/div/nav/div[2]/div/div[2]/div[2]/button[2]"


    def EnterEmail(self, email):
        self.SendKeys(email, self.EmailField, "name")

    def EnterPassword(self, password):
        self.SendKeys(password, self.PasswordField, "name")

    def ClickLoginButton(self):
        self.ElementClick(self.LoginButton, "xpath")

    def ClickLoginLink(self):
         self.ElementClick(self.Loginlink, "link")

    def click_Song1(self):
        self.ElementClick(self.Song1, "xpath")

    def click_Song2(self):
        self.ElementClick(self.Song2, "xpath")

    def click_Song3(self):
        self.ElementClick(self.Song3, "xpath")

    def click_Song4(self):
        self.ElementClick(self.Song4, "xpath")

    def click_Song5(self):
        self.ElementClick(self.Song5, "xpath")

    def click_Song6(self):
        self.ElementClick(self.Song6, "xpath")

    def click_Song7(self):
        self.ElementClick(self.Song7, "xpath")

    def click_Song8(self):
        self.ElementClick(self.Song8, "xpath")

    def click_Song9(self):
        self.ElementClick(self.Song9, "xpath")

    def click_Song10(self):
        self.ElementClick(self.Song10, "xpath")

    def click_Song11(self):
        self.ElementClick(self.Song11, "xpath")

    def click_Song12(self):
        self.ElementClick(self.Song12, "xpath")

    def click_Song13(self):
        self.ElementClick(self.Song13, "xpath")

    def click_Song14(self):
        self.ElementClick(self.Song14, "xpath")

    def click_Song15(self):
        self.ElementClick(self.Song15, "xpath")

    def click_Song16(self):
        self.ElementClick(self.Song16, "xpath")

    def click_Song17(self):
        self.ElementClick(self.Song17, "xpath")

    def click_Song18(self):
        self.ElementClick(self.Song18, "xpath")

    def click_Song19(self):
        self.ElementClick(self.Song19, "xpath")

    def click_Song20(self):
        self.ElementClick(self.Song20, "xpath")

    def click_Song21(self):
        self.ElementClick(self.Song21, "xpath")
    def click_Song22(self):
        self.ElementClick(self.Song22, "xpath")
    def click_Song23(self):
        self.ElementClick(self.Song23, "xpath")
    def click_Song24(self):
        self.ElementClick(self.Song24, "xpath")
    def click_Song25(self):
        self.ElementClick(self.Song25, "xpath")
    def click_Song26(self):
        self.ElementClick(self.Song26, "xpath")
    def click_Song27(self):
        self.ElementClick(self.Song27, "xpath")
    def click_Song28(self):
        self.ElementClick(self.Song28, "xpath")
    def click_Song29(self):
        self.ElementClick(self.Song29, "xpath")
    def click_Song30(self):
        self.ElementClick(self.Song30, "xpath")
    def click_Song31(self):
        self.ElementClick(self.Song31, "xpath")
    def click_Song32(self):
        self.ElementClick(self.Song32, "xpath")
    def click_Song33(self):
        self.ElementClick(self.Song33, "xpath")
    def click_Song34(self):
        self.ElementClick(self.Song34, "xpath")

    def click_Song35(self):
        self.ElementClick(self.Song35, "xpath")

    def click_Song36(self):
        self.ElementClick(self.Song36, "xpath")

    def click_Song37(self):
        self.ElementClick(self.Song37, "xpath")

    def click_Song38(self):
        self.ElementClick(self.Song38, "xpath")

    def click_Song39(self):
        self.ElementClick(self.Song39, "xpath")

    def click_Song40(self):
        self.ElementClick(self.Song40, "xpath")

    def click_Song41(self):
        self.ElementClick(self.Song41, "xpath")

    def click_Song42(self):
        self.ElementClick(self.Song42, "xpath")

    def click_Song43(self):
        self.ElementClick(self.Song43, "xpath")

    def click_Song44(self):
        self.ElementClick(self.Song44, "xpath")

    def click_Song45(self):
        self.ElementClick(self.Song45, "xpath")


    def ClickBarbutton(self):
        self.ElementClick(self.BarButton, "xpath")

    def ClickLikeSongs(self):
        self.ElementClick(self.Likedsongs, "link")

    def ClickLibrary(self):
        self.ElementClick(self.Libray, "link")


    def LikedLogin(self, username, password):
        self.ClickLoginLink()
        self.Driver.implicitly_wait(5)
        self.EnterEmail(username)
        self.EnterPassword(password)
        self.ClickLoginButton()
        time.sleep(2)
        self.ClickLikeSongs()

    def Stress1(self, username, password):
        self.ClickLoginLink()
        self.Driver.implicitly_wait(5)
        self.EnterEmail(username)
        self.EnterPassword(password)
        self.ClickLoginButton()
        time.sleep(2)
        self.ClickLikeSongs()
        i=0
        while(i<500):
            self.click_Song1()
            time.sleep(0.5)
            self.click_Song2()
            time.sleep(0.5)
            self.click_Song3()
            time.sleep(0.5)
            i = i + 1

    def Stress2(self, username, password):
        self.ClickLoginLink()
        self.Driver.implicitly_wait(5)
        self.EnterEmail(username)
        self.EnterPassword(password)
        self.ClickLoginButton()
        time.sleep(2)
        self.ClickLikeSongs()
        self.click_Song1()
        i = 0
        while(i<100):
            self.ClickBarbutton()
            i = i + 1
    def Stress3(self, username, password):
        self.ClickLoginLink()
        self.Driver.implicitly_wait(5)
        self.EnterEmail(username)
        self.EnterPassword(password)
        self.ClickLoginButton()
        time.sleep(2)
        self.ClickLikeSongs()
        i = 0
        while(i<4000):
            self.ClickLibrary()
            self.ClickLikeSongs()
            i = i + 1

