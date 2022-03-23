"use strict";

$(function(){
    const qrtext = location.href;
    const utf8qrtext = unescape(encodeURIComponent(qrtext));
    const group_name = document.getElementById("group_name_text");
    let group_name_def = $("#group_name_text").val();
    $("#group_link_qr_img").html("").qrcode({text:utf8qrtext});

    $("#edit_button img").on("click", () => {
        group_name.toggleAttribute("readonly");
        $("#edit_button img").toggleClass("edit_button_before edit_button_after")
    });

    $("#submit_button").on("click", () => {
        group_name_def = $("#group_name_text").val();
        const postdata = new FormData();
        postdata.append("new_group_name", group_name_def)
        const XHR = new XMLHttpRequest();
        XHR.open("POST", location.href, true)
        XHR.send(postdata)
    })

    $("#cancel_button").on("click", () => {
        $("#group_name_text").val(group_name_def);
    })


});

const copyToClipboard = () => {
    // 選択しているテキストをクリップボードにコピーする
    if(navigator.clipboard == undefined) {
        window.clipboardData.setData('Text', location.href);
    } else {
        navigator.clipboard.writeText(location.href);
    }
    alert("クリップボードにコピーしました");
};

const confirm_remove = (message) => {
    const res = confirm(message)
    if (res) {
        return true;
    } else {
        return false;
    }
}
