distractinator Ansible role
============================

Installs and configures the [distractinator] notification client.


Requirements
------------

* python-pip
* systemd

Role Variables
--------------

```yaml
# Whether pip package will be installed with `--user` flag.
# Defaults to yes to be consistent with systemd user services.
distractinator_user_install: yes

# Username to configure installation for. Will be added to `dialout` group.
distractinator_user: "{{ ansible_user|default(lookup('env', 'USER')) }}"

# Path to Python library defining custom actions. Absent by default.
# Create a custom .py file and provide the path (local to controller).
distractinator_custom_events_src: ''

# Path on remote host where custom events file is stored.
# File must be named "custom_events.py".
distractinator_custom_events_dest: "~{{ distractinator_user }}/.distractinator/customevents.py"
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
# Install distractinator and configure distractd
# user service via systemd.
- name: Configure distractinator
  hosts: workstations
  roles:
    - role: conorsch.distractinator
      # You will need to copy the default config file and edit it,
      # then specify the var below to the local path.
      distractinator_custom_events_src: files/customevents.py
```

Running the tests
-----------------

This role uses [Molecule] and [Testinfra] for testing. To test:

```
pip install -r requirements.txt
```

License
-------

MIT

[distractinator]: https://github.com/joedougherty/distractinator
[Molecule]: https://molecule.readthedocs.org/en/master/
[Testinfra]: https://testinfra.readthedocs.io/en/latest/
