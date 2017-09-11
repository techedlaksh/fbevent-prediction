'use strict';

function dataset_colors(cat){
  if( cat == "art"){
    var dataset = [1, 1, 1, 1, 1];
  }
  else if (cat == "food"){
    var dataset = [1, 1, 2, 1, 3];
  } 

// let colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd'];
// let colors = ['#67001f', '#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#e0e0e0', '#bababa', '#878787', '#4d4d4d', '#1a1a1a'];
var colors = ['#9e0142', '#d53e4f', '#f46d43', '#fdae61', '#fee08b',];
var names = ['travel', 'food', 'music', 'art', ' education'];
var combined = [dataset, colors, names];
console.log(combined);
return combined;
// ,  '#e6f598', '#abdda4', '#66c2a5', '#3288bd', '#5e4fa2'];
};


var draw = function draw(cat) {

  

  var combined = dataset_colors(cat);
  var dataset = combined[0];
  var colors = combined[1];
  var names = combined[2];
  console.log(dataset);
  svg.append("g").attr("class", "lines");
  svg.append("g").attr("class", "slices");
  svg.append("g").attr("class", "labels");

  // define slice
  var slice = svg.select('.slices').datum(dataset).selectAll('path').data(pie);
  slice.enter().append('path').attr({
    'fill': function fill(d, i) {
      return colors[i];
    },
    'd': arc,
    'stroke-width': '25px',
    'transform': function transform(d, i) {
      return 'rotate(-180, 0, 0)';
    }
  }).style('opacity', 0).transition().delay(function (d, i) {
    return i * arcAnimDelay + initialAnimDelay;
  }).duration(arcAnimDur).ease('elastic').style('opacity', 1).attr('transform', 'rotate(0,0,0)');

  slice.transition().delay(function (d, i) {
    return arcAnimDur + i * secIndividualdelay;
  }).duration(secDur).attr('stroke-width', '5px');

  var midAngle = function midAngle(d) {
    return d.startAngle + (d.endAngle - d.startAngle) / 2;
  };

  var text = svg.select(".labels").selectAll("text").data(pie(dataset));

  text.enter().append('text').attr('dy', '0.35em').style("opacity", 0).style('fill', function (d, i) {
    return colors[i];
  }).text(function (d, i) {
    return names[i];
  }).attr('transform', function (d) {
    // calculate outerArc centroid for 'this' slice
    var pos = outerArc.centroid(d);
    // define left and right alignment of text labels 							
    pos[0] = radius * (midAngle(d) < Math.PI ? 1 : -1);
    return 'translate(' + pos + ')';
  }).style('text-anchor', function (d) {
    return midAngle(d) < Math.PI ? "start" : "end";
  }).transition().delay(function (d, i) {
    return arcAnimDur + i * secIndividualdelay;
  }).duration(secDur).style('opacity', 1);

  var polyline = svg.select(".lines").selectAll("polyline").data(pie(dataset));

  polyline.enter().append("polyline").style("opacity", 0.5).attr('points', function (d) {
    var pos = outerArc.centroid(d);
    pos[0] = radius * 0.95 * (midAngle(d) < Math.PI ? 1 : -1);
    return [arc.centroid(d), arc.centroid(d), arc.centroid(d)];
  }).transition().duration(secDur).delay(function (d, i) {
    return arcAnimDur + i * secIndividualdelay;
  }).attr('points', function (d) {
    var pos = outerArc.centroid(d);
    pos[0] = radius * 0.95 * (midAngle(d) < Math.PI ? 1 : -1);
    return [arc.centroid(d), outerArc.centroid(d), pos];
  });
};

draw("art");

var button = document.querySelector('button');

function empty(cat){
  // do nothing
};

var replay = function(cat) {

  d3.selectAll('.slices').transition().ease('back').duration(100).delay(0).style('opacity', 0).attr('transform', 'translate(0, 250)').remove();
  d3.selectAll('.lines').transition().ease('back').duration(100).delay(100).style('opacity', 0).attr('transform', 'translate(0, 250)').remove();
  d3.selectAll('.labels').transition().ease('back').duration(100).delay(200).style('opacity', 0).attr('transform', 'translate(0, 250)').remove();
  console.log(cat);
  // draw(cat);
};

function doublefunction(){
  draw('food');
  replay('art');
}