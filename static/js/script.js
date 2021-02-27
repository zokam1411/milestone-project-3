$(document).ready(function(){
    $('.sidenav').sidenav({edge: 'right'})
    $(".dropdown-trigger").dropdown({coverTrigger: false});
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('input#title, textarea#description').characterCounter();
});