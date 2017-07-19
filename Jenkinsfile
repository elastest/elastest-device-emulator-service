node('docker'){
    stage "Container Prep"
        echo("the node is up")
        def mycontainer = docker.image('franciscordiaz/docker-in-docker-etm5')
        mycontainer.pull() // make sure we have the latest available from Docker Hub

        mycontainer.inside("-u jenkins -v /var/run/docker.sock:/var/run/docker.sock:rw") {
            git 'https://github.com/elastest/elastest-device-emulator-service.git'

            stage "Unit Tests"
                 sh 'ls -la'
                 echo ("Starting unit tests")
            //     echo ("No tests yet, but these would be integration at least")
                 sh 'which docker'

            stage "Build project"
                echo ("Building .. ")
                //Build project its done in the dockerfiles.

            stage "docker-compose"
                sh 'docker-compose --build -d blabla...'
                sh 'docker exec'

            stage "push miniservice 1"
                def zigbeeipe_image = docker.build("elastest/eds-zigbeeipe -f eds/docker/docker-files/zigbeeipe-amd64")
                zigbeeipe_image.pull()
            //this is work arround as withDockerRegistry is not working properly
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'elastestci-dockerhub',
                    usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
                    sh 'docker login -u "$USERNAME" -p "$PASSWORD"'
                    zigbeeipe_image.push()
                }
           // stage "Build Master image - Package"
             //   echo ("building..")
                //need to be corrected to the organization because at the moment elastestci can't create new repositories in the organization
               // def eds_image = docker.build("elastest/elastest-device-emulator-service")

           // stage "Build Spark Worker image - Package"
              //  echo ("building..")
                //need to be corrected to the organization because at the moment elastestci can't create new repositories in the organization
                //def eds_image = docker.build("elastest/elastest-device-emulator-service")

            stage "Run image"
                echo ("running..")
                myimage.run()

            stage "Integration tests"
                echo ("Starting integration tests...")
                echo ("No integration tests yet")

        }
}