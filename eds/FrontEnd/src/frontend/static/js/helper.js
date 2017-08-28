// helper functions
function getConfigFromList(configuredSensorList) {
  return _.chain(configuredSensorList).omit(function (value) {
    return value === null;
  }).invert().mapObject(function (val) {
    return {
      tile: val,
      created: false
    }
  }).cd ();
}

function setSensorColumn(tile, name) {
  $('#sensor-column-' + tile).html('<h5><span class="tag">SENSOR: </span>' + name + '</h5>')
}

function setDeviceColumn(tile, name) {
  $('#device-column-' + tile).html('<h5><span class="tag">DEVICE: </span >' + name + '</h5>')
}

function setSensorCardSection(tile) {
  var graphID = 'Graph-' + tile;
  var jsonID = 'JSON-' + tile;
  var valueID = 'Value-' + tile;
  $('#card-' + tile).html('' +
    '<div class="row expanded">' +
    '<ul class="tabs column small-12" data-tabs id="tabs-' + tile + '">' +
    '<li class="tabs-title is-active"><a href="#' + graphID + '">Graph</a></li>' +
    '<li class="tabs-title "><a href="#' + jsonID + '">JSON</a></li>' +
    '<li class="tabs-title"><a href="#' + valueID + '">Current Value</a></li>' +
    '</ul>' +
    '</div>' +
    '<div class="row expanded">' +
    '<div class="tabs-content column small-12" ' +
    'data-tabs-content="tabs-' + tile + '">' +
    '<div class="tabs-panel is-active column small-12" id="' + graphID + '">' +
    '<div id="chart-' + tile + '" class="charts"></div>' +
    '</div>' +
    '<div class="tabs-panel column small-12" id="' + jsonID + '">' +
    '<pre class="JSON" id="JSON-Data-' + tile + '"></pre>' +
    '</div>' +
    '<div class="tabs-panel" id="' + valueID + '"></div>' +
    '</div>' +
    '</div>').parent().removeClass("hide").foundation();
}

function initSensorTile(confSensor) {
  setDeviceColumn(confSensor.tile, confSensor.dev);
  setSensorColumn(confSensor.tile, confSensor.sensor);
  setSensorCardSection(confSensor.tile);
}

function setActuatorCardSection(tile) {
  $('#card-' + tile).html('' +
    '<div class="expanded button-group">' +
    '<a class="button " onclick="window.actuate(\'' + tile + '\', \'ON\')">ON</a>' +
    '<a class="button "  onclick="window.actuate(\'' + tile + '\', \'OFF\')">OFF</a>' +
    '</div>').parent().removeClass("hide").foundation();
}

function initActuatorTile(confActuator) {
  setDeviceColumn(confActuator.tile, confActuator.dev);
  setSensorColumn(confActuator.tile, confActuator.actuator);
  setActuatorCardSection(confActuator.tile);
}
