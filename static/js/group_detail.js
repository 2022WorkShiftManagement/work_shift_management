$(function(){
    const qrtext = location.href;
    const utf8qrtext = unescape(encodeURIComponent(qrtext));
    $("#group_link_qr_img").html("");
    $("#group_link_qr_img").qrcode({text:utf8qrtext});
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