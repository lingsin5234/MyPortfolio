// declarations, setup SVG
var box_width = 800;
var box_height = 200; // change to depend on length of work_desc
var svg = d3.select('#work_exp').append('svg')
    .attr('height', 600).attr('width', box_width);
var local = d3.local();

// set up groups
var workgroup = svg.selectAll('g')
    .data(work_exp).enter().append('g');

// create a box for each employment
var employer = workgroup.append('rect')
    .attr('height', 200).attr('width', box_width)
    .attr('fill', '#4b4b50')
    .attr('x', 0).attr('y', function(d,i){
        return i*210
    });

// job title
var title = workgroup.append('text')
    .style('text-anchor', 'left')
    .attr('fill', 'white')
    .attr('x', 10).attr('y', function(d,i){
        return i*210+25
    }).attr('font-family', 'roboto')
    .attr('font-size', '1.4em')
    .text(function(d) { return d.title; });

// company
var company = workgroup.append('text')
    .style('text-anchor', 'left')
    .attr('fill', 'white')
    .attr('x', 30).attr('y', function(d,i){
        return i*210+50
    }).attr('font-family', 'roboto')
    .attr('font-size', '1.0em')
    .text(function(d) { return d.company; });

// years worked
var years = workgroup.append('text')
    .style('text-anchor', 'right')
    .attr('fill', 'white')
    .attr('x', box_width-175).attr('y', function(d,i){
        return i*210+25
    }).attr('font-family', 'roboto')
    .attr('font-size', '1.1em')
    .text(function(d) {
        var str = d.start_month + ' ' + d.start_year + ' - ';
        if (d.end_year == null) {str = str + 'present';}
        else {str = str + d.end_month + ' ' + d.end_year;}
        return str;
    });

// call the workgroup box then for EACH work_exp, get the work_desc
var test = workgroup.append("svg")
    .attr('height', box_height).attr('width', box_width-20)
    .attr('x', 0).attr('y', function(d,i) {
        return i * 170 + 40
    })
    .append("g")
    .selectAll("text")
    .data( function(d,i) {
        // this part calls the work_desc for EACH work_exp
        local.set(this, i)
        return d.work_desc;
    })
    .enter()
    .append("text")
        .style('text-anchor', 'left')
        .attr('fill', 'white')
        // local.get(this) gets the current index in current array; != parent index (i)
        .attr("x", function(d,i) { return local.get(this) + 10; })
        .attr("y", function(d,i) { return (i * 22) + 75; })
        .attr('font-size', '0.9em')
        .text( function(d,i) { return d; });
