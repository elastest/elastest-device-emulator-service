node('docker'){
   stage "Container initialize"
         echo("the node is up")
         //the new image is working!!!
         def mycontainer = docker.image('elastest/ci-docker-compose-siblings')
         mycontainer.pull()
         mycontainer.inside("-u jenkins -v /var/run/docker.sock:/var/run/docker.sock:rw") {

             stage "Code retrieve"
                git 'https://github.com/elastest/elastest-device-emulator-service.git'
             //here you can test anything you need as correctness of the pull
            //also can retrieve values of the git such as git commit git branch...
             stage "Unit tests?"
                //if you have unitary tests execute them here:
                 //sh 'exec unitary tests' ==> OBVIOUSLY this doesn't work you should use the command you would use in a normal bash
                //if you execute tests you can delete the following line it is not delete as it isn't allowed empty stages.
                sh 'which docker'


            stage "build zigbee image"
                 //here we use only the build for zigbeeipe
                  def zigbeeipe_image = docker.build("elastest/eds-zigbeeipe -f ./eds/ZigBeeIPE/Dockerfile")


            stage "build memsipe image"
             //here we use only the build for memsipe
                def memsipe_image = docker.build("elastest/eds-memsipe -f ./eds/MemsIPE/Dockerfile")


            stage "build frontend image"
                //here we use only the build for frontend
                 def frontend_image = docker.build("elastest/eds-frontend -f ./eds/FrontEnd/Dockerfile")

            stage "publish"
               echo ("publishing..")
               withCredentials([[
                  $class: 'UsernamePasswordMultiBinding',
                  credentialsId: 'elastestci-dockerhub',
                  usernameVariable: 'USERNAME',
                  passwordVariable: 'PASSWORD']]) {
                        sh 'docker login -u "$USERNAME" -p "$PASSWORD"'
                        //here your code
                        zigbeeipe_image.push()
                        memsipe_image.push()
                        frontend_image.push()
                    }

        }
}