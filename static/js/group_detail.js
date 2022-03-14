$(function(){
    const group_link = document.getElementById("group_link_text");
    const qrtext = location.href;
    group_link.value = qrtext;
    const utf8qrtext = unescape(encodeURIComponent(qrtext));
    $("#group_link_qr_img").html("");
    $("#group_link_qr_img").qrcode({text:utf8qrtext});
});

const copyToClipboard = () => {
    // 選択しているテキストをクリップボードにコピーする
    if(navigator.clipboard == undefined) {
        window.clipboardData.setData('Text', group_link.value);
    } else {
        navigator.clipboard.writeText(group_link.value);
    }
   alert("クリップボードにコピーしました");
};