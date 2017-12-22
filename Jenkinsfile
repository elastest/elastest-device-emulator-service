node('docker'){
   def tag = "0.5.0"
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

          echo ("Running Unit Tests for ZigBeeIPE")
            //  sh 'cd eds/ZigBeeIPE && exec tox'
            //step([$class: 'JUnitResultArchiver', testResults: '**/nosetests.xml'])

          echo ("Running Unit Tests for Rest App")
           //sh 'cd eds/rest_app && exec tox'
           //step([$class: 'JUnitResultArchiver', testResults: '**/nosetests.xml'])



        //stage "build api image"
         //here we use only the build for zigbeeip
         //    sh 'docker build --build-arg GIT_COMMIT=$(git rev-parse HEAD) --build-arg COMMIT_DATE=$(git log -1 --format=%cd --date=format:%Y-%m-%dT%H:%M:%S) -f eds/rest_app . -t elastest/eds-api:${tag}' 
         //    def api_image = docker.image("elastest/eds-api:${tag}")


        stage "build memsipe image"
         //here we use only the build for zigbeeip
             sh 'docker build --build-arg GIT_COMMIT=$(git rev-parse HEAD) --build-arg COMMIT_DATE=$(git log -1 --format=%cd --date=format:%Y-%m-%dT%H:%M:%S) -f eds/MemsIPE . -t elastest/eds-memsipe:${tag}' 
             def memsipe_image = docker.image("elastest/eds-memsipe:${tag}")

        stage "build zigbeeipe image"
         //here we use only the build for zigbeeip
             sh 'docker build --build-arg GIT_COMMIT=$(git rev-parse HEAD) --build-arg COMMIT_DATE=$(git log -1 --format=%cd --date=format:%Y-%m-%dT%H:%M:%S) -f eds/ZigBeeIPE . -t elastest/eds-zigbeeipe:${tag}' 
             def zigbeeipe_image = docker.image("elastest/eds-zigbeeipe:${tag}")

        stage "build frontend image"
         //here we use only the build for zigbeeip
             sh 'docker build --build-arg GIT_COMMIT=$(git rev-parse HEAD) --build-arg COMMIT_DATE=$(git log -1 --format=%cd --date=format:%Y-%m-%dT%H:%M:%S) -f eds/FrontEnd . -t elastest/eds-frontend:${tag}' 
             def frontend_image = docker.image("elastest/eds-frontend:${tag}")


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
                 zigbeeipe_image.push()
                // api_image.push()


                    }

        }
}