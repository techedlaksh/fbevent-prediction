var margin = {top: 10, left: 10, bottom: 10, right: 10},
    width = parseInt(d3.select('#viz').style('width')),
    width = width - margin.left - margin.right,
    mapRatio = .5,
    height = width * mapRatio,
    mapRatioAdjuster = 50;
    nyc_center = [-74, 40.7];

//Define map projection
var projection = d3.geo.mercator()
                   .center(nyc_center)
                   .translate([width/2, height/2])
                   .scale(width * [mapRatio + mapRatioAdjuster]);

function resize() {
    // adjust things when the window size changes
    width = parseInt(d3.select('#viz').style('width'));
    width = width - margin.left - margin.right;
    height = width * mapRatio;

    // update projection
    projection.translate([width / 2, height / 2])
              .center(nyc_center)
              .scale(width * [mapRatio + mapRatioAdjuster]);

    // resize the map container
    svg.style('width', width + 'px')
       .style('height', height + 'px');

    // resize the map
    svg.selectAll("path").attr('d', path);
}

// adds zoom function to map
var zoom = d3.behavior.zoom()
                      .translate([0, 0])
                      .scale(1)
                      .scaleExtent([1, 10])
                      .on("zoom", zoomed);

// zoom function
function zoomed() {
  features.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
}

// when window size changes, resize the map
d3.select(window).on('resize', resize);

// create SVG element
var svg = d3.select("#viz")
            .append("svg")
            .attr("width", width)
            .attr("height", height)
            //Call zoom function on map
            .call(zoom);

//Define path generator
var path = d3.geo.path()
             .projection(projection);

//Group SVG elements together
var features = svg.append("g");

//Load TopoJSON data
d3.json("nyc_police_precincts-topojson.json", function(error, nyc) {

  if (error) return console.error(error);

  var subunits = topojson.feature(nyc, nyc.objects.nyc_police_precincts);

    //Bind data and create one path per TopoJSON feature
    features.selectAll("path")
    .data(topojson.feature(nyc, nyc.objects.nyc_police_precincts).features)
    .enter()
    .append("path")
    .attr("d", path)
    .attr("fill", "#e8d8c3")
    .attr("stroke", "#404040")
    .attr("stroke-width", .45)

    .on("mousemove", function(d) {
        
       //Update the tooltip position and value
       d3.select("#tooltip")
       .style("top", (d3.event.pageY) + 20 + "px")
       .style("left", (d3.event.pageX) + 20 + "px")
       .select('#precinct-number-tooltip')
       .text(d.properties.Precinct);   

       //Update province population in info box
       d3.select('#precinct-number')
       .text(d.properties.Precinct); 

       //Show the tooltip
       d3.select("#tooltip").classed("hidden", false);
       })
    
       .on("mouseout", function() {
       //Hide the tooltip
       d3.select("#tooltip").classed("hidden", true);
       });      
});