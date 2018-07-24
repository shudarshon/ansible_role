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
    assert user.home == '/opt/apache-tomcat-9.0.4'
    assert user.group == 'tomcat'


def test_tomcat_home_directory(host):
    homedir = host.file('/opt/apache-tomcat-9.0.4')

    assert homedir.is_directory
    assert oct(homedir.mode) == '0755'


def test_tomcat_logs_directory(host):
    config_dir = host.file('/opt/apache-tomcat-9.0.4/logs')

    assert config_dir.is_directory
    assert config_dir.user == 'tomcat'
    assert config_dir.group == 'tomcat'
    assert oct(config_dir.mode) == '0750'


def test_tomcat_temp_directory(host):
    config_dir = host.file('/opt/apache-tomcat-9.0.4/temp')

    assert config_dir.is_directory
    assert config_dir.user == 'tomcat'
    assert config_dir.group == 'tomcat'
    assert oct(config_dir.mode) == '0750'


def test_tomcat_webapps_directory(host):
    config_dir = host.file('/opt/apache-tomcat-9.0.4/webapps')

    assert config_dir.is_directory
    assert config_dir.user == 'tomcat'
    assert config_dir.group == 'tomcat'
    assert oct(config_dir.mode) == '0750'


def test_tomcat_work_directory(host):
    config_dir = host.file('/opt/apache-tomcat-9.0.4/work')

    assert config_dir.is_directory
    assert config_dir.user == 'tomcat'
    assert config_dir.group == 'tomcat'
    assert oct(config_dir.mode) == '0750'


def test_tomcat_port(host):
    port = host.socket('tcp://0.0.0.0:8080')

    assert port.is_listening


def test_tomcat_running_and_enabled(host):
    tomcat = host.service("tomcat")

    assert tomcat.is_running
    assert tomcat.is_enabled
