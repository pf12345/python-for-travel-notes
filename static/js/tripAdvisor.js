(function() {
	var _photoJson = {};
	window.daodao = {
		trip: {
			addPhotos: function(photoJson) {
				for(var key in photoJson) {
					_photoJson[key] = photoJson[key].url;
				}
				console.log(photoJson);
			}
		}
	}
	$(document).ready(function() {
		var getSpanIds = function() {
			var spans = $('span[data-type="image"]');
			spans.each(function(index, item){
				var _id = $(this).attr('data-id');
				if(_id && _photoJson[_id]) {
					$(this).html('<img src="'+_photoJson[_id]+'"/>')
				}
				console.log(item)
			})
			console.log(_photoJson)
		}
		getSpanIds();
	})
	
})()