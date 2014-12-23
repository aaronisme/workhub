$(function(){

    $.ajax({
        type: "GET",
        url: "/buildList",
        dataType: "json",
        success: function(data){
            $("#select").select2({
                width: 618,
                placeholder: "The first one in the dropdown list is the latest kit ",
                allowClear: true,
                data: data
            });
        }
    });

    $("#select").change(function(){
        var value = $("#select").select2("data")['text'];
        //跳转新页面
        window.open("static/build/"+value+".txt");
    });
});