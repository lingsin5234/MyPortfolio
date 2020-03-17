// declarations
// current setup as 75 offset to the descriptions with descriptions 22 apart
// var box_height = 200;
var box_height = 75;
var num_edu = education.length;

// setup SVG
var svg = d3.select('#education').append('svg')
    .attr('height', num_edu * (box_height + 10)).attr('width', box_width);

// set up groups
var edu_group = svg.selectAll('g')
    .data(education).enter().append('g');

// create a box for each education
var education = edu_group.append('rect')
    .attr('height', box_height).attr('width', box_width)
    .attr('fill', '#BC986A')
    .attr('x', 0).attr('y', function(d,i){
        return i * (box_height + 10)
    });

// major
var major = edu_group.append('text')
    .style('text-anchor', 'left')
    .attr('fill', '#FFFFFF')
    .attr('x', 10).attr('y', function(d,i){
        return i * (box_height + 10) + 30
    }).attr('font-size', '1.4em')
    .text(function(d) { return d.major; });

// school + cert
var school = edu_group.append('text')
    .style('text-anchor', 'left')
    .attr('fill', '#FFFFFF')
    .attr('x', 10).attr('y', function(d,i){
        return i * (box_height + 10) + 55
    }).attr('font-size', '1.0em')
    .text(function(d) { return d.school + ' - ' + d.cert; });

// years attended
var years = edu_group.append('text')
    .style('text-anchor', 'right')
    .attr('fill', '#FFFFFF')
    .attr('x', box_width-175).attr('y', function(d,i){
        return i * (box_height + 10) + 25
    }).attr('font-size', '1.1em')
    .text(function(d) {
        var str = d.start_month + ' ' + d.start_year + ' - ';
        if (d.end_year == null) {str = str + 'present';}
        else {str = str + d.end_month + ' ' + d.end_year;}
        return str;
    });
