// declarations, setup SVG
var box_width = 800;
var svg = d3.select('#work_exp').append('svg')
    .attr('height', 600).attr('width', 800);

// set up groups
var workgroup = svg.selectAll('g')
    .data(work_exp).enter().append('g');

// create a box for each employment
var employer = workgroup.append('rect')
    .attr('height', 200).attr('width', box_width)
    .attr('fill', '#4b4b50')
    .attr('x', 0)
    .attr('y', function(d,i){
        return i*210
    });

// job title
var title = workgroup.append('text')
    .style('text-anchor', 'left')
    .attr('fill', 'white')
    .attr('x', 10)
    .attr('y', function(d,i){
        return i*210+25
    })
    .attr('font-family', 'roboto')
    .attr('font-size', '1.4em')
    .text(function(d) { return d.title; });

// company
var company = workgroup.append('text')
    .style('text-anchor', 'left')
    .attr('fill', 'white')
    .attr('x', 30)
    .attr('y', function(d,i){
        return i*210+50
    })
    .attr('font-family', 'roboto')
    .attr('font-size', '1.0em')
    .text(function(d) { return d.company; });

// years worked
var years = workgroup.append('text')
    .style('text-anchor', 'right')
    .attr('fill', 'white')
    .attr('x', box_width-175)
    .attr('y', function(d,i){
        return i*210+25
    })
    .attr('font-family', 'roboto')
    .attr('font-size', '1.1em')
    .text(function(d) {
        var str = d.start_month + ' ' + d.start_year + ' - ';
        if (d.end_year == null) {str = str + 'present';}
        else {str = str + d.end_month + ' ' + d.end_year;}
        return str;
    });
