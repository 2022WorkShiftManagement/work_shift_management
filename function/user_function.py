import hashlib
import re


# ハッシュ化の関数
def hash(salt, pw):
    b_pw = bytes(pw, 'utf-8')
    b_salt = bytes(salt, 'utf-8')
    hashed_pw = hashlib.pbkdf2_hmac("sha256", b_pw, b_salt, 2560).hex()

    return hashed_pw


# メールのバリデーションチェック
def mail_validation(mail):
    # 64文字以内の時True
    if max_length_validation(mail, 64):
        # 文字列＠文字列.文字列の時True
        mail_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(mail_pattern, mail):
            return True

    return False


# 名前のバリデーションチェック
def name_validation(name):
    if max_length_validation(name, 32):
        name_pattern = '^( * |　*$)'
        if not re.search(name_pattern, name):
            return True

    return False


# パスワードのバリデーションチェック
def pw_validation(pw):
    if min_length_validation(pw, 6):
        pw_pattern = r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]'
        if re.search(pw_pattern, pw):
            return True

    return False


# 入力文字数のチェック(最大文字)
def max_length_validation(word, cnt):
    if cnt >= len(word) > 0 and word:
        return True
    return False


# 入力文字数のチェック(最小文字)
def min_length_validation(word, cnt):
    if cnt <= len(word) and word:
        return True
    return False
