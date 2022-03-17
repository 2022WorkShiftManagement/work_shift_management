import hashlib


# ハッシュ化の関数
def hash(salt, pw):
    b_pw = bytes(pw, 'utf-8')
    b_salt = bytes(salt, 'utf-8')
    hashed_pw = hashlib.pbkdf2_hmac("sha256", b_pw, b_salt, 2560).hex()

    return hashed_pw


# メールのバリデーションチェック
def mail_validation(mail):
    if max_length_validation(mail, 64):
        # TODO 正規表現してね
        return True

    return False


# 名前のバリデーションチェック
def name_validation(name):
    if max_length_validation(name, 32):
        return True

    return False


# パスワードのバリデーションチェック
def pw_validation(pw):
    if min_length_validation(pw, 6):
        # TODO 正規表現してね
        return True

    return False


# 入力文字数のチェック(最大文字)
def max_length_validation(word, cnt):
    return True if cnt >= len(word) > 0 else False


# 入力文字数のチェック(最小文字)
def min_length_validation(word, cnt):
    return True if cnt <= len(word) else False
