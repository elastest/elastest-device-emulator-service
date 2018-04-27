node('docker'){
   stage "Container initialize"
         echo("the node is up")
         //the new image is working!!!
        def mycontainer = docker.image('elastest/ci-docker-compose-py-siblings:latest')
        mycontainer.pull()
        mycontainer.inside("-u jenkins -v /var/run/docker.sock:/var/run/docker.sock:rw") {

        stage "Code retrieve"
         git 'https://github.com/elastest/elastest-device-emulator-service.git'
         //here you can test anything you need as correctness of the pull
         //also can retrieve values of the git such as git commit git branch...

        stage "Unit tests?"
          echo ("Running Unit Test ...")
         //if you have unitary tests execute them here:
          echo ("Running Unit Tests for FrontEnd")
          // sh 'cd eds/FrontEnd && exec tox'
           //step([$class: 'JUnitResultArchiver', testResults: '**/nosetests.xml'])

          echo ("Running Unit Tests for MemsIPE")
            //  sh 'cd eds/MemsIPE && exec tox'
            //step([$class: 'JUnitResultArchiver', testResults: '**/nosetests.xml'])


          echo ("Running Unit Tests for Rest App")
           //sh 'cd eds/rest_app && exec tox'
           //step([$class: 'JUnitResultArchiver', testResults: '**/nosetests.xml'])



        stage "build api image"
         //here we use only the build for api
            def api_image = docker.build("elastest/eds-api:latest", "./eds/rest_app")


        stage "build memsipe image"
         //here we use only the build for memsipe
             def memsipe_image = docker.build("elastest/eds-memsipe:latest", "./eds/MemsIPE")

        stage "build frontend image"
         //here we use only the build for frontend
             def frontend_image = docker.build("elastest/eds-frontend:latest", "./eds/FrontEnd")

        stage "build eds-base image"
            def edsbase_image = docker.build("elastest/eds-base:latest", "./demo/eds_base")

        stage "Run EDS docker-compose"
                //sh 'modprobe i2c-dev'
                //sh 'chmod +x script/* && script/startup-linux.sh && script/teardown-linux.sh'
                echo ("EDS System is running..")

        stage "publish"
          echo ("publishing..")
          withCredentials([[
            $class: 'UsernamePasswordMultiBinding',
                credentialsId: 'elastestci-dockerhub',
                usernameVariable: 'USERNAME',
                passwordVariable: 'PASSWORD']]) {
                 sh 'docker login -u "$USERNAME" -p "$PASSWORD"'
                        //here your code
                 memsipe_image.push()
                 frontend_image.push()
                 api_image.push()
                 edsbase_image.push()

                    }

        }
}
