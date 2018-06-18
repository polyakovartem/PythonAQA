class SMSContent:

    def __init__(self, text='test sms'):
        if len(text) > 160:
            self.text = text[:160]
        else:
            self.text = text

    def get_sms(self):
        return self.text


class SMSCutter:

    def __init__(self, text, length=160):
        if len(text) > length:
            self.text = text[:length]
        else:
            self.text = text

    def get_text(self):
        return self.text


class SMSSender:

    def __init__(self, text, receivers):
        self.receivers = receivers
        self.text = text

    def send_sms(self):
        for phone in self.receivers:
            print("\"{}\" was sent to {}".format(self.text, phone))


def main():

    sms = SMSContent().get_sms()
    ready_for_sending = SMSCutter(sms).get_text()
    send_sms = SMSSender(ready_for_sending, ['0631234567', '0671234567'])
    send_sms.send_sms()


if __name__ == '__main__':

    main()
