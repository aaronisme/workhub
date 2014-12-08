$(function(){

    $("#UFdiv").hide();
    $("#LA").click(function(event) {
        $("#UFdiv").hide();
        $("#LAdiv").show();
    });
    $("#UF").click(function(event) {
        $("#UFdiv").show();
        $("#LAdiv").hide();
    });

    uploadbutton = $("#addDocSubmit");

      $('#fileupload').fileupload({
          type:"POST",
          url: "/data",
          autoUpload:false,
          dataType: 'json',
          done: function (e, data) {
              if ( data.result.response==true ) {
                  $("#uploadId").val(data.result.uploadId);
              }else{
                  sweetAlert("Oops...", "Upload Failed!", "error");
              };
        }
    }).on('fileuploadadd', function (e, data) {
        uploadbutton.data = data

    });




    uploadbutton.on('click',function(){
        data = uploadbutton.data;
        data.submit().always(function () {
            $this.remove();
        });
    });


    function sendInfo(){
        var $this = $(this),
        data = $this.data();
    }

    //删除左右两端的空格
    function trim(str){ 
        return str.replace(/(^\s*)|(\s*$)/g, "");
    }

});