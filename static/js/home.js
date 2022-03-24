const DAYS = ["日", "月", "火", "水", "木", "金", "土"]
const USERCOLOR = ['FF0000', 'FF3399', 'FF9100', 'FFD400', '008000', 'B2D235', '67A7CC', '0067C0', '5F4894', '717375']
let modal;
let calmode = 0
const nowDate = new Date(Date.now());
let top_load_flg = true;
let selectedg = -1
let back_load_flg = true;


window.addEventListener('DOMContentLoaded', (event) => {

   modal = document.getElementById('easyModal');
   const buttonClose = document.getElementsByClassName('modalClose')[0];

   //３ヶ月分のカレンダー
   create_calendar(new Date(nowDate.getFullYear(), nowDate.getMonth(), 1))


   //モーダルコンテンツ以外がクリックされた時
   addEventListener('click', outsideClose);
   //[閉じる]がクリックされた時
   buttonClose.addEventListener('click', modalClose);
   console.log('-----------------')

   set_schedule(new Date(nowDate.getFullYear(), nowDate.getMonth() - 2, 1), new Date(nowDate.getFullYear(), nowDate.getMonth() + 1, 31))

   document.getElementById('-1').addEventListener('click', () => {
      groupChange()
   })
   //const body = Object.keys(obj).reduce((o, key) => (o.set(key, obj[key]), o), new FormData())
   //グループの取得
   let link = location.href;
   let fetch_url = link.replace("/home/" + location.hash, "/home/get_group");
   console.log(fetch_url)

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
   }).catch((e) => {
      let link = location.href;
      location.href = link.replace("/home/" + location.hash, "/");
   });

   //
   let linka = location.href;
   let fetch_urla = linka.replace("/home/" + location.hash, "/home/get-jobs");
   const heada = {
      'Accept': 'application/json'
   }
   const methota = "GET"

   fetch((fetch_urla), {
      "method": methota,
      "headers": heada,
   }).then(async (res) => {
      return await res.json()
   }).then((data) => {
      setjobData(data)
      //savedUserData = data;
   }).catch((e) => {
      let link = location.href;
      //location.href = link.replace("/home/" + location.hash, "/");
   });
   document.documentElement.scrollTop = document.getElementById(formatDate(nowDate)).getBoundingClientRect().top + window.pageYOffset + 10
   window.onscroll = function () {
      //下部スクロールで新しい日付を追加
      if (this.scrollY > document.body.scrollHeight - window.innerHeight - 100 && back_load_flg) {
         back_load_flg = false;
         let lastchild = document.getElementById('cal').lastElementChild;
         const date = new Date(lastchild.id.substr(0, 4), Number(lastchild.id.substr(4, 2)))
         add_calendar(date, false)
         set_schedule(date, new Date(date.getFullYear(), date.getMonth() + 2, 0))



      }
      //上部(ry
      if (this.scrollY < 1 && top_load_flg) {
         top_load_flg = false
         let firstchild = document.getElementById('cal').firstElementChild;
         document.documentElement.scrollTop = document.getElementById(`${firstchild.id.substr( 0, 4 )}${firstchild.id.substr( 4, 6 )}`).getBoundingClientRect().top + window.pageYOffset + 1800
         const date = new Date(firstchild.id.substr(0, 4), Number(firstchild.id.substr(4, 6)) - 2)
         add_calendar(date, true)
         set_schedule(date, new Date(date.getFullYear(), date.getMonth() + 2, 0))
      }
   };


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

