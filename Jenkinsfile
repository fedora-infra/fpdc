/**
 * This is fpdc's Jenkins Pipeline Jenkinsfile.
 *
 * You can read documentation about this file at https://jenkins.io/doc/book/pipeline/jenkinsfile/.
 * A useful list of plugins can be found here: https://jenkins.io/doc/pipeline/steps/.
*/

/**
 * Run the given script on the Duffy node.
 *
 * @param script The script to run on the node.
*/
def onmyduffynode(String script) {
    timestamps {
        sh 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l root ${DUFFY_NODE}.ci.centos.org "' + script + '"'
    }
}

/**
 * rsync the given path from the Duffy node back to the control host.
 *
 * @param rsyncpath The path to be rsync'd back to the control host.
 */
def syncfromduffynode(rsyncpath) {
    sh 'rsync -e "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l root " -Ha --include=' + " ${DUFFY_NODE}.ci.centos.org:~/payload/" + rsyncpath + " ./"
}

/**
 * rsync the given path from the control host to the Duffy node.
 *
 * @param rsyncpath The path to be rsync'd to the Duffy node.
 */
def synctoduffynode(rsyncpath) {
    sh 'rsync -e "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -l root " -Ha --include=' +  rsyncpath + " ./ ${DUFFY_NODE}.ci.centos.org:~/payload/"
}

/**
 * Install test dependencies on the Duffy node.
 */
def configure_node = {
    onmyduffynode 'yum -y install epel-release'
    onmyduffynode 'yum install -y python36 rsync'
}


node('fpdc') {
    checkout scm

    stage('Allocate Duffy node') {
        env.CICO_API_KEY = readFile("${env.HOME}/duffy.key").trim()
        // Get a duffy node and set the DUFFY_NODE and SSID environment variables.
        duffy_rtn=sh(
            script: 'cico --debug node get -f value -c hostname -c comment --retry-count 4 --retry-interval 60',
            returnStdout: true
            ).trim().tokenize(' ')
        env.DUFFY_NODE=duffy_rtn[0]
        env.SSID=duffy_rtn[1]
    }

    try {

        stage('Configure node'){
            retry_with_sleep(configure_node)
        }

        stage('Sync pull request to node') {
            synctoduffynode('fpdc')
        }

        stage('setup') {
            steps {
                onmyduffynode "pip3 install -r requirements-dev.txt"
            }
        }

        stage('unit tests') {
            steps {
                onmyduffynode "cd fpdc && tox -e py36"
            }
        }

        stage('lint') {
            steps {
                onmyduffynode "cd fpdc && tox -e lint"
            }
        }

        stage('format') {
            steps {
                onmyduffynode "cd fpdc && tox -e format"
            }
        }

        stage('django-migrations') {
            steps {
                onmyduffynode "cd fpdc && tox -e django-migrations"
            }
        }

        stage('licenses') {
            steps {
                onmyduffynode "cd fpdc && tox -e lisenses"
            }
        }

    } catch (e) {
        currentBuild.result = "FAILURE"
        throw e
    } finally {
        stage('Deallocate node'){
            sh 'cico node done ${SSID}'
        }
    }
}
