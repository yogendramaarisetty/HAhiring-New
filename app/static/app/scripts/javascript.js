$(document).ready(function() {
$
var e = ace.edit("code_editor");
e.getSession().setMode("ace/mode/java");
var selected="";
$("#q1_btn").click(function(){
    $(selected).css("background-color","#FFFFFF");
    $(selected).css("color","black");
    $("#q1_btn").css("background-color","green");
    $("#q1_btn").css("color","white");
    selected = "#q1_btn";
})

$("#q2_btn").click(function(){
    $(selected).css("background-color","#FFFFFF");
    $(selected).css("color","black");
    $("#q2_btn").css("background-color","green");
    $("#q2_btn").css("color","white");
    selected = "#q2_btn";
})
$("#q3_btn").click(function(){
    $(selected).css("background-color","#FFFFFF");
    $(selected).css("color","black");
    $("#q3_btn").css("background-color","green");
    $("#q3_btn").css("color","white");
    selected = "#q3_btn";
})
$("#q4_btn").click(function(){
    $(selected).css("background-color","#FFFFFF");
    $(selected).css("color","black");
    $("#q4_btn").css("background-color","green");
    $("#q4_btn").css("color","white");
    selected = "#q4_btn";
})
$("#q5_btn").click(function(){
    $(selected).css("background-color","#FFFFFF");
    $(selected).css("color","black");
    $("#q5_btn").css("background-color","green");
    $("#q5_btn").css("color","white");
    selected = "#q5_btn";
})

})


var date=new Date()
$(document).ready( function(){
    $(".testdate").html(date.toDateString());
})