function groupChange() {
   let elements = document.getElementsByName('group');
   for (let i = 0; i < elements.length; i++) {
      if (elements.item(i).checked) {
         selectedg = elements.item(i).id;
         //TODO:
      }

   }
   console.log(selectedg)
   if (selectedg == -1) {
      const ul = document.getElementById('cal');
      ul.innerHTML = ''
      create_calendar(new Date(nowDate.getFullYear(), nowDate.getMonth(), 1))
      calmode = 0
      set_schedule(new Date(nowDate.getFullYear(), nowDate.getMonth() - 2, 1), new Date(nowDate.getFullYear(), nowDate.getMonth() + 1, 31))

   } else {
      const ul = document.getElementById('cal');
      ul.innerHTML = ''
      create_calendar(new Date(nowDate.getFullYear(), nowDate.getMonth(), 1))
      calmode = 1
      set_schedule(new Date(nowDate.getFullYear(), nowDate.getMonth() - 2, 1), new Date(nowDate.getFullYear(), nowDate.getMonth() + 1, 31))
   }

   document.documentElement.scrollTop = document.getElementById(formatDate(nowDate)).getBoundingClientRect().top + window.pageYOffset + 10


}

function create_calendar(date) {
   for (let mm = 0; mm < 3; mm++) {

      const month_date = getMonthDaycount(date.getFullYear(), Number(date.getMonth()) + (mm))
      const ul = document.getElementById('cal');
      const mounth_li = document.createElement('li')
      mounth_li.style.backgroundColor = '#27C5FF'
      mounth_li.style.color = '#FDFDFD'
      mounth_li.style.textAlign = 'center'
      mounth_li.id = (`${date.getFullYear()}${('00' + (date.getMonth() +(mm))).slice(-2)}`)
      mounth_li.innerText = `${date.getFullYear()}年　${Number(date.getMonth()) + (mm)}月`
      mounth_li.className = 'sticky-li'
      ul.appendChild(mounth_li)
      for (let i = 0; i < month_date; i++) {
         const date_li = document.createElement('li')
         date_li.className = 'days-area'

         date_li.id = formatDate(new Date(date.getFullYear(), date.getMonth() + (mm - 1), i + 1))
         if (date_li.id == formatDate(nowDate)) {
            date_li.style.backgroundColor = '#C1E4F1'
         }
         date_li.addEventListener('click', () => {
            create_popup(new Date(date.getFullYear(), date.getMonth() + (mm - 1), i + 1))
         })

         if (getMonthDays(date.getFullYear(), date.getMonth() + (mm - 1), i + 1) === '日') {
            date_li.innerHTML = `<div class="date-txt" >${i+1}</div><div class="day sun">${getMonthDays(date.getFullYear(),date.getMonth() + (mm - 1),i+1)}</div>`
            ul.appendChild(date_li)

         } else if (getMonthDays(date.getFullYear(), date.getMonth() + (mm - 1), i + 1) === '土') {
            date_li.innerHTML = `<div class="date-txt" >${i+1}</div><div class="day sat">${getMonthDays(date.getFullYear(),date.getMonth() + (mm - 1),i+1)}</div>`
            ul.appendChild(date_li)
         } else {
            date_li.innerHTML = `<div class="date-txt" >${i+1}</div><div class="day">${getMonthDays(date.getFullYear(),date.getMonth() + (mm - 1),i+1)}</div>`
            ul.appendChild(date_li)
         }
      }
   }
}

