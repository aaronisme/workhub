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

    $('#fileupload').fileupload({
        url: ADDDOCADDR,
        dataType: 'json',
        done: function (e, data) {
            if ( data.result.response==true ) {
                $("#uploadId").val(data.result.uploadId);
            }else{
                sweetAlert("Oops...", "Upload Failed!", "error");
            };
        }
    });

    $("#addDocSubmit").click(function(event){
        if ( $("#LA")[0].checked ) {
            if ( (trim($("#inputLink").val())=="") || (trim($("#inputName").val())=="") || (trim($("#inputOwner").val())=="") ) {
                sweetAlert("Sorry", "Link Addr,Doc Name and Owner should not be empty!", "error");
            }else{
                sendInfo();
            };
        };
        if ( $("#UF")[0].checked ) {
            if ( (trim($("#uploadId").val())=="") || (trim($("#inputName").val())=="") || (trim($("#inputOwner").val())=="") ) {
                sweetAlert("Sorry", "Upload File,Doc Name and Owner should not be empty!", "error");
            }else{
                sendInfo();
            };
        };
    });

    function sendInfo(){
        $.ajax({
                type: "POST",
                url:"./fake2.json",
                data:$('#addDocForm').serialize(),
                success: function(data) {
                    console.log(data);
                    if(data.response == true && data.success == true){
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
                    window.location.href = "docList.html";
                }
                        }); 
                    }else{
                        swal({
                            title:data.errorInfo,
                            type:"error",
                            showCancelButton:false,
                            confirmButtonColor:"#AEDEF4",
                            confirmButtonText:"OK",
                            closeOnConfirm:true
                        });
                    }
                }                    
        });
    }

    //删除左右两端的空格
    function trim(str){ 
        return str.replace(/(^\s*)|(\s*$)/g, "");
    }

});