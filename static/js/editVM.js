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
	var id = Request["id"];

	$.ajax({
		type: "POST",
		url: "./fake1.json",
		data: {"data": id, "requestType":"read"},
		dataType: "json",
		success: function(data){
			var showdata = data.data[id-1];
			//console.log(showdata[1]);
			$("#inputIP").val(showdata[1]);
			$("#inputUser").val(showdata[2]);
			$("#inputOccupied").val(showdata[3]);
			$("#inputBuild").val(showdata[4]);
			$("#inputDescription").val(showdata[5]);
		}
	});

	$("#inputID").val(id);

	$("#editVMSubmit").click(function(event){
		if(($("#inputUser").val() == "") && ($("#inputBuild").val() == "")){
            sweetAlert("Sorry", "User & Build should not be empty!", "error");
		}else if($("#inputUser").val() == ""){
			sweetAlert("Sorry", "User should not be empty!", "error");
		}else if($("#inputBuild").val() == ""){
			sweetAlert("Sorry", "Build should not be empty!", "error");
		}else{
			$.ajax({
	                type: "POST",
	                url:"./fake2.json",
	                data:$('#editVMForm').serialize(),
	                success: function(data) {
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
});