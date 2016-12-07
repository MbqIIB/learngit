/**
 * Created by lianliang on 16/9/10.
 */


// 创建select元素
function createSelect(value) {
    if(value=='上线'){
        var html = '<select><option value="上线" selected="selected">上线</option><option value="下线">下线</option></select>';
    }else {
        var html = '<select><option value="上线">上线</option><option value="下线" selected="selected">下线</option></select>';
    }
    return html;
}

// 创建一行
function createTr(value) {
    var html_start = '<tr>';
    var checkbox = '<td class="edit_select"><input type="checkbox" /></td>';
    var id = '<td name="NEW" style="color: red">NEW</td>';
    var hostname = '<td name="hostname" editEnable="true" edType="text"><input type="text" style="width:100%;"/></td>';
    var address = '<td name="address" editEnable="true" edType="text"><input type="text" style="width:100%;"/></td>';
    var port = '<td name="port" editEnable="true" edType="text"><input type="text" style="width:100%;"/></td>';
    var status = '<td name="status" editEnable="true" edType="select"></td>';
    var html_end = '</tr>';
    
    var html = html_start + checkbox + id + hostname + address + port + status + html_end;
    return html;
}

// 表单变更,接受一行(tr)内容和动作
function SubmitForm(ths,active) {
    $.ajax({
        url: '/data/1/',
        type: 'POST',
        data: {
            'active': active,
            'nid': $(ths).find('[name = "nid"]').text(),
            'hostname': $(ths).find('[name = "hostname"]').text(),
            'address': $(ths).find('[name = "address"]').text(),
            'port': $(ths).find('[name = "port"]').text(),
            'status': $(ths).find('[name = "status"]').text()
        },
        dataType: 'json',
        success: function (result) {
            if (result.status) {
                // return result;
                $('#message').text(result.message);
                $('#message').css({"background-color": "darkseagreen", "color": "white"});
                setTimeout( function () {
                    $('#message').text('');
                    location.reload();  // 重新加载页面
                },3000);
            }else {
                // return result;
                $('#message').text(result.message);
                $('#message').css({"background-color": "red", "color": "white"});
                setTimeout( function () {
                    $('#message').text('');
                    location.reload();  // 重新加载页面
                },3000);
                // alert(result.message);
            }
        }
    });
}


// 表单验证
function FromVerify() {
    
}


// 单行进入编辑模式
function rowInEditing(ths) {
    $(ths).parent().removeClass('table-striped');
    $(ths).parent().addClass('table-bordered');
    // var close = '<td><i style="font-size: 18px;" class="fa fa-times" aria-hidden="true" onclick=""></i></td>';
    // $(ths).parent().append(close);
    $(ths).children().each(function () {
        if($(this).attr("editEnable")){
            if($(this).attr("edType")=="select"){
                var value = $(this).text();
                var select_element = createSelect(value);
                $(this).html(select_element);
            }else{
                var text = $(this).text();
                var html = "<input type='text' style='width:100%;'/>";
                $(this).html(html);
                $(this).children().attr('value', text);
            }
        }
    });
}

// 单行退出编辑模式
function rowOutEditing(ths) {
    $(ths).parent().removeClass('table-bordered');
    $(ths).parent().addClass('table-striped');
    $(ths).children().each(function () {
        if($(this).attr("editEnable")){
            if($(this).attr("edType") == "select"){
                var value = $(this).find("select option:selected").val();
                $(this).html(value);
            }else {
                $(this).find("input").each(function () {
                    var value = $(this).val();
                    $(this).parent().text(value);
                });
            }
        }
    });
}


// 绑定checkbox按钮,在进入编辑模式后,选中则进入编辑,取消选中则退出编辑
$(function () {
    $('input[type="checkbox"]').click(function () {
        if(EDITOR_STATUS){
            if($(this).prop('checked')){
                var tr = $(this).parent().parent();
                rowInEditing(tr);
            }else {
                var tr = $(this).parent().parent();
                rowOutEditing(tr);
                SubmitForm(tr,'update');
            }
        }
    });
});

// 页面刚加载完执行,分页按钮添加样式
$(function () {
    $('.page-number').each( function () {
        var url = location.href;
        var current_page = url.split('/')[4];
        var current_num = $(this).text();
        if (current_page == current_num) {
            $(this).addClass('current');
        }
    });
});

// 编辑模式下按回车提交
$(function () {
    window.onkeydown = function (event) {
        if (event && event.keyCode == 13) {
            $('input').parent().parent().each(function () {
                var ths = $(this);
                rowOutEditing(ths);
                SubmitForm(ths, 'update');
                // tr.remove();
            });
        }
    }
});



