$(function(){
	$("#addVMSubmit").click(function(event){
                if((trim($("#inputIP").val()) == "") && (trim($("#inputUser").val()) == "") && (trim($("#inputBuild").val()) == "")){
                        sweetAlert("Sorry", "Fill the table!", "error");
                }else if(trim($("#inputIP").val()) == ""){
                        sweetAlert("Sorry", "IP should not be empty!", "error");
                }else if(trim($("#inputUser").val()) == ""){
                        sweetAlert("Sorry", "User should not be empty!", "error");
                }else if(trim($("#inputBuild").val()) == ""){
                        sweetAlert("Sorry", "Build should not be empty", "error");
                }else{
        		$.ajax({
                        type: "POST",
                        url:"./data",
                        data:$('#addVMForm').serialize(),
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
							window.location.href = "vm.html";
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
	});
function trim(str){ //删除左右两端的空格
　　     return str.replace(/(^\s*)|(\s*$)/g, "");
　　 }

});