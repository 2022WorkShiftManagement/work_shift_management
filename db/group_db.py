from db.connect_db import *
from function.random_string import randomstring
def create_group(uid, group_name):
    random_string = randomstring(16)
    conn = get_update_connection()
    cur = conn.cursor()
    # グループの作成
    sql = "INSERT INTO user_groups(user_id, group_name, group_string) VALUES(%s,%s,%s)"
    # グループへの参加
    sql2 = '''INSERT INTO joining_groups(user_id, group_id)
                VALUES (%s,
                    (SELECT group_id FROM user_groups
                    WHERE group_string = %s
                ));'''
    try:
        cur.execute(sql, (uid, group_name, random_string,))
        cur.execute(sql2, (uid, random_string,))
        conn.commit()
        cur.close()
        conn.close()
        return random_string
    except MySQLdb.Error as e:
        cur.close()
        conn.close()
        return None


def select_group(gid):
    check_existence_group()
    conn = get_select_connection()
    cur = conn.cursor()
    sql = '''SELECT jg.user_id, user_name, jg.group_id, ug.user_id as group_reader, group_name, group_string FROM joining_groups as jg
            INNER JOIN users as us ON us.user_id = jg.user_id
            INNER JOIN user_groups as ug ON ug.group_id = jg.group_id
            WHERE us.delete_flg=0 AND ug.group_string=%s'''
    try:
        cur.execute(sql, (gid,))
        group_details = cur.fetchall()
        cur.close()
        conn.close()
        return group_details
    except MySQLdb.Error as e:
        cur.close()
        conn.close()
        return None


def entry_group_confirmation(uid, gid):
    conn = get_select_connection()
    cur = conn.cursor()
    sql = '''SELECT COUNT(*) FROM joining_groups
            WHERE user_id = %s AND group_id = (
                SELECT group_id from user_groups 
                WHERE group_string = %s)
            '''
    try:
        cur.execute(sql, (uid, gid))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return False if result[0][0] == 0 else True
    except MySQLdb.Error as e:
        cur.close()
        conn.close()
        return None


def select_member_count(gid):
    check_existence_group()
    conn = get_select_connection()
    cur = conn.cursor()
    sql = '''SELECT COUNT(*) FROM joining_groups
            WHERE group_id = (
                SELECT group_id FROM user_groups
                WHERE group_string = %s)
            '''
    try:
        cur.execute(sql, (gid,))
        result = cur.fetchone()
        if result[0] == 0:
            delete_group_db(gid)
        cur.close()
        conn.close()
        return result
    except MySQLdb.Error as e:
        cur.close()
        conn.close()
        return None


def join_group(uid, gid):
    conn = get_update_connection()
    cur = conn.cursor()
    sql = '''INSERT INTO joining_groups
            VALUES(null, %s, (
                SELECT group_id FROM user_groups
                WHERE group_string = %s
            ))'''
    try:
        cur.execute(sql, (uid, gid,))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error as e:
        cur.close()
        conn.close()
        return False


def remove_member(uid, gid):
    check_existence_group()
    conn = get_update_connection()
    cur = conn.cursor()
    sql = '''DELETE FROM joining_groups
                WHERE user_id=%s
                AND user_id!=(
                SELECT user_id FROM user_groups
                    WHERE group_string=%s) 
                AND group_id=(
                SELECT group_id FROM user_groups
                    WHERE group_string=%s)'''
    try:
        cur.execute(sql, (uid, gid, gid,))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error as e:
        cur.close()
        conn.close()
        return False


def delete_group_db(gid):
    conn = get_update_connection()
    cur = conn.cursor()
    sql = 'DELETE FROM user_groups WHERE group_string=%s'
    try:
        cur.execute(sql, (gid,))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error as e:
        cur.close()
        conn.close()
        return False


def update_group(gid, gname):
    conn = get_update_connection()
    cur = conn.cursor()
    sql = 'UPDATE user_groups SET group_name=%s WHERE group_string=%s'
    try:
        cur.execute(sql, (gname, gid,))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error as e:
        cur.close()
        conn.close()
        return False


def check_existence_group():
    conn = get_select_connection()
    cur = conn.cursor()
    sql = '''SELECT group_string FROM user_groups as ug
            LEFT OUTER JOIN joining_groups as jg ON jg.group_id = ug.group_id
            WHERE joining_group_id is null 
            GROUP BY group_string'''
    try:
        cur.execute(sql,)
        result = cur.fetchall()
        cur.close()
        conn.close()
        for i in result:
            delete_group_db(i[0])
    except MySQLdb.Error as e:
        cur.close()
        conn.close()
    return

