# fortimanager-playbook-example

This repository aims to collect runnable playbooks for FortiManager Ansible collections. Anyone can contribute, enhance or alter examples under
`src` folder.

**Please always use the latest and default branch when submitting a pull request so that they are included in future release!**


### Contribute Process

First of all, please have a short and descriptive file name for your example.

Please also provide additional information about your example, they `MUST` be put in the head of your example file:
* `Author`: Your full name, optional.
* `Org`: Your organization name, optional.
* `Date`: In format `YYYY.MM.DD`, the date your example being added, optional. if missing, the day on which the example is processed is chosen instead.
* `Label`: Label list, they can be seperated by `,` if there are multiple labels, optioal.
* `Desc`: the description for your example, please let it be short.


One example:
```
# Author: Link Zheng
# Org: Fortinet
# Date: 2020.09.11
# Label: device, cmd
# Desc: Add a FGT device to FMG
# This line doesn't take any effect.

- name: Add a FOS device to FMG
  hosts: fortimanager01
  gather_facts: no
  connection: httpapi
  ... ...
  ... ...
  ... ...
```
The fields themselves are case insenstive, and white blank characters are not restricted as well.
You can also keep any comment lines in your example playbooks. 
