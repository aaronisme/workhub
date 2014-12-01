$(function(){
	$.ajax({
		type: "POST",
		url: DOCADDR,
		data: {"requestType":"read","data": "DOC"},
		dataType: "json",
		success: function(data){
			// console.log(data);	
			if ( data.response == true && data.hasData == true ) {
				$("#DocContent").empty();
				$("#DocContent").append('\
					<table class="table table-hover">\
						<thead>\
							<tr>\
								<th>Doc Name</th>\
								<th>Owner</th>\
								<th>Upload Time</th>\
								<th>Description</th>\
								<th>Good</th>\
								<th class="docOpt">Option</th>\
							</tr>\
						</thead>\
						<tbody id="Doctbody">\
						</tbody>\
					</table>');
					for (var i = 0; i < data.data.length; i++) {	
						$("#Doctbody").append('\
							<tr>\
								<td><a href="#">'+data.data[i][1]+'</a></td>\
								<td>'+data.data[i][2]+'</td>\
								<td>'+data.data[i][3]+'</td>\
								<td>'+data.data[i][4]+'</td>\
								<td>\
								<img src="./img/good.png" class="docGood">\
								<span class="goodNum">'+data.data[i][5]+'</span>\
								</td>\
								<td class="docOpt">\
								<a href="javascript:void(0);" index="'+i+'" id="'+data.data[i][0]+'" type="button" class="btn btn-danger btn-xs del">\
								<span class="glyphicon glyphicon-remove"></span>\
								</a>\
								</td>\
							</tr>');
					};
			};
			//tooltip
			$('.del').tooltip({
				placement: 'right',
				title: '删除Doc',
				trigger:'hover',
			});
			$('.addDoc').tooltip({
				placement: 'top',
				title: '添加Doc',
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
							window.location.href = DOCDELADDR+"?requestType=delete&page=doc&data="+$id;
						} 
					});
			});

		}
	});

	$("#DocContent").delegate(".docGood", "click", function(){
		$self = $(this);
		$.ajax({
			type:"POST",
			url:DOCADDR,
			data:{ "author": "sunny"},
			dataType:"json",
			success: function(data){
				if ( data.response==false ) {
					$score = $self.next().text();
					$newScore = parseInt($score)+1;
					$self.next().text($newScore);
				}else{
					sweetAlert("Oops...", "骚年，你已经赞过了哟~", "error");
				}
			},
			error: function(){
				sweetAlert("Oops...", "请求木有发过去~", "error");
			}
		});



	});




});