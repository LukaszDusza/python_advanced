$(function(){
	$('#btn-submit').click(function(){
		$.ajax({
			url: '/register-car',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

$(function() {
    $.ajax({
        url: '/cars',
        type: 'GET',
        success: function(json) {
            console.log("json");
        },
        error: function(error){
            console.log(error);
        }
    });
})
