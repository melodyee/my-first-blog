/**
 * Created by libingxin on 7/9/17.
 */

//$(function(){
//   $('.navbar-nav li').click(function(e){
//       e.preventDefault();
//       $(this).addClass('active').siblings().removeClass('active');
//   });
//});

//$(document).ready(function(){
//    $("#signin").click(function(e){
//        e.preventDefault();
//        alert("Hello World!");
//        //$(this).addClass('active').siblings().removeClass('active');
//    });
//
//
//});

//$(function(){
//    $(".navbar-nav li").click(function(){
//    //$("#navbar-nav li").click(function(){
//    //    alert("Hello World!");
//        console.log("I am a log: click bar");
//        $(this).addClass('active').siblings().removeClass('active');
//        //return false;
//    });
//})
$(function(){
    $("#navbar-nav li a").each(function(){
        if($(this)[0].href==String(window.location))
            $(this).parent().addClass("active");
            //console.log($(this)[0].href);
            //console.log($($(this))[0].href);
            console.log("so so so ... yeah~~ ");
    });
})


$(function(){
    $("button#btnshowinfo").click(function(){
        var message="                 Congratulation !!!";
        <!--获得文本框的值-->
        var oTextValue = $("#Textl").val();
        <!--获得单选框按钮值-->
        var oRdoValue = $('input:radio[name="rdoSex"]:checked').val();
        <!--获得复选框按钮值-->
        var oChkValue = $("#Checkboxl").is(":checked") ? "已婚" : "未婚";
        <!--显示提示文本元素和内容-->
        console.log("I am a log: Test Show Info");
        $("#divTip").html(oTextValue + ":" + oRdoValue + ":" + oChkValue + ":" + message);
    });
})




