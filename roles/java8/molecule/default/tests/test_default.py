import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_version(host):
    command = host.run("java -version")
    assert command.rc == 0


def test_java_path(host):
    java_path = host.file("/usr/bin/java")
    assert java_path.user == "root"
    assert java_path.group == "root"
    assert java_path.is_file
    assert java_path.is_symlink
