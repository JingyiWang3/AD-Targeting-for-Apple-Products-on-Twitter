// URL: https://beta.observablehq.com/d/dd12ff35be803a39
// Title: Disjoint Force-Directed Graph
// Author: Yuanqing Hong (@yh2866)
// Version: 219
// Runtime version: 1

const m0 = {
  id: "dd12ff35be803a39@219",
  variables: [
  {
      inputs: ["md"],
      value: (function(md){return(
md`
### Influencer Graph

**Nodes**: Green - Users who created the most retweeted tweets

**Entities**: Purple - Important URLs; Orange - Hashtags; Yellow - The user commonly mentioned

**Edges**:  Entities are connected to green nodes if they are menditoned in the  tweets created by this user.

**Nodes size**: proportional to the retweeted count of the tweets the nodes is related to.`
)})
    },
    {
      name: "chart",
      inputs: ["data","forceSimulation","d3","DOM","width","height","color","drag"],
      value: (function(data,forceSimulation,d3,DOM,width,height,color,drag)
{
  const links = data.links.map(d => Object.create(d));
  const nodes = data.nodes.map(d => Object.create(d));
  const simulation = forceSimulation(nodes, links).on("tick", ticked);

  const svg = d3.select(DOM.svg(width, height))
      .attr("viewBox", [-width / 3.2, -height / 3.2, width / 1.6, height / 1.6]);

  var radiusScale = d3.scaleLinear()
        .domain([0, 2])
        .range([5, 30])
  
  const link = svg.append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
    .selectAll("line")
    .data(links)
    .enter().append("line")
      .attr("stroke-width", d => Math.sqrt(d.value));

  const node = svg.append("g")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
    .selectAll("circle")
    .data(nodes)
    .enter().append("circle")
      .attr("r", d => radiusScale(+(d.weight*400)))
      // .attr("r", 5)
      .attr("fill", color)
      .call(drag(simulation));

  
var label = svg.selectAll(null)
    .data(nodes)
    .enter()
    .append("text")
    .text(function (d) { return d.id; })
    .style("text-anchor", "middle")
    .style("fill", "#555")
    .style("font-family", "Arial")
    .style("font-size", 6);
  

  function ticked() {
    link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);
    
    node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);
    
    
    label
        .attr("x", d => d.x)
        .attr("y", d => d.y-5);
  }

  return svg.node();
}
)
    },
    {

    },
    {
      name: "forceSimulation",
      inputs: ["d3"],
      value: (function(d3){return(
function forceSimulation(nodes, links) {
  return d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id(d => d.id))
      .force("charge", d3.forceManyBody())
      .force("x", d3.forceX())
      .force("y", d3.forceY());
}
)})
    },
    {
      name: "data",
      inputs: ["d3"],
      value: (function(d3){return(
d3.json("https://raw.githubusercontent.com/yh2866/AD-Targeting-for-Apple-Products-on-Twitter/master/website/d3/influence_dict2.json")
)})
    },
    {
      name: "height",
      value: (function(){return(
680
)})
    },
    {
      name: "color",
      inputs: ["d3"],
      value: (function(d3)
{
  const scale = d3.scaleOrdinal(d3.schemeAccent);
  return d => scale(d.group);
}
)
    },
    {
      name: "drag",
      inputs: ["d3"],
      value: (function(d3){return(
simulation => {
  
  function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }
  
  function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
  }
  
  function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }
  
  return d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended);
}
)})
    },
    {
      name: "d3",
      inputs: ["require"],
      value: (function(require){return(
require("d3@5")
)})
    }
  ]
};

const notebook = {
  id: "dd12ff35be803a39@219",
  modules: [m0]
};

export default notebook;
