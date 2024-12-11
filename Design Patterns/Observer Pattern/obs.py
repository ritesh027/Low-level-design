from abc import ABC, abstractmethod


class notificationAlertObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class emailAlertObserver(notificationAlertObserver):
    
    def __init__(self, email, observable: stockObservable):
        self.email = email
        self.observable = observable
    
    def sendmail(email):
        print(f"mail send to: {email}")
    
    def update(self):
        sendmail(self.email)


class mobileAlertObserver(notificationAlertObserver):
    
    def __init__(self, username, observable: stockObservable):
        self.username = username
        self.observable = observable
    
    def sendmail(username):
        print(f"mail send to: {username}")
    
    def update(self):
        sendmail(self.username)

