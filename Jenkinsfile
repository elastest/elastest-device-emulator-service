node('docker'){
   stage "Container initialize"
         echo("the node is up")
         //the new image is working!!!
         def mycontainer = docker.image('elastest/docker-compose-siblings')
         mycontainer.pull()
    stage "Code retrieve"
         git 'https://github.com/elastest/elastest-device-emulator-service.git'
         //here you can test anything you need as correctness of the pull
         //also can retrieve values of the git such as git commit git branch...
    stage "Unit tests?"
         //if you have unitary tests execute them here:
         //sh 'exec unitary tests' ==> OBVIOUSLY this doesn't work you should use the command you would use in a normal bash
         //if you execute tests you can delete the following line it is not delete as it isn't allowed empty stages.
         sh 'which docker'
    stage "build image"
         //here we use only the build for zigbeeip
          def zigbeeipe_image = docker.build("elastest/eds-zigbeeipe -f ./eds/docker/docker-files/zigbeeipe-amd64")
     stage "push image"
          zigbeeipe_image.push()
}