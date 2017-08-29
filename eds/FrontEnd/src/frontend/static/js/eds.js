var configuredSensorList = {
    'top-left': '/mn-cse-1/onem2m/ZigBeeIPE/devices/ZBS122S000001/sensor_data/brightness',
    'top-middle': '/mn-cse-1/onem2m/ZigBeeIPE/devices/ZBS122S000001/sensor_data/humidity',
    'top-right': '/mn-cse-1/onem2m/ZigBeeIPE/devices/ZBS122S000001/sensor_data/temperature',
    'bottom-left':  '/mn-cse-1/onem2m/MemsIPE/sensor_data/x',
    'bottom-middle': '/mn-cse-1/onem2m/MemsIPE/sensor_data/y',
    'bottom-right': '/mn-cse-1/onem2m/MemsIPE/sensor_data/z'

};


function trafficLights(data) {
 //   var current = signals[(data.v)-1];
    var current = signals[data];

    if (current == 1)  {
        $('.trafficlight').removeClass("aktiv");
        $('#green').addClass("aktiv");
    } else if  (current == 2){
        $('.trafficlight').removeClass("aktiv");
        $('#yellow').addClass("aktiv");
    } else{
        $('.trafficlight').removeClass("aktiv");
        $('#red').addClass("aktiv");
    }
}



$("#btnAdd1").on('click',function() {
    console.log("Motor Started");
    socket.emit("motor_start")


});
$("#btnAdd2").on('click',function() {
    console.log("Motor Stopped");
    socket.emit("motor_stop")
});


$(document).ready(function () {
    $(document).foundation();

    var socket = io();

    initDashboard(socket, configuredSensorList);
   // trafficLights();
    ('MachineStatus', function(data){
        trafficLights(data)
    });



});




function errorCallback(error) {

}



