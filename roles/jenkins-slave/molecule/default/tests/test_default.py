import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_version(host):
    command = host.run("java -version")
    assert command.rc == 0


def test_jenkins_user(host):
    user = host.user('jenkins')

    assert user.exists
    assert user.shell == '/bin/bash'
    assert user.home == '/var/lib/jenkins'
    assert user.group == 'jenkins'


def test_jenkins_home_directory(host):
    homedir = host.file('/var/lib/jenkins')

    assert homedir.is_directory
    assert homedir.user == 'jenkins'
    assert homedir.group == 'jenkins'


def test_tomcat_ssh_directory(host):
    sshdir = host.file('/var/lib/jenkins/.ssh')

    assert sshdir.is_directory


def test_tomcat_ssh_config(host):
    sshconf = host.file('/var/lib/jenkins/.ssh/config')

    assert sshconf.exists
    assert sshconf.is_file


def test_tomcat_ssh_auth_key(host):
    authkey_file = host.file('/var/lib/jenkins/.ssh/authorized_keys')

    assert authkey_file.exists
    assert authkey_file.is_file
    assert authkey_file.size > 0
