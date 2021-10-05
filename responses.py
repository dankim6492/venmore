from venmo_api import Client, PaymentPrivacy, utils
from datetime import date


def get_access_token():
    username = input('Username: ')
    password = input('Password: ')
    access_token = Client.get_access_token(username, password)
    return access_token


def recurring_payment(client, request_amount, request_note, username_list, Privacy):
    for request_id in username_list:
        client.payment.request_money(amount=request_amount, note=request_note, target_user_id=request_id,
                                     privacy_setting=Privacy)


def get_user_ids(client, user_list):
    user_ids = []
    for user in user_list:
        add_user = client.user.get_user_by_username(username=user)
        user_ids.append(add_user.id)
    return user_ids

# def split_cost_equally(self, client):
