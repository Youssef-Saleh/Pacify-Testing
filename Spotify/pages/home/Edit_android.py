from base.appium_driver import AppiumDriver
import time

class Edit_Android(AppiumDriver):
    def __init__(self , driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    Loginlink = "com.example.pacify:id/login_button"
    emailfield = "com.example.pacify:id/Email_logIn_text"
    passwordfield = "com.example.pacify:id/password_login_editText"
    loginbutton = "com.example.pacify:id/login_button"
    yourLibrary = "com.example.pacify:id/nav_favorites"
    settings = "com.example.pacify:id/logout_button"
    edit = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout"
    back = "android:id/icon"
    change_email_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout"
    change_password_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout"
    change_country_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout"
    change_phone_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.RelativeLayout"
    change_gender_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.RelativeLayout"
    change_date_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[8]/android.widget.RelativeLayout"
    new_email = "com.example.pacify:id/edit_email_New_Email_text"
    change_email = "com.example.pacify:id/edit_email_confirm_button"
    change_mind = "com.example.pacify:id/edit_email_go_back_button"
    done = "com.example.pacify:id/edit_email_go_back_button"
    current = "com.example.pacify:id/edit_password_old_password_text"
    new_password = "com.example.pacify:id/edit_password_new_password_text"
    repeat = "com.example.pacify:id/edit_password_new_password_text_again"
    confirm_password = "com.example.pacify:id/edit_password_confirm_button"
    change_mind_password = "com.example.pacify:id/edit_password_go_back_button"
    done_password = "com.example.pacify:id/edit_password_go_back_button"
    country_field= "com.example.pacify:id/edit_country_name_text"
    confirm_change_country = "com.example.pacify:id/edit_country_confirm_button"
    change_mind_country = "com.example.pacify:id/edit_country_go_back_button"
    done_country = "com.example.pacify:id/edit_country_go_back_button"
    phone_field = "com.example.pacify:id/edit_phone_number_text"
    confirm_change_phone = "com.example.pacify:id/edit_phone_number_confirm_button"
    change_mind_phone = "com.example.pacify:id/edit_phone_number_go_back_button"
    done_phone = "com.example.pacify:id/edit_phone_number_go_back_button"
    change_mind_gender = "com.example.pacify:id/edit_gender_go_back_button"
    Male = "com.example.pacify:id/male_button"
    Female = "com.example.pacify:id/female_button"
    day = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[2]/android.widget.EditText"
    month = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[1]/android.widget.EditText"
    year = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[3]/android.widget.EditText"
    change_my_dob = "com.example.pacify:id/edit_Dob_confirm_button"
    change_mind_date = "com.example.pacify:id/edit_dob_go_back_button"
    Like = "com.example.pacify:id/likeButton"
    pause = "com.example.pacify:id/playPauseBarButton"
    song = "com.example.pacify:id/songName"

    def entereamil(self, email):
         self.sendKeys(email, self.emailfield)

    def enterpassword(self,password):
         self.sendKeys(password, self.passwordfield)

    def enterday(self, day):
         self.sendKeys(day, self.day)

    def entermonth(self, month):
         self.sendKeys(month, self.month)

    def enteryear(self, year):
         self.sendKeys(year, self.passwordfield)

    def enter_new_email(self, email):
         self.sendKeys(email, self.new_email)

    def enter_new_password(self, password):
        self.sendKeys(password, self.new_password)

    def enter_reprat_password(self, password):
        self.sendKeys(password, self.repeat)

    def enter_current_password(self, password):
        self.sendKeys(password, self.current)

    def enter_country(self, data):
         self.sendKeys(data, self.country_field)

    def enter_phone(self, data):
        self.sendKeys(data, self.phone_field)

    def click_done(self):
         self.elementClick(self.done)

    def click_like(self):
         self.elementClick(self.Like)

    def click_pause(self):
         self.elementClick(self.pause)

    def click_song(self):
         self.elementClick(self.song)

    def click_done_password(self):
         self.elementClick(self.done_password)

    def click_done_phone(self):
         self.elementClick(self.done_phone)

    def clickloginbutton(self):
         self.elementClick(self.loginbutton)

    def clickloginlink(self):
         self.elementClick(self.Loginlink)

    def clicklibrary(self):
        self.elementClick(self.yourLibrary)

    def clicksettings(self):
        self.elementClick(self.settings)

    def click_edit(self):
        self.elementClick(self.edit, "xpath")

    def clickback(self):
        self.elementClick(self.back)

    def click_confirm_passsword(self):
        self.elementClick(self.confirm_password)

    def click_confirm_country(self):
        self.elementClick(self.confirm_change_country)

    def click_confirm_phone(self):
        self.elementClick(self.confirm_change_phone)

    def click_dob(self):
        self.elementClick(self.change_my_dob)

    def click_change_email_button(self):
        self.elementClick(self.change_email_button, "xpath")

    def click_change_password_button(self):
        self.elementClick(self.change_password_button, "xpath")

    def click_change_country_button(self):
        self.elementClick(self.change_country_button, "xpath")

    def click_change_phone_button(self):
        self.elementClick(self.change_phone_button, "xpath")

    def click_change_gender_button(self):
        self.elementClick(self.change_gender_button, "xpath")

    def click_change_date_button(self):
        self.elementClick(self.change_date_button, "xpath")

    def change_email_confirm(self):
        self.elementClick(self.change_email)

    def click_change_mind(self):
        self.elementClick(self.change_mind)

    def click_change_mind_password(self):
        self.elementClick(self.change_mind_password)

    def click_change_mind_country(self):
        self.elementClick(self.change_mind_country)

    def click_change_mind_phone(self):
        self.elementClick(self.change_mind_phone)

    def click_change_mind_gender(self):
        self.elementClick(self.change_mind_gender)

    def click_change_mind_date(self):
        self.elementClick(self.change_mind_date)

    def click_male(self):
        self.elementClick(self.Male)

    def click_female(self):
        self.elementClick(self.Female)

    def click_day(self):
        self.elementClick(self.day)

    def click_month(self):
        self.elementClick(self.month)

    def click_year(self):
        self.elementClick(self.year)

    def  click_done_country(self):
        self.elementClick(self.done_country)

    def clear_new_mail(self):
        self.clears(self.new_email)

    def clear_country(self):
        self.clears(self.country_field)

    def clear_phone(self):
        self.clears(self.phone_field)

    def clear_current_password(self):
        self.clears(self.current)

    def clear_new_password(self):
        self.clears(self.new_password)

    def clear_repeat_password(self):
        self.clears(self.repeat)

    def login_edit(self, email, password):
        self.clickloginlink()
        self.driver.implicitly_wait(2)
        self.entereamil(email)
        self.enterpassword(password)
        self.clickloginbutton()
        self.driver.implicitly_wait(2)
        self.clicklibrary()
        self.clicksettings()
        self.click_edit()


    def edit_email_with_change_mind(self):
        self.clickback()
        self.click_edit()
        self.click_change_email_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind()

    def edit_email_without_button(self, email):
        self.clear_new_mail()
        self.enter_new_email(email)

    def edit_email_with_button(self, email):
        self.clear_new_mail()
        self.enter_new_email(email)
        self.change_email_confirm()
        self.click_done()


    def edit_password_with_change_mind(self):
        self.clickback()
        self.click_edit()
        self.click_change_password_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind_password()

    def edit_password_with_change_mind_full(self):
        # self.clickback()
        self.click_edit()
        self.click_change_password_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind_password()

    def edit_password_without_button(self, current, password, newpassword):
        self.clear_current_password()
        self.clear_new_password()
        self.clear_repeat_password()
        self.enter_current_password(current)
        self.enter_new_password(password)
        self.enter_reprat_password(newpassword)

    def edit_password_with_button(self, current, password, newpassword):
        self.clear_current_password()
        self.clear_new_password()
        self.clear_repeat_password()
        self.enter_current_password(current)
        self.enter_new_password(password)
        self.enter_reprat_password(newpassword)
        self.click_confirm_passsword()
        self.click_done_password()

    def edit_country_with_change_mind(self):
        self.clickback()
        self.click_edit()
        self.click_change_country_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind_country()

    def edit_country_with_change_mind_full(self):
        self.click_edit()
        self.click_change_country_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind_country()

    def edit_country_without_done(self, data):
        self.clear_country()
        self.enter_country(data)
        self.click_confirm_country()

    def edit_country_with_done(self, data):
        self.clear_country()
        self.enter_country(data)
        self.click_confirm_country()
        self.click_done_country()

    def edit_phone_with_change_mind(self):
        self.clickback()
        self.click_edit()
        self.driver.implicitly_wait(4)
        self.click_change_phone_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind_phone()

    def edit_phone_with_change_mind_full(self):
        # self.clickback()
        self.click_edit()
        self.driver.implicitly_wait(4)
        self.click_change_phone_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind_phone()

    def edit_phone_without_done(self, data):
        self.driver.implicitly_wait(4)
        self.clear_phone()
        self.enter_phone(data)

    def edit_phone_with_done(self, data):
        self.clear_phone()
        self.enter_phone(data)
        self.click_confirm_phone()
        self.click_done_phone()

    def edit_gender_with_change_mind(self):
        self.clickback()
        self.click_edit()
        self.driver.implicitly_wait(4)
        self.click_change_gender_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind_gender()

    def edit_gender_with_change_mind_full(self):
        # self.clickback()
        self.click_edit()
        self.driver.implicitly_wait(4)
        self.click_change_gender_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind_gender()

    def edit_gender_Male(self):
        self.click_edit()
        self.driver.implicitly_wait(4)
        self.click_change_gender_button()
        self.driver.implicitly_wait(4)
        self.click_male()

    def edit_gender_Female(self):
        # self.click_edit()
        # self.driver.implicitly_wait(4)
        # self.click_change_gender_button()
        # self.driver.implicitly_wait(4)
        self.click_female()

    def edit_date_with_change_mind(self):
        self.clickback()
        self.click_edit()
        self.driver.implicitly_wait(4)
        self.click_change_date_button()
        self.driver.implicitly_wait(4)
        self.click_change_mind_date()

    def edit_date(self, day, moth, year):
        self.click_day()
        self.enterday(day)
        self.click_month()
        self.entermonth(day)
        self.click_year()
        self.enteryear(day)

    def edit_date_done(self, day, moth, year):
        self.driver.implicitly_wait(5)
        self.click_day()
        self.enterday(day)
        self.click_month()
        self.entermonth(day)
        self.click_year()
        self.enteryear(day)
        self.click_dob()

