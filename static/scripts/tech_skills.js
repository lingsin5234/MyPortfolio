// declarations
var num_skills3 = tech_skills.length / 3 + 0.5;
var height = 60;
var svg_height = height * num_skills3;

//setup SVG
var svg = d3.select('#tech_skills').append('svg')
    .attr('height', svg_height).attr('width', box_width);

// set up the groups
var group_skills = svg.selectAll('g')
    .data(tech_skills).enter().append('g')
    .attr("transform", function(d,i) {
        return "translate(" + (i % 3 * 250 + 20) + "," + (Math.floor(i / 3) * height + 10) + ")";
    });

// list the skills as text
var skill_names = group_skills.append('text')
    .attr('class', 'skill-text')
    .attr('fill', 'white')
    .style('text-anchor', 'left')
    .attr('x', 0).attr('y', 5)
    .attr('font-family', 'roboto')
    .attr('font-size', '1.1em')
    .text(function(d) { return d.name; });

// skill bar background
var skill_bars = group_skills.append('rect')
    .attr('class', 'bar-rect')
    .attr('rx', 10).attr('ry', 10)
    .attr('fill', 'gray')
    .attr('height', 15).attr('width', 200)
    .attr('x', 0).attr('y', 10);

// set up experience-fill bars
var exp_fill = group_skills.append('rect')
    .attr('class', 'exp-rect')
    .attr('rx', 10).attr('ry', 10)
    .attr('fill', 'orange')
    .attr('height', 15).attr('width', 0)
    .attr('x', 0).attr('y', 10);

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

// years of exp text
var exp_text = group_skills.append('text')
    .attr('class', 'exp-text')
    .attr('fill', 'white')
    .style('text-anchor', 'right')
    .attr('x', 180).attr('y', 35)
    .attr('font-family', 'roboto')
    .attr('font-size', '0.6em')
    .text('10+ yrs');

