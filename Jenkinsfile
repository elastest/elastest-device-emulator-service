node('docker'){
    stage "Container Prep"
        echo("the node is up")
        def mycontainer = docker.image('gtunon/docker-in-docker:latest')
        mycontainer.pull() // make sure we have the latest available from Docker Hub
        mycontainer.inside("-u jenkins -v /var/run/docker.sock:/var/run/docker.sock:rw") {
            git 'https://github.com/elastest/elastest-device-emulator-service.git'
            
            // stage "Test"
            //     sh 'ls -la'
            //     echo ("Starting maven tests")
            //     echo ("No tests yet, but these would be integration at least")
            //     sh 'which docker'
                
            stage "Build  Base image - Package"
                echo ("building..")
                //need to be corrected to the organization because at the moment elastestci can't create new repositories in the organization
                def eds_image = docker.build("elastest/elastest-device-emulator-service")

          

            stage "Run image"
            //    eds_image.run()
                echo ("running..")
                
            stage "publish"
                echo ("publishing..")
            // //this is work arround as withDockerRegistry is not working properly 
            withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'elastestci-dockerhub',
                usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
                sh 'docker login -u "$USERNAME" -p "$PASSWORD"'
                eds_image.push()
                //spark_master_image.push()
                //spark_worker_image.push()
             }
        }
}
