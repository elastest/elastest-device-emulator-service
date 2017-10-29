////////////
// GRAPH //
//////////

function updateChart(confSensor) {
  // graph
  d3.select('#chart-' + confSensor.tile + ' svg').datum([{
    values: _.map(confSensor.data, function (x) {
      return _.clone(x)
    }),
    key: confSensor.sensor,
    color: "#fff",
    strokeWidth: 6
  }]).transition().duration(500).call(confSensor.chart);
  nv.utils.windowResize(confSensor.chart.update);

  // json
  $('#JSON-Data-' + confSensor.tile)
    .html(JSON.stringify(confSensor.data.slice().reverse(), null, 2));

  $('pre').each(function (i, block) {
    hljs.highlightBlock(block);
  });

  // value
  $('#Value-' + confSensor.tile)
    .html('<h1 class="giant">'
      + _.last(confSensor.data).y.toFixed(1)
      + (confSensor.unit !== null ? +"  " + confSensor.unit : "")
      + '</h1>')
}

function createChart(confSensor) {
  // graph
  nv.addGraph(function () {
    var chart = nv.models.lineChart()
      .options({
        duration: 300,
        useInteractiveGuideline: true
      });
    confSensor.chart = chart;

    // chart sub-models (ie. xAxis, yAxis, etc) when accessed directly, return themselves, not the parent chart, so need to chain separately
    chart.xAxis
      .rotateLabels(-45)
      .tickFormat(function (d) {
        return d3.time.format('%H:%M:%S')(new Date(d));
      })
      .staggerLabels(true);

    chart.yAxis
      .axisLabel(confSensor.unit)
      .tickFormat(function (d) {
        if (d === null) {
          return 'N/A';
        }
        return d3.format(',.2f')(d);
      });

    d3.select('#chart-' + confSensor.tile).append('svg')
      .datum([{
        values: _.map(confSensor.data, function (x) {
          return _.clone(x)
        }),
        key: confSensor.sensor,
        color: "#fff",
        strokeWidth: 6
      }])
      .call(chart);

    nv.utils.windowResize(chart.update);

    return chart;
  });

  // json
  $('#JSON-Data-' + confSensor.tile)
    .html(JSON.stringify(confSensor.data.slice().reverse(), null, 2));

  $('pre').each(function (i, block) {
    hljs.highlightBlock(block);
  });

  // value
  $('#Value-' + confSensor.tile)
    .html('<h1 class="giant">'
      + _.last(confSensor.data).y.toFixed(1)
      + (confSensor.unit !== null ? +"  " + confSensor.unit : "")
      + '</h1>')
}
