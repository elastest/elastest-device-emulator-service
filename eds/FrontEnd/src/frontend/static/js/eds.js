var configuredSensorList = {

    'top-left':  '/mn-cse-1/onem2m/MemsIPE/sensor_data/x',
    'top-middle': '/mn-cse-1/onem2m/MemsIPE/sensor_data/y',
    'top-right': '/mn-cse-1/onem2m/MemsIPE/sensor_data/z'

};







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



