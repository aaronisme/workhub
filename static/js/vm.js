$(function(){
	$.ajax({
		type: "POST",
		url: "/data",
		data: {"requestType":"read", "page": "vm","data":"all"},
		dataType: "json",
		success: function(data){
			// console.log(data);
			if ( data.response == true && data.hasData == true ) {
				$("#VMContent").empty();
				$("#VMContent").append('\
					<table class="table table-hover">\
						<thead>\
							<tr>\
								<th>IP</th>\
								<th>User</th>\
								<th>Occupied Time</th>\
								<th>Build</th>\
								<th>Description</th>\
								<th>Option</th>\
							</tr>\
						</thead>\
						<tbody id="VMtbody">\
						</tbody>\
					</table>');
					for (var i = 0; i < data.data.length; i++) {	
						$("#VMtbody").append('\
							<tr>\
								<td><a href="http://'+data.data[i][1]+'/ibmcognos">'+data.data[i][1]+'<a></td>\
								<td>'+data.data[i][2]+'</td>\
								<td>'+data.data[i][3]+'</td>\
								<td>'+data.data[i][4]+'</td>\
								<td>'+data.data[i][5]+'</td>\
								<td>\
								<a href="/editVM?id='+data.data[i][0]+'" type="button" class="btn btn-primary btn-lg edit">\
								<span class="glyphicon glyphicon-wrench"></span>\
								</a>\
								<a href="javascript:void(0);" index="'+i+'" id="'+data.data[i][0]+'" type="button" class="btn btn-danger btn-lg del">\
								<span class="glyphicon glyphicon-remove"></span>\
								</a>\
								</td>\
							</tr>');
					};
			};
			//tooltip
			$('.edit').tooltip({
				placement: 'left',
				title: '编辑VM',
				trigger:'hover',
			});
			$('.del').tooltip({
				placement: 'right',
				title: '删除VM',
				trigger:'hover',
			});
			$('.addVM').tooltip({
				placement: 'top',
				title: '添加VM',
				trigger:'hover',
			});

			$(".del").click(function(event){
				$index = $(this).attr("index");
				$id = $(this).attr("id");
				swal({   
					title: "Are you sure?",   
					text: "You will delete the VM whose IP is "+data.data[$index][1],   
					type: "warning",   
					showCancelButton: true,   
					confirmButtonColor: "#DD6B55",   
					confirmButtonText: "Yes, delete it!",   
					cancelButtonText: "No, cancel plx!",   
					closeOnConfirm: false,   
					closeOnCancel: true }, 
					function(isConfirm){   
						if (isConfirm) {     
								$.ajax({
		                                  type: "POST",
		                                  url: "/data",
                                          data: {"data": $id, "requestType":"delete","page":"vm"},
                                          dataType: "json",
                                          success: function(data){
                                                if(data.response == true && data.success == true){
                                                    window.location.href = "/vm";
                                                }
                                          }
                                        });

						}
					});
			});

		}
	});
});