var stateObj = {
	userLogged: null,
	userCurrConversation:null
};

var friends = null;

var basicURL    = "http://127.0.0.1:8000/home/";
var updInterval = 2000; 

$(document).ready(function(){
	init();
	updateMessages();
	checkAllUnreadMessages();
	$('.friend-container').click(function() {
		var url  = document.location.href;
		var surl = url.split("/");
		var uid  = parseInt(surl[surl.length-1]);
		var fid  = parseInt($(this).attr('id'));
		stateObj.userLogged = uid;
		stateObj.userCurrConversation = fid;
		$.ajax({
		  	url: "http://127.0.0.1:8000/home/" + uid + "/" + fid,
		  	context: document.body,
		  	dataType: "jsonp",
		}).done(function(response) {
			//console.log(response);
			console.log(fid);
		  	showMessages(response, uid, fid);
		});
	});
	$('#messagetype').keyup(function(e){
		if(e.keyCode == 13) {
			var msg = $(this).val();
			console.log(stateObj.userLogged + "/" + stateObj.userCurrConversation);
			$.ajax({
			  	url: "http://127.0.0.1:8000/home/" + stateObj.userLogged + "/" + stateObj.userCurrConversation + "/" + msg + "/",
			  	context: document.body,
			  	dataType: "jsonp",
			}).done(function(response) {
				console.log(response);
				console.log(fid);
			  	showMessages(response, uid, fid);
			});

			$(this).val('');
		}
	});
});

var showMessages = function(data, idSent, idRecv){
	$('.message-content-area').empty();
	var messages = data.messages;
	var html = "";
	for (m of messages) {
		html = "";
		if(m.whoSent_id == idSent ) {
			html = '<div class="card-panel blue-grey lighten-5 message-content user-message">';
			html += '<span class="blue-text text-darken-2">'+m.msg+'</span>';
			html += '</div>';
		} else {
			html = '<div class="card-panel blue-grey lighten-5 message-content friend-message">';
			html += '<span class="blue-text text-darken-2">'+m.msg+'</span>';
			html += '</div>';
		}
		$('.message-content-area').append(html);
	}
}

var updateMessages = function() {
	//if(stateObj.userCurrConversation == null) return;

	window.setInterval(function(){
		var url  = document.location.href;
		var surl = url.split("/");
		
		var uid  = parseInt(surl[surl.length-1]);
		var fid  = parseInt(stateObj.userCurrConversation);
		console.log(uid);
		console.log(fid);
		$.ajax({
			statusCode: {
			    404: function() {
			      alert( "page not found" );
			    }
			  },
		  	url: "/home/" + uid + "/" + fid,
		  	//context: document.body,
		  	//dataType: "json",

		}).done(function(response) {
			//console.log(response);
			console.log(fid);
		  	showMessages(response, uid, fid);
		}).fail(function(response) {
    		//console.log(response);
  });
		console.log("fim");
	},updInterval);

}

var checkAllUnreadMessages = function() {
	window.setInterval(function() {
		checkUnreadMessages(stateObj.userLogged);
	}, updInterval);
}

var checkUnreadMessages = function(id) {
	//for(f of friends) {
		//_checkUnreadMessages(id, f.id);
	//}
}

var _checkUnreadMessages = function(u1, u2) {
	console.log("http://127.0.0.1:8000/home/countUnreadMessages/" + u1 + "/" + u2 + "/");

	$.ajax({
		url: "http://127.0.0.1:8000/home/countUnreadMessages/" + u1 + "/" + u2 + "/",
		context: document.body,
		async: false,
		dataType: "jsonp"
	}).done(function(response) { 
		if((count = parseInt(response.count)) > 0) {
			if(count < 10)
				$('#' + u2 + ' .unread-msgs').html(count);
			else
				$('#' + u2 + ' .unread-msgs').html("+9");
			console.log('#' + u2)
		}
	});
}

var requestFriends = function(id, async = true) {
	console.log("http://127.0.0.1:8000/home/requestFrieds/" + id + "/");
	$.ajax({
		url: "http://127.0.0.1:8000/home/requestFrieds/" + id + "/",
		context: document.body,
		async:async,
		dataType: "jsonp"
	}).done(function(response) {
		//console.log(response);
		window.friends = response.friends;
	});	
}

var init = function() {
	var url  = document.location.href;
	var surl = url.split("/");
	var uid  = parseInt(surl[surl.length-1]);
	stateObj.userLogged = uid;
	console.log(uid);

	requestFriends(stateObj.userLogged, false);
	console.log(window.friends)
	//checkUnreadMessages(stateObj.userLogged);
}