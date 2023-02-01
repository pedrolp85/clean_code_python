class Communication:
    def send_notification():
        pass


class SMSCommunication(Communication):
    def send_notification():
        pass
        # do something!


class EmailCommunication(Communication):
    def send_notification():
        pass
        # do something!


class SlackCommunication(Communication):
    def send_notification():
        pass
        # do something!


class PhoneCommunication(Communication):
    def send_notification():
        pass
        # do something!


def get_communication(is_important=False):
    return SMSCommunication() if is_important else EmailCommunication()


# factoria normal


class BankAccountCommunication:
    def add_money(self):
        pass

    def substract_money(self):
        pass


# factoria abastracta


class NormalBankAccountCommunication(BankAccountCommunication):
    communication: Communication = get_communication(is_important=True)

    def add_money(self):
        self.communication.send_notification()

    def substract_money(self):
        self.communication.send_notification()


class PremiumBankAccountCommunication(NormalBankAccountCommunication):
    def substract_money(self):
        SMSCommunication().send_notification()


class CryptoBroBankAccountCommunication(NormalBankAccountCommunication):
    communication = SlackCommunication()


def get_bank_client_communication(client):
    if client.cryto_bro:
        return CryptoBroBankAccountCommunication()
    return PremiumBankAccountCommunication() if client.premium else NormalBankAccountCommunication()
    # factoria normal


class BankAccount:
    def __init__(self, client):
        self.communication = get_bank_client_communication(client)

    def add_money(self):
        pass
        self.communication.add_money()

    def substract_money(self):
        pass
        self.communication.substract_money()


class AccoutSettings:
    communication: Communication = get_communication(is_important=True)

    def edit_profile(self):
        pass
        self.communication.send_notification()
