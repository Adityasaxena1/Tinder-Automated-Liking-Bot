from selenium import webdriver
from selenium.webdriver.common.by import By



class Login():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=464891386855067&kid_directed_site=0"
                        "&app_id=464891386855067&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog"
                        "%2Foauth%3Fapp_id%3D464891386855067%26cbt%3D1693579669868%26channel_url%3Dhttps%253A%252F%252Fs"
                        "taticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfca33"
                        "ace80cb%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%2"
                        "5252Ftinder.com%25252Ff1356e158b346dc%2526relation%253Dopener%26client_id%3D464891386855067%26"
                        "display%3Dpopup%26domain%3Dtinder.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A"
                        "%252F%252Ftinder.com%252F%26locale%3Den_US%26logger_id%3Df2762f982fe66%26origin%3D1%26redirec"
                        "t_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fv"
                        "ersion%253D46%2523cb%253Df3b81724331975c%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%252"
                        "6origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff1356e158b346dc%2526relation%253Dopener"
                        "%2526frame%253Df1b6694e9e02db4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26s"
                        "cope%3Duser_birthday%252Cuser_photos%252Cemail%252Cuser_likes%26sdk%3Djoey%26version%3Dv2.8%26"
                        "ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com"
                        "%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3b81724331975c%26domain%3Dtinder.com%26i"
                        "s_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff1356e158b346dc%26relation%3Dop"
                        "ener%26frame%3Df1b6694e9e02db4%26error%3Daccess_denied%26error_code%3D200%26error_description"
                        "%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0")







