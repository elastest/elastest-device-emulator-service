var configuredSensorList = {
  'top-left': null,
  'top-middle': null,
  'top-right': null,
  'bottom-left': null,
  'bottom-middle': null,
  'bottom-right': null
};

$(document).ready(function () {
  $(document).foundation();

  var socket = io();

  initDashboard(socket, configuredSensorList);
});
