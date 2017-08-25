var configuredSensorList = {
  'top-left': '/mn-cse-1/onem2m/OPCUAIPE/plc_2/',
  'top-right': '/mn-cse-1/onem2m/OPCUAIPE/plc_1/',
  'bottom-left': '/mn-cse-1/onem2m/MemsIPE/sensor_data/'
};

$(document).ready(function () {
  $(document).foundation();

  var socket = io();


    $("#btnAdd1").on('click',function() {
        console.log("Motor Started");
        socket.emit("motor_start")

    });

    $("#btnAdd2").on('click',function() {
        console.log("Motor Stopped");
        socket.emit("motor_stop")
    });

     socket.on('MachineStatusLED', function(data){
            trafficLights(data)
        });

  initDashboard(socket, configuredSensorList);
});
