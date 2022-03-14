window.addEventListener('DOMContentLoaded', (event) => {
   const nowDate = new Date(Date.now());

   const month_date = getMonthDaycount(nowDate.getFullYear(),nowDate.getMonth()+1)
   const ul = document.getElementById('cal');
   for(let i=0;i<month_date;i++){
      ul.innerHTML += `<li class="days-area"><div class="date-txt">${i+1}</div></li>`
   }

   

});


function getMonthDaycount(fullyear,mounth){
   return new Date(fullyear,mounth,0).getDate()
}
