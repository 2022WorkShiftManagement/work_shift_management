const DAYS = ["日", "月", "火", "水", "木", "金", "土"]
let modal;
window.addEventListener('DOMContentLoaded', (event) => {
   const nowDate = new Date(Date.now());

   const month_date = getMonthDaycount(nowDate.getFullYear(), nowDate.getMonth() + 1)
   const ul = document.getElementById('cal');
   modal = document.getElementById('easyModal');
   const buttonClose = document.getElementsByClassName('modalClose')[0];
   //モーダルコンテンツ以外がクリックされた時
   addEventListener('click', outsideClose);
   //バツ印がクリックされた時
   buttonClose.addEventListener('click', modalClose);
   
   for (let i = 0; i < month_date; i++) {
      const date_li = document.createElement('li')
      date_li.className = 'days-area'
      date_li.id = formatDate(new Date(nowDate.getFullYear(),nowDate.getMonth(),i+1))
      date_li.addEventListener('click',() =>{
         create_popup(new Date(nowDate.getFullYear(),nowDate.getMonth()))
      })

      if (getMonthDays(nowDate.getFullYear(), nowDate.getMonth(), i + 1) === '日') {
         date_li.innerHTML =  `<div class="date-txt" >${i+1}</div><div class="day sun">${getMonthDays(nowDate.getFullYear(),nowDate.getMonth(),i+1)}</div>`
         ul.appendChild(date_li)

      } else if (getMonthDays(nowDate.getFullYear(), nowDate.getMonth(), i + 1) === '土') {
         date_li.innerHTML =  `<div class="date-txt" >${i+1}</div><div class="day sat">${getMonthDays(nowDate.getFullYear(),nowDate.getMonth(),i+1)}</div>`
         ul.appendChild(date_li)
      } else {
         date_li.innerHTML =  `<div class="date-txt" >${i+1}</div><div class="day">${getMonthDays(nowDate.getFullYear(),nowDate.getMonth(),i+1)}</div>`
         ul.appendChild(date_li)
      }
   }

   //const body = Object.keys(obj).reduce((o, key) => (o.set(key, obj[key]), o), new FormData())
   let link = location.href;
   let fetch_url = link.replace("/home/"+location.hash ,"/home/get_group");

   const head = {
      'Accept': 'application/json'
   }
   const methot = "GET"

   fetch((fetch_url), {
      "method": methot,
      "headers": head,
   }).then(async (res) => {
      return await res.json()
   }).then((data) => {
      setgroupData(data)
      //savedUserData = data;
   });

});

function getstrdate(date) {
   return "" + date.getFullYear() + (date.getMonth() + 1) + date.getDate()
}

function getMonthDaycount(fullyear, mounth) {
   return new Date(fullyear, mounth, 0).getDate()
}

function getMonthDays(fullyear, mounth, day) {
   return DAYS[new Date(fullyear, mounth, day).getDay()]
}

function setgroupData(data){
   const group_list = document.getElementById('group_list')
   data.items.forEach(element => {
      const group_tab = document.createElement('div')
      group_tab.className = 'cp_actab'


      const select_radio = document.createElement('input')
      select_radio.id = element.group_id
      select_radio.setAttribute('name','group')
      select_radio.type = 'radio'
      select_radio.className = 'group_radio'

      const hide_label = document.createElement('label')
      hide_label.htmlFor = element.group_id
      hide_label.className = 'radio_ci'

      const tab_check =  document.createElement('input')
      tab_check.id = 'tab-' +element.group_id
      tab_check.type = 'checkbox'
      tab_check.setAttribute('name','tabs')

      const tabs_label = document.createElement('label')
      tabs_label.htmlFor  ='tab-' +  element.group_id
      tabs_label.className = 'group_name'
      tabs_label.innerText = element.group_name
      
      const user_list = document.createElement('div')
      user_list.className = 'cp_actab-content'
      element.user_list.forEach(user =>{
         const user_col = document.createElement('p')
         user_col.id = 'user-' + user.user_id;
         user_col.innerText = user.user_name
         user_list.appendChild(user_col)
      })

      group_tab.appendChild(select_radio)
      group_tab.appendChild(hide_label)
      group_tab.appendChild(tab_check)
      group_tab.appendChild(tabs_label)
      group_tab.appendChild(user_list)
      group_list.appendChild(group_tab)

   });
}

function formatDate(dt) {
   var y = dt.getFullYear();
   var m = ('00' + (dt.getMonth()+1)).slice(-2);
   var d = ('00' + dt.getDate()).slice(-2);
   return (y + m + d);
 }

function create_popup(id){
   modal.style.display = 'block';
   document.getElementById('modal-text').innerHTML = id + document.getElementById('modal-text').innerHTML

}


function modalClose() {
   modal.style.display = 'none';
};



function outsideClose(e) {
   if (e.target == modal) {
   modal.style.display = 'none';
   };
};
