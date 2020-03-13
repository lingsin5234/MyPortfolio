// declarations, setup SVG
var svg = d3.select('#startContent').append('svg')
    .attr('height', 1000).attr('width', 800);

// set up the groups
var group_skills = svg.selectAll('g')
    .data(tech_skills).enter().append('g')
    .attr("transform", function(d,i) {
        return "translate(" + (i % 3 * 250 + 20) + "," + (Math.floor(i / 3) * 60 + 10) + ")";
    });

// list the skills as text
var skill_names = group_skills.append('text')
    .attr('class', 'skill-text')
    .attr('fill', 'white')
    .style('text-anchor', 'left')
    .attr('x', 0)
    .attr('y', 70)
    .attr('font-family', 'roboto')
    .attr('font-size', '1.1em')
    .text(function(d) { return d.name; });

// skill bar background
var skill_bars = group_skills.append('rect')
    .attr('class', 'bar-rect')
    .attr('rx', 10).attr('ry', 10)
    .attr('fill', 'gray')
    .attr('height', 15).attr('width', 200)
    .attr('x', 0)
    .attr('y', 75);

// set up experience-fill bars
var exp_fill = group_skills.append('rect')
    .attr('class', 'exp-rect')
    .attr('rx', 10).attr('ry', 10)
    .attr('fill', 'orange')
    .attr('height', 15).attr('width', 0)
    .attr('x', 0)
    .attr('y', 75);

// move the exp-fill bar after page load
exp_fill.transition()
    .duration(1000)
    .attr('width', function(d) {
        // using 10 years as max
        if (d.year_exp > 10) {
            return 200;
        } else {
            return d.year_exp/10 * 200;
        }
    });