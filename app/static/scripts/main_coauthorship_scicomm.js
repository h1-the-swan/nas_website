var NodeLinkCoauthorshipVis = nodelink_vis_coauthorship.NodeLinkCoauthorshipVis;

var activateTooltips = nodelink_vis_coauthorship.activateTooltips;

var fuseOptions = {
	id: "id",
	shouldSort: true,
	threshold: 0.3,
	location: 0,
	distance: 100,
	maxPatternLength: 32,
	minMatchCharLength: 1,
	keys: [
		"author_name",
		"affil_name"
	]
};

var nodelinkvis;

// d3.json("data/test_coauthorship_graph.json").then(function(graph) {
// d3.json("./data/cl1-594_min5.json").then(function(graph) {
// var params = new URLSearchParams(window.location.search);
// var filename = params.get('fn');
// if (filename === null) {
// 	filename = ".data/science_communication_papers_plus_extended_relevant_coauthor.json";
// }
d3.json(data_fname).then(function(graph) {
	var sel = d3.select('#chartDiv');
	console.log(sel);
	// for (var i = 0, len = graph.nodes.length; i < len; i++) {
	// 	var removed = [];
	// 	// graph.nodes[i].papers = [];
	// 	if (graph.nodes[i].affil_name === null) {
	// 		graph.nodes[i].affil_name = "";
	// 	}
    //
	// 	var affil_pos = null;
	// 	for (var j = 0; j < 10; j++) {
	// 		if (graph.nodes[i].affil_name === graph.graph.top_affiliations[j]) {
	// 			affil_pos = j;
	// 		}
	// 		// 'other' case for less popular affilations:
	// 		if (affil_pos === null) {
	// 			affil_pos = 10;
	// 		}
	// 		graph.nodes[i].color_group = affil_pos;
	// 	}
	// }
	// nodelinkvis = new NodeLinkCoauthorshipVis({data: graph, el: sel, forceStrength: -50});
	nodelinkvis = new NodeLinkCoauthorshipVis({data: graph, el: sel});
	// nodelinkvis = new NodeLinkCoauthorshipVis().width(960)
	// 	.data(graph);
	// d3.select("#chartDiv").call(nodelinkvis);
	// // nodelinkvis.data(graph);
    //
		console.log(nodelinkvis.color(16));
	activateTooltips();
	labelImportantNodes();

	// post-hoc tooltip manipulation (hack)
	d3.selectAll('.node circle').each(function(d) {
		var $tooltipNode = $(this._tippy.popper);
		// $tooltipNode.find('.paper_titles h5').text('Papers (' + d.number_of_papers + '):')
		$tooltipNode.find('.paper_titles').empty();
	});

	d3.selectAll(".node")
		.each(function(d) { 
			$(this).addClass("au_" + d.id );
			console.log(d.color);
		});

	// var mapOpts = {
	// 	data: graph.graph.institutions,
	// 	el: d3.select("#mapDiv"),
	// 	width: 500,
	// }
	// var mapVis = new LeafletD3PointMap(mapOpts);
	// // $('#mapDiv circle').css("z-index", 1000);
	// d3.selectAll("#mapDiv circle")
	// 	.style("pointer-events", "auto")
	// 	.each(function(d) { 
	// 		var tippyInstance = tippy(this); 
	// 		var toolTipContent = d.NAME;
	// 		toolTipContent = toolTipContent + ", " + d.CITY;
	// 		if (d.STATE !== "" && d.STATE !== "NONE") {
	// 			toolTipContent = toolTipContent + ", " + d.STATE;
	// 		}
	// 		toolTipContent = toolTipContent + ", " + d.COUNTRY;
	// 		tippyInstance.setContent(toolTipContent);
	// 	})
	// 	.on("mouseover", function(d) {
	// 		unfocusVis();
	// 		d3.selectAll(".node")
	// 			.filter(function(node) { return node.affil_id.includes(d.ID); })
	// 			.each(function(node) { focusAuthor(node.id); });
	// 	});

	// var $allAffil = $('#collection-card').find('.affilList');
	// for (var i = 0; i < 10; i++) {
	// 	$allAffil.append('<li>' + graph.graph.top_affiliations[i] + '</li>');
	// }
	// var $allConcepts = $('#collection-card').find('.conceptsList');
	// for (var i = 0; i < 10; i++) {
	// 	$allConcepts.append('<li>' + graph.graph.top_concepts[i] + '</li>');
	// }

	graph.nodes.sort(function(a, b) { return d3.descending(a.flow, b.flow); })
	var authorsCardList = d3.select("#authorsCardList")
							.selectAll("li")
							.data(graph.nodes, function(d) { return d.id; })
							.enter().append("li")
							.attr("class", function(d) { return "au_" + d.id; })
							.on("mouseover", function(d) { focusSingleAuthor(d.id); });
	// authorsCardList.append("img")
	// 			.attr("src", function(d) { return 'https://assets.beta.meta.org/images/authors/' + d.id + '.jpg'})
	// 			.attr("class", "rounded-circle")
	authorsCardList.append("p")
				.text(function(d) { return d.author_name });

	d3.selectAll('.node').on('mouseover', function(d) {
		focusSingleAuthor(d.id);
	});
		

});

