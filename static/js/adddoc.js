$(function(){

    var addr = window.location.search;
    function GetRequest(addr) {
        var url = addr;
        var theRequest = new Object();
        if(url.indexOf("?") != -1) {
            var str = url.substr(1);
            strs = str.split("&");
            for(var i = 0; i < strs.length; i++) {
                theRequest[strs[i].split("=")[0]] = (strs[i].split("=")[1]);
            }
        }
        return theRequest;
    }
    var Request = new Object();
    Request = GetRequest(addr);
    var cat = Request["cat"];

    /*$("#UFdiv").hide();
    $("#LA").click(function(event) {
        $("#UFdiv").hide();
        $("#LAdiv").show();
    });
    $("#UF").click(function(event) {
        $("#UFdiv").show();
        $("#LAdiv").hide();
    });*/

    $("#inputCat").val(cat);
    $("#addDocSubmit").next().attr("href",("/docList?cat=" + cat))
    uploadbutton = $("#addDocSubmit");

      $('#fileupload').fileupload({
          type:"POST",
          url: "/data",
          autoUpload:false,
          dataType: 'json',
          done: function (e, data) {
              console.log(data);
              if(data.result.response == true && data.result.success == true){
                  swal({
                        title:"Successfully!",
                        type:"success",
                        showCancelButton:false,
                        confirmButtonColor:"#AEDEF4",
                        confirmButtonText:"OK",
                        closeOnConfirm:false
                        },
                        function(isConfirm){
						    if (isConfirm) {
							    window.location.href = "/docList?cat=" + cat;
						}
        				});
              }else{
                  swal({
                        title:"failed",
                        type:"error",
                        showCancelButton:false,
                        confirmButtonColor:"#AEDEF4",
                        confirmButtonText:"OK",
                        closeOnConfirm:true
                       });
              }
        }
    }).on('fileuploadadd', function (e, data) {
        uploadbutton.data = data;
        $("#inputName").val(data.files[0].name.split(".")[0]);
    });



    uploadbutton.on('click',function(){

        if ( (trim($("#inputName").val())=="") || (trim($("#inputOwner").val())=="") ) {
                sweetAlert("Sorry", "Upload File,Doc Name and Owner should not be empty!", "error");
            }else{
                    var data = uploadbutton.data;
                    data.submit();
            };


    });



    //删除左右两端的空格
    function trim(str){
        return str.replace(/(^\s*)|(\s*$)/g, "");
    }

});