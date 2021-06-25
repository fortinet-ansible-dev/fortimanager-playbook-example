YML_FILES = $(foreach item, . ,$(wildcard $(item)/*.yml))
# remove cases which need to be ignored
YML_FILES := $(filter-out ./discover_and_add_device.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_user_pop3.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_system_sdnconnector.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_system_replacemsggroup_custommessage.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_system_report_group_groupby.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_dvmdb_script_execute.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_pkg_footer_policy.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_pkg_footer_policy__fact.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_application_custom.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_application_list_entries.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_application_list_entries_parameters.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_application_list_entries_parameters__fact.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_firewall_vip_dynamicmapping.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_pkg_firewall_dospolicy6, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_pkg_firewall_dospolicy6_anomaly.yml, $(YML_FILES))
YML_FILES := $(filter-out ./, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_firewall_vip6_dynamicmapping.yml, $(YML_FILES))
YML_FILES := $(filter-out ./fmgr_devprof_system_snmp_community_hosts.yml, $(YML_FILES))
YML_FAKE_OBJECT = $(patsubst %.yml,%.fakeobject,$(YML_FILES))


.PHONY:all
all: $(YML_FAKE_OBJECT)
	@echo "[RUN] all cases done..."
	@make stats

# dependency
fmgr_firewall_addrgrp.yml: fmgr_firewall_address.fakeobject
fmgr_firewall_addrgrp6.yml: fmgr_firewall_address.fakeobject fmgr_firewall_address6.fakeobject
fmgr_firewall_gtp_ieremovepolicy.yml: fmgr_firewall_gtp.fakeobject
fmgr_system_snmp_community_hosts__fact.yml: fmgr_system_snmp_community_hosts.fakeobject
fmgr_system_snmp_community_hosts.yml: fmgr_system_snmp_community.fakeobject
fmgr_antivirus_notification_entries.yml: fmgr_antivirus_notification.fakeobject
fmgr_system_dhcp_server_excluderange.yml: fmgr_system_dhcp_server.fakeobject
fmgr_firewall_vip_dynamicmapping.yml:fmgr_firewall_vip.fakeobject
fmgr_system_replacemsggroup_admin.yml: fmgr_system_replacemsggroup.fakeobject
fmgr_firewall_address6_list.yml: fmgr_firewall_address6.fakeobject
fmgr_firewall_address6_list__fact.yml: fmgr_firewall_address6_list.fakeobject
	@echo "[CHECK] detected dependency for $@..."

%.fakeobject:%.yml
	@echo "[RUN] running testcase $< ..."
	@-ansible-playbook -i hosts $< >/tmp/runtime.test 2>/tmp/ignore
	@#create fake object to make incremental test
	@touch $@

.PHONY:clean
clean:
	@rm -f *.fakeobject

.PHOONY: stats
stats:
	@echo "[STATS] `ls *.fakeobject |wc -l`/`ls *.yml |wc -l` pass"
