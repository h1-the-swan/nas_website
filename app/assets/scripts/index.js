const projects = require('./projects.json');

projects.forEach(function(item) {
	var p = $('#project-item-template').clone();
	p.find('img').attr('src', STATIC_FOLDER_ROOT + '/img/' + item.img).attr('alt', item.img_alt);
	var $name = $('<a>').attr('href', SCRIPT_ROOT + item.url);
	$name.append($('<h5>').html(item.name))
	p.find('.project-name').append($name);
	p.find('.project-description').append($('<p>').html(item.description));
	$('#projects').append(p.show());
});
