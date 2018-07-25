import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_version(host):
    command = host.run("java -version")

    assert command.rc == 0


def test_tomcat_user_existence(host):
    user = host.user('tomcat')

    assert user.exists
    assert user.shell == '/bin/bash'
    assert user.home == '/opt/tomcat'
    assert user.group == 'tomcat'


def test_tomcat_home_directory(host):
    homedir = host.file('/opt/tomcat')

    assert homedir.is_directory
    assert homedir.user == 'tomcat'
    assert homedir.group == 'tomcat'


def test_tomcat_ssh_directory(host):
    sshdir = host.file('/opt/tomcat/.ssh')

    assert sshdir.is_directory


def test_tomcat_ssh_config(host):
    sshconf = host.file('/opt/tomcat/.ssh/config')

    assert sshconf.exists
    assert sshconf.is_file


def test_tomcat_port(host):
    port = host.socket('tcp://0.0.0.0:80')

    assert port.is_listening


def test_tomcat_running_and_enabled(host):
    tomcat = host.service("tomcat")

    assert tomcat.is_running
    assert tomcat.is_enabled
