import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_version(host):
    command = host.run("java -version")
    assert command.rc == 0


def test_nginx_user(host):
    os = host.system_info.distribution

    if os == 'debian':
        user = host.user('www-data')

        assert user.exists
        assert user.shell == '/usr/sbin/nologin'
        assert user.home == '/var/www'
        assert user.group == 'www-data'

    elif os =='redhat':
        user = host.user('nginx')

        assert user.exists
        assert user.shell == '/sbin/nologin'
        assert user.home == '/var/cache/nginx'
        assert user.group == 'nginx'


def test_tomcat_user(host):
    user = host.user('tomcat')

    assert user.exists
    assert user.shell == '/bin/bash'
    assert user.home == '/opt/tomcat'
    assert user.group == 'tomcat'


def test_tomcat_home_directory(host):
    homedir = host.file('/opt/tomcat')

    assert homedir.is_directory
    assert oct(homedir.mode) == '0755'


def test_tomcat_logs_directory(host):
    config_dir = host.file('/opt/tomcat/logs')

    assert config_dir.is_directory
    assert config_dir.user == 'tomcat'
    assert config_dir.group == 'tomcat'
    assert oct(config_dir.mode) == '0750'


def test_tomcat_temp_directory(host):
    config_dir = host.file('/opt/tomcat/temp')

    assert config_dir.is_directory
    assert config_dir.user == 'tomcat'
    assert config_dir.group == 'tomcat'
    assert oct(config_dir.mode) == '0750'


def test_tomcat_webapps_directory(host):
    config_dir = host.file('/opt/tomcat/webapps')

    assert config_dir.is_directory
    assert config_dir.user == 'tomcat'
    assert config_dir.group == 'tomcat'
    assert oct(config_dir.mode) == '0750'


def test_tomcat_work_directory(host):
    config_dir = host.file('/opt/tomcat/work')

    assert config_dir.is_directory
    assert config_dir.user == 'tomcat'
    assert config_dir.group == 'tomcat'
    assert oct(config_dir.mode) == '0750'


def test_http_port(host):
    port = host.socket('tcp://0.0.0.0:80')

    assert port.is_listening


def test_tomcat_port(host):
    port = host.socket('tcp://0.0.0.0:8080')

    assert port.is_listening


def test_nginx_service(host):
    service = host.service('nginx')

    assert service.is_enabled
    assert service.is_running


def test_tomcat_service(host):
    service = host.service('tomcat')

    assert service.is_running
    assert service.is_enabled
