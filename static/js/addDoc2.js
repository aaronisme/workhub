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

        if ( $("#LA")[0].checked ) {
            if ( (trim($("#inputLink").val())=="") || (trim($("#inputName").val())=="") || (trim($("#inputOwner").val())=="") ) {
                sweetAlert("Sorry", "Link Addr,Doc Name and Owner should not be empty!", "error");
            }else{

                data = uploadbutton.data;
                data.submit();
            };
        };
        if ( $("#UF")[0].checked ) {
            if ( (trim($("#uploadId").val())=="") || (trim($("#inputName").val())=="") || (trim($("#inputOwner").val())=="") ) {
                sweetAlert("Sorry", "Upload File,Doc Name and Owner should not be empty!", "error");
            }else{
                 data = uploadbutton.data;
                 data.submit();
            };
        };




        data = uploadbutton.data;
        data.submit();
    });


    //删除左右两端的空格
    function trim(str){ 
        return str.replace(/(^\s*)|(\s*$)/g, "");
    }

});