// 分页上翻下翻按钮
$(function () {
    var current_page = parseInt($('.current').text());
    if(current_page == 1) {
        $('.previous').addClass('disabled');
    }else {
        // $('.previous').removeClass('disabled');
        var prev_page = current_page-1;
        var prev_url = '/data/'.concat(prev_page) + '/';
        $('.previous a').each( function () {
            $(this).attr('href', prev_url);

        })
    }
    // 现有的page最后一个是多少,做比较
    var last_page = $('.pager').find('.page-number:last').text();
    if(current_page == last_page) {
        $('.next').addClass('disabled');
    }else {
        // $('.previous').removeClass('disabled');
        var next_page = current_page+1;
        var next_url = '/data/'.concat(next_page) + '/';
        $('.next a').each( function () {
            $(this).attr('href', next_url);

        })
    }
});



// 编辑模式全局标识
var EDITOR_STATUS = false;

// 切换编辑模式
$("#edit").click(function () {
    if(EDITOR_STATUS){
        EDITOR_STATUS = false;
        $(this).removeClass("btn-danger");
        $(this).addClass("btn-success");
        $(this).html('<i class="fa fa-share" aria-hidden="true"></i>&nbsp;进入编辑模式');
        var checkboxes = $('input[type="checkbox"]');
        checkboxes.each(function () {
            if($(this).prop("checked")){
                var tr = $(this).parent().parent();
                rowOutEditing(tr);
                SubmitForm(tr,'update');
            }
         });
    }else{
        EDITOR_STATUS = true;
        $(this).removeClass("btn-success");
        $(this).addClass("btn-danger");
        $(this).html('<i class="fa fa-reply" aria-hidden="true"></i>&nbsp;退出编辑模式');
        var checkboxes = $('input[type="checkbox"]');
        checkboxes.each(function () {
            if($(this).prop("checked")){
                var tr = $(this).parent().parent();
                rowInEditing(tr);
            }
         });
    }
});


// 全选按钮动作
$("#all").click(function () {
    if(EDITOR_STATUS){
        var checkboxes = $('input[type="checkbox"]');
        checkboxes.each(function () {
            if(!$(this).prop("checked")){
                $(this).prop("checked",true);
                var tr = $(this).parent().parent();
                rowInEditing(tr);
            }
         });
    }else{
        $('input[type="checkbox"]').prop("checked",true);
    }
});


// 取消按钮动作
$("#cancel").click(function () {
    if(EDITOR_STATUS){
        var checkboxes = $('input[type="checkbox"]');
        checkboxes.each(function () {
            if($(this).prop("checked")){
                $(this).prop("checked",false);
                var tr = $(this).parent().parent();
                rowOutEditing(tr);
                SubmitForm(tr,'update');
            }
         });
    }else{
        $('input[type="checkbox"]').prop("checked",false);
    }
});


// 反选按钮动作
$("#reverse").click(function () {
    if(EDITOR_STATUS){
        var checkboxes = $('input[type="checkbox"]');
        checkboxes.each(function () {
            if(!$(this).prop("checked")){
                $(this).prop("checked",true);
                var tr = $(this).parent().parent();
                rowInEditing(tr);
            }else{
                $(this).prop("checked",false);
                var tr = $(this).parent().parent();
                rowOutEditing(tr);
            }
         });
    }else{
        var checkboxes = $('input[type="checkbox"]');
        checkboxes.each(function () {
            if($(this).prop("checked")){
                $(this).prop("checked",false);
            }else{
                $(this).prop("checked",true);
            }
        });
    }
});


// 删除按钮动作
$("#del").click(function () {
    var checkboxes = $('input[type="checkbox"]');
    checkboxes.each(function () {
        if ($(this).prop("checked")) {
            var tr = $(this).parent().parent();
            SubmitForm(tr, 'delete');
            tr.remove();
        }
    });
});


// 添加按钮动作
$("#add").click(function () {
    var tr = createTr();
    var select = createSelect();
    $('tbody').prepend(tr);
    $('tbody tr:first [name="status"]').html(select);
    $('tbody tr:first').append('<td><a>点击查看</a></td>');
    window.onkeydown = function (event) {
        if(event && event.keyCode == 13) {
            $('td[name="NEW"]').parent().each( function () {
                var ths = $(this); 
                rowOutEditing(ths);
                SubmitForm(ths, 'add');
                // tr.remove();
            });
        }
    }
});


