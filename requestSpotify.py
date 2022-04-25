import os
from datetime import date
from venmo_api import PaymentPrivacy
from dotenv import load_dotenv
from helper import Venmo

def get_month():
    today = date.today()
    return today.strftime("%B")

def generate_env_list(friends_num):
    env_var_list = ["ACCESS_TOKEN"]
    for num in range(1, friends_num+1):
        env_var_list.append("FRIEND_{}".format(num))

    return env_var_list

def get_env_val(env_var_list):

    acess_token = os.getenv(env_var_list[0])
    usernames = map(lambda var: os.getenv(var), env_var_list[1:])
    
    return access_token, usernames

if __name__ == "__main__":

    # --- Grab env variables
    load_dotenv()
    env_var_list = generate_env_list(5)
    access_token, friend_username_list = get_env_val(env_var_list)

    # --- Initialize Venmo client
    venmore = Venmo(access_token)

    # --- Send recurring_payment request
    friend_id_list = venmore.get_user_ids(friend_username_list)
    charge_note = "{} - Spotify Family".format(get_month())
    venmore.recurring_payment(2.67, charge_note, friend_id_list, PaymentPrivacy.PRIVATE)