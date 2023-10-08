import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\Admin\\PycharmProjects\\nopsush.py\\Configuration\\Config.ini")

class Readconfig:
    @staticmethod
    def getUrl():
        url=config.get("Common Info","baseUrl")
        return url

    @staticmethod
    def getuserEmail():
        email=config.get("Common Info","userName")
        return email

    @staticmethod
    def getpassword():
        passw=config.get("Common Info","passWord")
        return passw