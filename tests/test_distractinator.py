import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_pip_is_installed(Package):
    """
    The role does not install python-pip, but it's required.
    The role doesn't install because some admins may wish to use a more recent
    version of pip than is provided by the distribution's repositories.
    """
    assert Package('python-pip').is_installed


@pytest.mark.xfail
def test_distractinator_is_installed(Command, PipPackage):
    """
    Ensure the distractinator pip package is present.
    """
    c = Command('pip freeze')
    assert 'distractinator' in c.stdout
    assert 'distractinator' in PipPackage.get_packages()


@pytest.mark.xfail
def test_distractd_service_is_running(Service):
    """
    Ensure the distractinator systemd service is running.
    """
    s = Service('distractd')
    assert s.is_running
    assert s.is_enabled
