import os
import MySQLdb
import datetime

from db.connect_db import get_select_connection, get_update_connection


def get_join_groups(id: str):
    """
    現在の最新のユーザーIDを取得
    Args:
    id: str
    Returns:
      自分が所属しているグループとその一覧
    """

    conn = get_select_connection()
    cur = conn.cursor()

    cur.execute('''SELECT a.user_id,u.user_name, b.group_id, c.group_name FROM joining_groups AS a 
    INNER JOIN (SELECT group_id FROM joining_groups WHERE user_id = (%s)) AS b ON b.group_id = a.group_id LEFT
    OUTER JOIN user_groups as c on c.group_id = b.group_id LEFT OUTER JOIN users as u on u.user_id = a.user_id ORDER BY group_id''', (1,))

    group_list = cur.fetchall()
    cur.close()
    conn.close()

    return group_list


def set_schedule(user_id,title, start_day, end_day, color, job_id, is_private):
    conn = get_update_connection()
    cur = conn.cursor()
    
    flg =0
    if is_private:
       flg =1 
        
    
    
    print(color)
    if job_id == "-1":
        cur.execute('INSERT INTO schedules(user_id,color_code,schedule_title,start_time,end_time,private_flg) VALUES(%s,%s,%s,%s,%s,%s)',
                (user_id, color, title, start_day, end_day, flg))
    else:
        cur.execute('INSERT INTO schedules(user_id,job_id,color_code,schedule_title,start_time,end_time,private_flg) VALUES(%s,%s,%s,%s,%s,%s,%s)',
                    (user_id, job_id, color, title, start_day, end_day, flg))
    conn.commit()
    
    cur.close()
    conn.close()
    
    return True
    # DBとのコネクションを取得
    

def get_my_schedules(user_id,sy,sm,ey,em):
    
    start_date = datetime.date(int(sy), int(sm), 1)
    end_date = datetime.date(int(ey), int(em), 1)
    
    
    conn = get_select_connection()
    cur = conn.cursor()
    cur.execute('SELECT schedules.color_code,schedule_title,start_time,end_time,job_infos.job_name FROM schedules LEFT OUTER JOIN job_infos on schedules.job_id = job_infos.job_id where schedules.user_id = %s and start_time > %s and end_time < %s and schedules.delete_flg = false ORDER BY start_time  '
                 ,(user_id,start_date,end_date))
    
    schedule_list = cur.fetchall()
    cur.close()
    conn.close()
    return schedule_list
    

def get_jobs(user_id):
    conn = get_update_connection()
    cur = conn.cursor()
    cur.execute('SELECT job_id, job_name, color_code FROM job_infos where user_id = %s',(user_id,))
    
    job_list = cur.fetchall();
    cur.close()
    conn.close()
    
    return job_list
    
    
    
    
    



