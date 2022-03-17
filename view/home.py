from types import resolve_bases
from db.home_db import get_join_groups
from flask import Flask, Blueprint, render_template, request, redirect, jsonify

home = Blueprint('home',__name__, url_prefix='/home')

@home.route('/')
def home_index():
   return render_template('home.html')

@home.route('/get_group',methods=["GET"])
def get_group():
   user_id = 1 #userID 
   join_groups_table = get_join_groups(user_id)
   now_group = join_groups_table[0][2]
   groups = {'items':[]}
   group_info ={
      'group_id':join_groups_table[0][2],
      'group_name':join_groups_table[0][3],
      'user_list':[]
   }
   
   for join_tpl in join_groups_table:
      if now_group == join_tpl[2]:
         group_info['user_list'].append({'user_id':join_tpl[0],'user_name':join_tpl[1]})
      else:
         groups['items'].append(group_info)
         group_info = {
            'group_id':join_tpl[2],
            'group_name':join_tpl[3],
            'user_list':[]
         }
         group_info['user_list'].append({'user_id':join_tpl[0],'user_name':join_tpl[1]})
         
   groups['items'].append(group_info)
   return jsonify(groups)
         
   