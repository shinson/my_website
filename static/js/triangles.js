var colorsOdd = ["#152934", "#3C6B75", "#559AA8", "none", "none"]

var colorsEven = ["#45818E", "#7890CD", "none", "none"]

function Draw(){

var w = window.innerWidth;
var h = window.innerHeight;
var triangle = d3.symbol().type(d3.symbolTriangle);
var spaceW = 76,
  spaceWOpp = 0,
  spaceH = 150,
  spaceHOpp = 107,
  spaceHBtwn = 130,
  size = 10050;

var svg = d3.select('#triangles')
  .append('svg')
  .attr('width', w)
  .attr('height', h)
  .attr('opacity', 0.2);

rows = _.range(h / 170);
columns = _.range(w / 75);

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
        .attr('fill', (j%4===0)? 'none':getColorE);
      
    } else {
      svg.append("path")
        .attr("class", "pathOdd")
        .attr("d", triangle.size(size))
        .attr("transform", "translate(" + (spaceW + spaceWOpp) * j + "," + ((i * spaceHBtwn) + spaceHOpp) + ") rotate(180)")
        .attr('fill', (j%3===0)? 'none':getColorO);
    }
  });
});
}

Draw();