// setTimeout(function() {
// 	d3.json("data/test_coauthorship_graph_misinfo_max600.json").then(function(graph) {
// 		nodelinkvis.data(graph);
// 		activateTooltips();
// 	});
// }, 3000);

// function applyRadioSelection() {
// 	var val = $( 'input[type=radio][name=nodelab-radio]:checked' ).val();
// 	console.log(val);
// 	$( '.node' ).find( 'text' ).hide();
// 	if (val !== 'none') {
// 		$( '.node.focus' ).find( '.' + val ).show();
// 	}
// }

function labelImportantNodes() {
	var topN = 10;
	var x = d3.selectAll('.node')
		.sort(function(a, b) {
			return d3.descending(a.flow, b.flow)
			// return d3.descending(a.number_of_papers, b.number_of_papers)
		})
		.filter(function(d, i) { return i<topN; })
		.append('g').attr("class", "label-important");
		// .each(function(d) {
		// 	console.log(d);
		// 	var instance = tippy(this)
		// 	instance.setContent('ddd');
		// 	instance.show();
		// });
	x.append("circle").attr("r", 0.0001).style("visible", "hidden")
		.each(function(d) {
			var instance = tippy(this, {
				// animation: "scale",
				placement: "right",
				duration: 0,
				delay: 0,
				distance: 10,
				hideOnClick: false,
				interactive: true,
				trigger: "manual",
				appendTo: document.getElementById("chartDiv"),
				theme: "label-important",
				showOnInit: true,
				sticky: true,  // move around with the nodes
				updateDuration: 0,
				content: d.author_name,
			});
			// instance.show();
		});
	// x.append('text').text(function(d) { return d.author_name; });
}

function focusSingleAuthor(author_id) {
	// change the focus to a new author
	unfocusVis();
	focusAuthor(author_id);

	$('#authorsCardList li').removeClass('focus-author');
	$('#authorsCardList li.au_' + author_id).addClass('focus-author');

	clearAuthorCard();
	fillAuthorCard(author_id);
}

function focusAuthor(author_id) {
	
	$('.node.au_' + author_id).find('circle').addClass('highlight-primary');

	d3.selectAll("line.link")
		.filter(function(d) { return d.source.id === author_id; })
		.classed("highlight-primary", true)
		.each(function(d) {
			$('.node.au_' + d.target.id).find('circle').addClass('highlight-secondary');
		});
	d3.selectAll("line.link")
		.filter(function(d) { return d.target.id === author_id; })
		.classed("highlight-primary", true)
		.each(function(d) {
			$('.node.au_' + d.source.id).find('circle').addClass('highlight-secondary');
		});
}

function unfocusVis() {
	// remove any focus from visualizations
	$('.node circle').removeClass('highlight-primary');
	$('.node circle').removeClass('highlight-secondary');
	$('line.link').removeClass('highlight-primary');
}

function fillAuthorCard(author_id) {
	d3.select(".node.au_" + author_id).each(function(d) {
		$authorCard = $('#author-card');
		$authorCard.find('.au-card-name').text(d.author_name);
		$authorCard.find('.au-card-img').attr('src', 'https://assets.beta.meta.org/images/authors/' + d.id + '.jpg');
		// $authorCard.find('.au-card-affil').text("Last Affiliation: " + d.affil_name);

		// $conceptsList = $authorCard.find('.au-card-concepts');
		// $conceptsList.append("<h5>Top Concepts</h5>");
		// $conceptsList.append("<ol></ol>");
		// for (var i = 0; i < 5; i++) {
		// 	$conceptsList.find('ol').append('<li>' + d.top_concepts[i] + '</li>');
		// }

		$papersList = $authorCard.find('.au-card-papers');
		$papersList.append("<h5>Top Papers</h5>");
		$papersList.append("<ol></ol>");
		d.papers.sort(function(a, b) {
			return d3.descending(a.ef, b.ef);
		});
		for (var i = 0; i < d.papers.length; i++) {
			// $papersList.find('ol').append('<li>' + d.papers[i].title + ' (' + d.papers[i].YEAR + ')</li>');
			// No year right now
			$papersList.find('ol').append('<li>' + d.papers[i].title + '</li>');
		}
	});
}

function clearAuthorCard() {
	$authorCard = $('#author-card');
	$authorCard.find('.au-card-name').empty();
	$authorCard.find('.au-card-affil').empty();
	$authorCard.find('.au-card-concepts').empty();
	$authorCard.find('.au-card-papers').empty();
}

$( document ).ready(function() {
	// var $nodelabRadio = $( 'input[type=radio][name=nodelab-radio]' );
	// $nodelabRadio.change( applyRadioSelection );

	
})
