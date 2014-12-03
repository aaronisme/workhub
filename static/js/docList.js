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

	$.ajax({
		type: "POST",
		url: "/data",
		data: {"requestType":"read","page": "doc", "data":cat},
		dataType: "json",
		success: function(data){
			// console.log(data);	
			if ( data.response == true && data.hasData == true ) {
				$("#DocContent").empty();
				for (var i = 0; i < data.data.length; i++) {
					$titleLength = data.data[i][2].length;
					$shortTitle = data.data[i][2].slice(0,20)+"...";
					$result = ($titleLength > 20)?$shortTitle:data.data[i][2];
					$("#DocContent").append('\
						<div class="col-sm-6 col-md-4 col-lg-3">\
          					<div class="thumbnail">\
            					<div class="caption">\
              						<h4>\
                					<a href="'+data.data[i][1]+'" target="_blank" title="'+data.data[i][2]+'" class="docTitle">'+$result+'</a>\
              						</h4>\
              						<h5><small>'+data.data[i][3]+'</small></h5>\
              						<p>'+data.data[i][5]+'</p>\
              						<small>'+data.data[i][4]+'</small>\
            					</div>\
            					<div class="bar" height="35">\
            						<img src="static/img/good.png" class="docGood">\
            						<span class="goodNum">'+data.data[i][6]+'</span>\
              						<a href="javascript:void(0);" index="'+i+'" id="'+data.data[i][0]+'" class="del">\
              							<img src="static/img/delete.png">\
              						</a>\
            					</div>\
          					</div>\
        				</div>\
						');
				};
				$("#DocContent").append('\
						<div class="col-sm-6 col-md-4 col-lg-3">\
          					<div class="thumbnail addDoc" style="padding:50px; height:220px;">\
          					<a href="addDoc.html">\
          						<img src="static/img/addDoc.png" width="120" height="120">\
          					</a>\
          					</div>\
        				</div>');
			};
			//tooltip
			$('.del').tooltip({
				placement: 'top',
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
					text: "You will delete the Doc whose Name is "+data.data[$index][1],   
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
        $id = $(this).next().next().attr("id");
        $num =$(this.).next().next("div.goodNum").text();
		$.ajax({
			type:"POST",
			url:/data,
			data:{ "data":"likenum","id": $id,"likenum":$num},
			dataType:"json",
			success: function(data){
				if ( data.response==true ) {
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