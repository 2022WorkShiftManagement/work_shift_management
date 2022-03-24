from sre_constants import SUCCESS
from types import resolve_bases
from db.home_db import get_group_schedules, get_jobs, get_join_groups, get_my_schedules, set_schedule
from flask import Flask, Blueprint, render_template, request, redirect, jsonify,session

home = Blueprint('home', __name__, url_prefix='/home')


@home.route('/')
def home_index():
    return render_template('home.html',user_id=session['user'])


@home.route('/get_group', methods=["GET"])
def get_group():
    if "user" not in session:
        return redirect("/")
    user_id = session['user']# userID
    join_groups_table = get_join_groups(user_id)
    now_group = join_groups_table[0][2]
    groups = {'items': []}
    group_info = {
        'group_id': join_groups_table[0][2],
        'group_name': join_groups_table[0][3],
        'group_string':join_groups_table[0][4],
        'user_list': []
    }
    if join_groups_table is None:
        return

    for join_tpl in join_groups_table:
        if now_group == join_tpl[2]:
            group_info['user_list'].append(
                {'user_id': join_tpl[0], 'user_name': join_tpl[1]})
        else:
            groups['items'].append(group_info)
            group_info = {
                'group_id': join_tpl[2],
                'group_name': join_tpl[3],
                'group_string': join_tpl[4],
                'user_list': []
            }
            group_info['user_list'].append(
                {'user_id': join_tpl[0], 'user_name': join_tpl[1]})

    groups['items'].append(group_info)
    return jsonify(groups)

@home.route('/send-schedule', methods=["POST"])
def send_schedule():
    if "user" not in session:
        return jsonify({"values":"BAD SESSION"})
    
    #a
    start_day = request.form.get('start-day')
    end_day = request.form.get('end-day')
    title = request.form.get('title')
    title_color = request.form.get('color')
    job_id = request.form.get('job_id')
    is_private = request.form.get("is_private")
    print(job_id)
    
    
  
    if set_schedule(session['user'],title,start_day,end_day,int(str(title_color),16),job_id,is_private):
        return jsonify({"values":"SUCCESS"})
    else:
        return jsonify({"values":"BAD..."})
    

@home.route('/get-schedule', methods=["POST"])
def get_schedule():
    if "user" not in session:
        return jsonify({"values":"BAD SESSION"})
    start_m = request.form.get('start-m')
    start_y = request.form.get('start-y')
    end_m = request.form.get('end-m')
    end_y = request.form.get('end-y')

    print(start_m)
    print(end_m)
    schedules = get_my_schedules(session['user'],start_y,start_m,end_y,end_m)
    
    if schedules is None:
        return jsonify({"values":"No DATA"})
    
    json_schedule = {'items': []}
    
    for schedule_tpl in schedules:
        if schedule_tpl[0] is None:
            print(schedule_tpl[3])
            group_info = {
            'title': schedule_tpl[1],
            'color': '{0:06x}'.format(schedule_tpl[0]),
            'job_name': schedule_tpl[4],
            'start_time': schedule_tpl[2].strftime('%Y-%m-%dT%H:%M:00'),
            'end_time':schedule_tpl[3].strftime('%Y-%m-%dT%H:%M:00')
            }
            
        else:
            print(schedule_tpl[3])    
            group_info = {
                'title': schedule_tpl[1],
                'color': '{0:06x}'.format(schedule_tpl[0]),
                'job_name': schedule_tpl[4],
                'start_time': schedule_tpl[2].strftime('%Y-%m-%dT%H:%M:00'),
                'end_time':schedule_tpl[3].strftime('%Y-%m-%dT%H:%M:00')
                }
        json_schedule['items'].append(group_info)

    return jsonify(json_schedule)

@home.route('/get-jobs', methods=["GET"])
def get_joblist():
    if "user" not in session:
        return jsonify({"values":"BAD SESSION"})
    job_list = get_jobs(session['user'])
    
    json_jobs = {'items': []}
    
    if job_list is None:
        return jsonify({"values":"No DATA"})
    
    for job_tpl in job_list:
        job_info = {
            'job_id':job_tpl[0],
            'job_name':job_tpl[1],
            'color':'{0:06x}'.format(job_tpl[2])
        }
        json_jobs['items'].append(job_info)
        
    return json_jobs
        

@home.route('/get-group-schedule', methods=["POST"])
def get_group_schedule():
    if "user" not in session:
        return jsonify({"values":"BAD SESSION"})
    group_id = request.form.get('group_id')
    start_m = request.form.get('start-m')
    start_y = request.form.get('start-y')
    end_m = request.form.get('end-m')
    end_y = request.form.get('end-y')

    
    schedules = get_group_schedules(session['user'],group_id,start_y,start_m,end_y,end_m)
    json_schedule = {'items': []}
    if schedules is None:
        return
    
    for schedule_tpl in schedules:
        if schedule_tpl[0] is None:
            print(schedule_tpl[3])
            group_info = {
            'title': schedule_tpl[1],
            'name': schedule_tpl[0],
            'job_name': schedule_tpl[4],
            'start_time': schedule_tpl[2].strftime('%Y-%m-%dT%H:%M:00'),
            'end_time':schedule_tpl[3].strftime('%Y-%m-%dT%H:%M:00')
            }
            
        else:
            group_info = {
                'title': schedule_tpl[1],
                'user_id':schedule_tpl[5],
                'name': schedule_tpl[0],
                'job_name': schedule_tpl[4],
                'start_time': schedule_tpl[2].strftime('%Y-%m-%dT%H:%M:00'),
                'end_time':schedule_tpl[3].strftime('%Y-%m-%dT%H:%M:00')
                }
        json_schedule['items'].append(group_info)
    
    return json_schedule
    
    
    
    
    