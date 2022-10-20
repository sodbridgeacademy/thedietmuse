var sidebar = document.getElementById('sidebar');

function sidebarToggle() {
    if (sidebar.style.display === "none") {
        console.log('click in')
        sidebar.style.display = "block";
    } else {
        sidebar.style.display = "none";
        console.log('click out')
    }
}


var profileDropdown = document.getElementById('ProfileDropDown');

function profileToggle() {
    if (profileDropdown.style.display === "none") {
        profileDropdown.style.display = "block";
    } else {
        profileDropdown.style.display = "none";
    }
}

function navSlide(){
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');

    burger.addEventListener('click', function(){
        nav.classList.toggle('nav-active');
        console.log('event triggered');
    }); 
}

navSlide();

$(document).ready(function(){
   $('.button-left').click(function(){
       $('.sidebar').toggleClass('fliph');
   });
     
});

today = new Date();
var year = today.getFullYear();
var month = today.getMonth();
var day = today.getDate()

document.getElementById('date').innerHTML = year

console.log('Current Year: ', year)