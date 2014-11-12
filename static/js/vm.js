$(function(){
	$.ajax({
		type: "POST",
		url: "/data",
		data: {"data": "VM"},
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
								<td><a href="'+data.data[i][1]+'/ibmcognos">'+data.data[i][1]+'<a></td>\
								<td>'+data.data[i][2]+'</td>\
								<td>'+data.data[i][3]+'</td>\
								<td>'+data.data[i][4]+'</td>\
								<td>'+data.data[i][5]+'</td>\
								<td>\
								<a href="?'+data.data[i][0]+'" type="button" class="btn btn-primary btn-lg edit">\
								<span class="glyphicon glyphicon-wrench"></span>\
								</a>\
								<a href="?'+data.data[i][0]+'" type="button" class="btn btn-danger btn-lg del">\
								<span class="glyphicon glyphicon-remove"></span>\
								</a>\
								</td>\
							</tr>');
					};
			};
			//tooltip
			$('.edit').tooltip({
				placement: 'top',
				title: '编辑VM',
				trigger:'hover',
			});
			$('.del').tooltip({
				placement: 'top',
				title: '删除VM',
				trigger:'hover',
			});

		}
	});


});