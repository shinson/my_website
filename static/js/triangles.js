var colorsOdd = ["#152934", "#128EA8", "#3C6B75", "#559AA8", "none"]

var colorsEven = ["#45818E", "#7890CD", "none"]

function Draw(){

var w = 1650;
var h = window.innerHeight;
var triangle = d3.symbol().type(d3.symbolTriangle);
var spaceW = 24,
  spaceWOpp = 0,
  spaceH = 30,
  spaceHOpp = 16,
  spaceHBtwn = 42,
  size = 1050;

var svg = d3.select('#triangles')
  .append('svg')
  .attr('width', w)
  .attr('height', h);

rows = _.range(h / 20);
columns = _.range(w / 24);

function getColorO() {
  return colorsOdd[Math.floor(Math.random() * colorsOdd.length)];
}

function getColorE() {
  return colorsEven[Math.floor(Math.random() * colorsEven.length)];
}

_.forEach(rows, function(i) {
  _.forEach(columns, function(j) {
    if (j % 2 === 0) {
      svg.append("path")
        .attr("class", "pathEven")
        .attr("d", triangle.size(size))
        .attr("transform", "translate(" + spaceW * j + "," + ((i * spaceHBtwn) + spaceH) + ") rotate(180)")
        .transition()
        .duration(4000)
        .attr("transform", "translate(" + spaceW * j  + "," + ((i * spaceHBtwn) + spaceH) + ") rotate(360)")
        .attr('fill', getColorE)
        .attr('opacity', 1);
      
    } else {
      svg.append("path")
        .attr("class", "pathOdd")
        .attr("d", triangle.size(size))
        .attr("transform", "translate(" + (spaceW + spaceWOpp) * j + "," + ((i * spaceHBtwn) + spaceHOpp) + ") rotate(180)")
        .attr('fill', getColorO)
        .attr('opacity', 1);
    }
  });
});
}

Draw();
