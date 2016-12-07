/**
 * Created by lianliang on 16/8/20.
 */

function alert_msg() {
    // js 获取一个id='username'的标签
    var text = document.getElementById("username");
    var message = document.getElementsByClassName("message");
    var msg = document.getElementsByClassName("msg");
    // 获取标签内容
    var username = text.value;
    msg[0].innerHTML="欢迎您,神奇宝贝训练家:" + username;
    message[0].style.display = "block";
    // alert("欢迎您,神奇宝贝训练家:" + username)
}


function content() {
    // js 获取一个id='username'的标签
    var text = document.getElementById("username");
    var message = document.getElementsByClassName("message");
    var mask = document.getElementsByClassName("mask");
    var content = document.getElementsByClassName("content");
    // var msg = document.getElementsByClassName("msg");
    // 获取标签内容
    var username = text.value;
    // msg[0].innerHTML="欢迎您,神奇宝贝训练家:" + username;
    message[0].style.display = "none";
    mask[0].style.display = "block";
    content[0].style.display = "block";
}


function quit() {
    // js 获取一个id='username'的标签
    var text = document.getElementById("username");
    var mask = document.getElementsByClassName("mask");
    var content = document.getElementsByClassName("content");
    // var msg = document.getElementsByClassName("msg");
    // 获取标签内容
    var username = text.value;
    // msg[0].innerHTML="欢迎您,神奇宝贝训练家:" + username;
    mask[0].style.display = "none";
    content[0].style.display = "none";
}