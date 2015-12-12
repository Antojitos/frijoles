========
Frijoles
========

Simple notifications powered by jumping beans

.. image:: https://travis-ci.org/Antojitos/frijoles.svg?branch=master
       :target: https://travis-ci.org/Antojitos/frijoles


Deployment
----------

Before start to deploying you need to have root access into a remote
server using SSH with a public key.

Install [ansible](<http://docs.ansible.com/ansible/intro_installation.html>) and run:

```shell
cp deploy/hosts.example hosts
vim hosts # edit/add your remote server
ansible-playbook -i hosts deploy/site.yml
```