function add_calendar(date, front_flg) {

   const month_date = getMonthDaycount(date.getFullYear(), Number(date.getMonth() + 1))
   const mounth_li = document.createElement('li')
   mounth_li.style.backgroundColor = '#27C5FF'
   mounth_li.style.color = '#FDFDFD'
   mounth_li.style.textAlign = 'center'
   mounth_li.id = (`${date.getFullYear()}${('00' + (date.getMonth() +1)).slice(-2)}`)
   mounth_li.innerText = `${date.getFullYear()}年　${Number(date.getMonth() +1) }月`
   mounth_li.className = 'sticky-li'
   let li = document.getElementById('cal');
   if (front_flg) {
      li.prepend(mounth_li)
   } else {
      li.append(mounth_li)
   }


   let backelement = mounth_li
   for (let i = 0; i < month_date; i++) {
      const date_li = document.createElement('li')
      date_li.className = 'days-area'
      date_li.id = formatDate(new Date(date.getFullYear(), date.getMonth(), i + 1))
      date_li.addEventListener('click', () => {
         create_popup(new Date(date.getFullYear(), date.getMonth(), i + 1))
      })

      if (getMonthDays(date.getFullYear(), date.getMonth(), i + 1) === '日') {
         date_li.innerHTML = `<div class="date-txt" >${i+1}</div><div class="day sun">${getMonthDays(date.getFullYear(),date.getMonth(),i+1)}</div>`
         li.insertBefore(date_li, backelement.nextSibling)
      } else if (getMonthDays(date.getFullYear(), date.getMonth(), i + 1) === '土') {
         date_li.innerHTML = `<div class="date-txt" >${i+1}</div><div class="day sat">${getMonthDays(date.getFullYear(),date.getMonth(),i+1)}</div>`
         li.insertBefore(date_li, backelement.nextSibling)
      } else {
         date_li.innerHTML = `<div class="date-txt" >${i+1}</div><div class="day">${getMonthDays(date.getFullYear(),date.getMonth(),i+1)}</div>`
         li.insertBefore(date_li, backelement.nextSibling)
      }
      backelement = date_li
   }
   top_load_flg = true
   back_load_flg = true
}

