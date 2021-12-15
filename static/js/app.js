

d3.csv("../../Data/survey_df.csv").then((feature) => {
    console.log(feature)
});
let trace1 = {
    x: feature.map(row => row.romanName),
    y: feature.map(row => row.romanSearchResults),
    type: "bar"
};

// Data trace array
let traceData = [trace1];

// Apply title to the layout
let layout = {
  title: "Popular Roman gods search results"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", traceData, layout);