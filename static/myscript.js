var page_size = 1

$(document).ready(function(){
    $("#data").click(function (){
        var page_foot = $('div.page_foot');
        if (page_foot.length != 0) {
            page_foot.remove();
        } else {
        $.ajax({
            url: '/api/articles',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                page_no: 1,
                page_size: page_size
            }),
            processData: false,
            dataType: 'html',
            success: function(data, textStatus) {
                var page = $('div.page');
                page.append(data);
            },
            error: function(xhr, textStatus, errorThrown) {
                alert("error code: " + xhr.status + "status: " + textStatus + "error: "+ errorThrown);
            },
            complete: function(xhr, textStatus) {
//                alert("result code: " + xhr.status + "status: " + textStatus);
            }
        })
        }
    });
});


function prev() {
    var page_no = parseInt($("#page_no").text()) - 1;
    var count = parseInt($("#count").text());
    if (page_no <= 0) {
        alert("已到第一页");
        return
    }
    $.ajax({
            url: '/api/articles',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                page_no: page_no,
                page_size: page_size
            }),
            processData: false,
            dataType: 'html',
            success: function(data, textStatus) {
                var page_foot = $('div.page_foot');
                page_foot.remove();
                var page = $('div.page');
                page.append(data);
            },
            error: function(xhr, textStatus, errorThrown) {
                alert("error code: " + xhr.status + "status: " + textStatus + "error: "+ errorThrown);
            },
        })
    }


function next() {
    var page_no = parseInt($("#page_no").text()) + 1;
    var count = parseInt($("#count").text());
    if ((page_no - 1) * page_size >= count) {
        alert("已到最后一页");
        return
    }

    $.ajax({
            url: '/api/articles',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                page_no: page_no,
                page_size: page_size
            }),
            processData: false,
            dataType: 'html',
            success: function(data, textStatus) {
                var page_foot = $('div.page_foot');
                page_foot.remove();
                var page = $('div.page');
                page.append(data);
            },
            error: function(xhr, textStatus, errorThrown) {
                alert("error code: " + xhr.status + "status: " + textStatus + "error: "+ errorThrown);
            },
        })
    }