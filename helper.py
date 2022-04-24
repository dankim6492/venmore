from venmo_api import Client, PaymentPrivacy

class Venmo:
    
    def __init__(self, access_token):
        self.client = Client(access_token)

    def recurring_payment(self, request_amount, request_note, username_list, Privacy=PaymentPrivacy.PRIVATE):
        for request_id in username_list:
            self.client.payment.request_money(request_amount, request_note, request_id, Privacy)

    def get_user_ids(self, user_list):
        user_ids = [self.client.user.get_user_by_username(username=user).id for user in user_list]
        return user_ids
