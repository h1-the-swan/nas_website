var NodeLinkCoauthorshipVis = nodelink_vis_coauthorship.NodeLinkCoauthorshipVis;

var activateTooltips = nodelink_vis_coauthorship.activateTooltips;

var nodelinkvis;

console.log(data_fname);
d3.json(data_fname).then(function(graph) {
	var sel = d3.select('#mainVis');
	nodelinkvis = new NodeLinkCoauthorshipVis({data: graph, el: sel});
	activateTooltips();
	labelImportantNodes();

});

function labelImportantNodes() {
	var topN = 10;
	var x = d3.selectAll('.node')
		.sort(function(a, b) {
			return d3.descending(a.flow, b.flow)
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