function setgroupData(data) {
   const group_list = document.getElementById('group_list')
   data.items.forEach(element => {
      const group_tab = document.createElement('div')
      group_tab.className = 'cp_actab'


      const select_radio = document.createElement('input')
      select_radio.id = element.group_id
      select_radio.setAttribute('name', 'group')
      select_radio.type = 'radio'
      select_radio.className = 'group_radio dradio'
      select_radio.addEventListener('click', () => {
         groupChange()
      })

      const hide_label = document.createElement('label')
      hide_label.htmlFor = element.group_id
      hide_label.className = 'radio_ci'

      const tab_check = document.createElement('input')
      tab_check.id = 'tab-' + element.group_id
      tab_check.type = 'checkbox'
      tab_check.setAttribute('name', 'tabs')

      const tabs_label = document.createElement('label')
      tabs_label.htmlFor = 'tab-' + element.group_id
      tabs_label.className = 'group_name'
      tabs_label.innerText = element.group_name

      const user_list = document.createElement('div')
      user_list.className = 'cp_actab-content'
      let cnt = 0;
      element.user_list.forEach(user => {
         if (cnt >= 10) {
            cnt = 0;
         }
         const user_col = document.createElement('p')
         user_col.id = 'user-' + user.user_id;
         user_col.innerHTML = `<span style='color: #${USERCOLOR[cnt++]}'>●</span><span> ${user.user_name}</span>`
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

function setjobData(data) {
   const job_list = document.getElementById('job')
   const job_colorlist = []
   for (let i = 0; i < data.items.length; i++) {
      const job_name = document.createElement('option')
      job_name.value = data.items[i]['job_id']
      job_name.innerText = data.items[i]['job_name']
      job_list.appendChild(job_name)
      job_colorlist.push(data.items[i]['color'])
   }

   job_list.addEventListener('change', () => {
      if (job_list.selectedIndex == 0) {
         document.getElementById('color-pic').disabled = false;
         document.getElementById('jobco').value = '000000'
         document.getElementById('jobco').innerText = 'なし'

         document.getElementById('title').disabled = false;
         document.getElementById('title').value = ""

      } else {
         document.getElementById('color-pic').disabled = true;
         document.getElementById('jobco').value = job_colorlist[job_list.selectedIndex - 1]
         document.getElementById('jobco').innerText = job_colorlist[job_list.selectedIndex - 1]
         document.getElementById('title').disabled = true;
         document.getElementById('title').value = job_list.options[job_list.selectedIndex].text

      }
   })
}

function formatDate(dt) {
   var y = dt.getFullYear();
   var m = ('00' + (dt.getMonth() + 1)).slice(-2);
   var d = ('00' + dt.getDate()).slice(-2);
   return (y + m + d);
}

function formatInputDate(dt) {
   var y = dt.getFullYear();
   var m = ('00' + (dt.getMonth() + 1)).slice(-2);
   var d = ('00' + dt.getDate()).slice(-2);
   return (y + '-' + m + '-' + d);
}

function create_popup(id) {
   modal.style.display = 'block';
   //document.getElementById('modal-text').innerHTML = id + document.getElementById('modal-text').innerHTML
   document.getElementById('start-day').value = formatInputDate(id)
   document.getElementById('end-day').value = formatInputDate(id)
   //現在時刻をセット
   console.log(`${id.getHours()}:${id.getMinutes()}`)
   document.getElementById('start-time').value = `${("0" + nowDate.getHours()).slice( -2 )}:00`
   //1時間プラスする
   document.getElementById('end-time').value = `${("0" + (Number(nowDate.getHours()) +1)).slice( -2 ) }:00`

}


function modalClose() {
   modal.style.display = 'none';
};



function outsideClose(e) {
   if (e.target == modal) {
      modal.style.display = 'none';
   };
};

//DateTimeStrFormat
function dateTimeFormat(dateTime) {
   const year = dateTime.getFullYear();
   const nfmonth = 1 + dateTime.getMonth();
   const month = (nfmonth < 10) ? "0" + nfmonth : nfmonth;
   const nfdate = dateTime.getDate();
   const date = (nfdate < 10) ? "0" + nfdate : nfdate;
   const nfhour = dateTime.getHours();
   const hour = (nfhour < 10) ? "0" + nfhour : nfhour;
   const nfmin = dateTime.getMinutes();
   const min = (nfmin < 10) ? "0" + nfmin : nfmin;
   const nfsec = dateTime.getSeconds();
   const sec = (nfsec < 10) ? "0" + nfsec : nfsec;

   return `${year}/${month}/${date} ${hour}:${min}:${sec}`
}

function timeFormat(dateTime) {
   const nfhour = dateTime.getHours();
   const hour = (nfhour < 10) ? "0" + nfhour : nfhour;
   const nfmin = dateTime.getMinutes();
   const min = (nfmin < 10) ? "0" + nfmin : nfmin;
   const nfsec = dateTime.getSeconds();
   const sec = (nfsec < 10) ? "0" + nfsec : nfsec;
   return `${hour}:${min}`
}

function onsend() {
   //バリテート
   const title = document.getElementById('title')
   const start_day = document.getElementById('start-day')
   const start_time = document.getElementById('start-time')
   const end_day = document.getElementById('end-day')
   const end_time = document.getElementById('end-time')
   const job = document.getElementById('job')
   const color = document.getElementById('color-pic')
   const radio = document.getElementById('nopr')
   //valueの変換

   console.log(document.getElementById('start-time').value)
   let start_date_time = new Date(`${start_day.value}T${start_time.value}:00`)
   let end_date_time = new Date(`${end_day.value}T${end_time.value}:00`)
   console.log(start_date_time)

   if (job.value == -1) {
      if (title.value == '') {
         //TODO: エラー表示
         title.style.borderColor = '#FF0000'
         return
      }
   } else {
      title.style.border = ' 2px solid #c7c7c7'
   }

   if (end_day.value == '' || end_time.value == '') {
      //TODO: エラー表示
      start_day.style.borderColor = '#FF0000'
      start_time.style.borderColor = '#FF0000'
      end_day.style.borderColor = '#FF0000'
      end_time.style.borderColor = '#FF0000'
      return
   } else {
      start_day.style.borderColor = '#c7c7c7'
      start_time.style.borderColor = '#c7c7c7'
      end_day.style.borderColor = '#c7c7c7'
      end_time.style.borderColor = '#c7c7c7'
   }

   if (start_date_time > end_date_time) {
      //TODO: エラー表示
      start_day.style.borderColor = '#FF0000'
      start_time.style.borderColor = '#FF0000'
      end_day.style.borderColor = '#FF0000'
      end_time.style.borderColor = '#FF0000'
      return
   } else {
      start_day.style.borderColor = '#c7c7c7'
      start_time.style.borderColor = '#c7c7c7'
      end_day.style.borderColor = '#c7c7c7'
      end_time.style.borderColor = '#c7c7c7'
   }


   //TODO: バックエンドへPOSTする
   const setData = {
      'start-day': dateTimeFormat(start_date_time),
      'end-day': dateTimeFormat(end_date_time),
      'title': title.value,
      'color': color.value,
      'job_id': job.value,
      'is_private': !radio.value
   }
   console.log(color.value)

   const body = Object.keys(setData).reduce((o, key) => (o.set(key, setData[key]), o), new FormData())
   let link = location.href;
   let fetch_url = link.replace("/home/" + location.hash, "/home/send-schedule");

   const head = {
      'Accept': 'application/json'
   }
   const methot = "POST"

   fetch((fetch_url), {
      "method": methot,
      "headers": head,
      "body": body,
      "credentials": 'include' // クッキーを含める
   }).then(async (res) => {
      if (res.status == 200) {
         return await res.json()
      }
      alert("エラーが発生しました。\nステータスコード:" + res.status);
   }).then((data) => {
      console.log(data)
   });
   if (calmode == 0) {
      local_set_schedule(start_date_time, end_date_time, title.value, color.value)
   } else {
      const name = '自分'
      local_set_schedule(start_date_time, end_date_time, title.value, color.value, name)
   }

   //モーダルを削除する
   modalClose();
}

function set_schedule(start_date, end_date) {
   //TODO: バックエンドへPOSTする
   if (calmode == 0) {



      console.log(start_date.getMonth())
      const setData = {
         'start-y': start_date.getFullYear(),
         'start-m': start_date.getMonth() + 1,
         'end-y': end_date.getFullYear(),
         'end-m': end_date.getMonth() + 1,
      }

      const body = Object.keys(setData).reduce((o, key) => (o.set(key, setData[key]), o), new FormData())
      let link = location.href;
      let fetch_url = link.replace("/home/" + location.hash, "/home/get-schedule");

      const head = {
         'Accept': 'application/json'
      }
      const methot = "POST"

      fetch((fetch_url), {
         "method": methot,
         "headers": head,
         "body": body,
         "credentials": 'include' // クッキーを含める
      }).then(async (res) => {
         if (res.status == 200) {
            return await res.json()
         }
         alert("エラーが発生しました。\nステータスコード:" + res.status);
      }).then((data) => {
         data.items.forEach(element => {
            const eventDate = new Date(element['start_time'])
            const end_Date = new Date(element['end_time'])

            local_set_schedule(eventDate, end_Date, element['title'], element['color'])
         })

      });
   } else {

      console.log(start_date.getMonth())
      const setData = {
         'group_id': selectedg,
         'start-y': start_date.getFullYear(),
         'start-m': start_date.getMonth() + 1,
         'end-y': end_date.getFullYear(),
         'end-m': end_date.getMonth() + 1,
      }

      const body = Object.keys(setData).reduce((o, key) => (o.set(key, setData[key]), o), new FormData())
      let link = location.href;
      let fetch_url = link.replace("/home/" + location.hash, "/home/get-group-schedule");

      const head = {
         'Accept': 'application/json'
      }
      const methot = "POST"

      fetch((fetch_url), {
         "method": methot,
         "headers": head,
         "body": body,
         "credentials": 'include' // クッキーを含める
      }).then(async (res) => {
         if (res.status == 200) {
            return await res.json()
         }
         alert("エラーが発生しました。\nステータスコード:" + res.status);
      }).then((data) => {
         data.items.forEach(element => {
            const eventDate = new Date(element['start_time'])
            const end_Date = new Date(element['end_time'])

            local_set_schedule(eventDate, end_Date, element['title'], element['user_id'], element['name'])
         })

      });


   }
}

function local_set_schedule(start_date, end_date, title, color, name) {



   let mstartTime = timeFormat(start_date)
   let firstchild = document.getElementById('cal').firstElementChild;
   console.log(`${('00' + (start_date.getMonth() )).slice(-2)}`)
   console.log(`${Number(firstchild.id)}`)
   while (`${start_date.getFullYear()}${('00' + (start_date.getMonth()-1)).slice(-2)}99` < firstchild.id) {
      add_calendar(new Date(firstchild.id.substr(0, 4), Number(firstchild.id.substr(4, 2)) - 2), true)
      firstchild = document.getElementById('cal').firstElementChild
   }

   let lastchild = document.getElementById('cal').lastElementChild;
   let mendTime = timeFormat(end_date)
   console.log(`${end_date.getFullYear()}${('00' + (end_date.getMonth() )).slice(-2)}99`)
   while (`${end_date.getFullYear()}${('00' + (end_date.getMonth() +1 )).slice(-2)}00` > lastchild.id) {
      console.log(lastchild.id.substr(4, 6))
      add_calendar(new Date(lastchild.id.substr(0, 4), Number(lastchild.id.substr(4, 2))), false)
      lastchild = document.getElementById('cal').lastElementChild
   }

   console.log(formatDate(start_date))
   console.log(document.getElementById(formatDate(start_date)))
   const addevent = document.getElementById(formatDate(start_date))
   addevent.style.paddingBottom = '1em'
   let timeCount = end_date.getTime() - start_date.getTime()
   console.log(timeCount)


   if (calmode == 0) {
      if (timeCount > 86400000) {
         while (timeCount > 86400000) {


            const date = document.getElementById(formatDate(new Date(end_date - timeCount)))
            date.innerHTML = date.innerHTML + `<div class="schedule-text"><span style="color:#${color};margin-right: 0.5em">●</span>${mstartTime}〜24:00 ${title}</div>`
            timeCount = timeCount - 86400000
            mstartTime = '00:00'
         }
         document.getElementById(formatDate(end_date)).innerHTML = document.getElementById(formatDate(end_date)).innerHTML + `<div class="schedule-text"><span style="color:#${color};margin-right: 0.5em">●</span>${mstartTime}〜${timeFormat(end_date)}  ${title}</div>`
      } else {
         addevent.innerHTML = addevent.innerHTML + `<div class="schedule-text"><span style="color:#${color};margin-right: 0.5em">●</span>${timeFormat(start_date)}〜${timeFormat(end_date)}  ${title}</div>`

      }
   } else {
      //GROP
      const span_color = document.getElementById(`user-${color}`).children[0]
      if (timeCount > 86400000) {
         while (timeCount > 86400000) {


            const date = document.getElementById(formatDate(new Date(end_date - timeCount)))
            date.innerHTML = date.innerHTML + `<div class="schedule-text"><span style="color:${span_color.style.color};margin-right: 0.5em">●</span>${mstartTime}〜24:00 ${title}-${name}</div>`
            timeCount = timeCount - 86400000
            mstartTime = '00:00'
         }
         document.getElementById(formatDate(end_date)).innerHTML = document.getElementById(formatDate(end_date)).innerHTML + `<div class="schedule-text"><span style="color:${span_color.style.color};;margin-right: 0.5em">●</span>${mstartTime}〜${timeFormat(end_date)}  ${title}-${name}</div>`
      } else {
         addevent.innerHTML = addevent.innerHTML + `<div class="schedule-text"><span style="color:${span_color.style.color};margin-right: 0.5em">●</span>${timeFormat(start_date)}〜${timeFormat(end_date)}  ${title}-${name}</div>`

      }

   }


}
