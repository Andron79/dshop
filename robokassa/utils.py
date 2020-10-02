import hashlib

from django.shortcuts import redirect

from dip import settings


def get_payment_url(inv_id, out_summ, inv_desc):
    """
    :param inv_id: order id
    :param out_summ: order cost
    :param inv_desc: order description
    :return: robokassa payment url
    """
    if settings.ROBOKASSA_TEST_PAY:
        is_test = 1
    else:
        is_test = 0
    mrh_login = settings.ROBOKASSA_LOGIN
    mrh_pass1 = settings.ROBOKASSA_PASSWORD1
    hash_string = f'{mrh_login}:{out_summ}:{inv_id}:{mrh_pass1}'
    sign_hash = hashlib.md5(hash_string.encode())
    crc = sign_hash.hexdigest()
    url = f'{settings.ROBOKASSA_URL}' \
          f'MrchLogin={mrh_login}' \
          f'&OutSum={out_summ}' \
          f'&InvId={inv_id}' \
          f'&Desc={inv_desc}' \
          f'&IsTest={is_test}' \
          f'&SignatureValue={crc}'
    return url


# print(get_payment_url(677, 500, "Оплата подписки Wingo Plan"))


