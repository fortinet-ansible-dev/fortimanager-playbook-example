YML_FILES_ORIGINAL = $(foreach item, . ,$(wildcard $(item)/*.yml))
# remove cases which need to be ignored
FILES_TO_IGNORE_FORSHORT = fmgr_dvm_cmd_discover_device \
    discover_and_add_device \
	fmgr_dvmdb_script_execute \
	fmgr_system_report_group_groupby \
	fmgr_user_fortitoken \
    commit_config_to_device \
    execute_script \
    fmgr_dvm_cmd_del_device \
    fmgr_firewall_address6_tagging \
    fmgr_firewall_address_tagging \
    fmgr_firewall_addrgrp6_tagging \
    fmgr_firewall_addrgrp_dynamicmapping \
    fmgr_firewall_addrgrp_tagging \
    fmgr_firewall_gtp_apn \
    fmgr_firewall_identitybasedroute_rule__fact \
    commit_config_to_device \
    fmgr_firewall_multicastaddress6_tagging \
    fmgr_firewall_proxyaddress_tagging \
    fmgr_firewall_proxyaddrgrp_tagging \
    fmgr_ips_custom \
    fmgr_pkg_footer_policy6 \
    fmgr_system_admin_profile_datamaskcustomfields \
    fmgr_system_admin_profile_datamaskcustomfields__fact \
    fmgr_system_admin_user_metadata \
    fmgr_system_certificate_ca \
    fmgr_system_report_group_groupby \
    fmgr_system_report_group_groupby__fact \
    fmgr_user_device_tagging \
    fmgr_user_devicecategory \
    fmgr_user_devicegroup_tagging \

FILES_TO_IGNORE = $(foreach item, $(FILES_TO_IGNORE_FORSHORT), $(wildcard ./$(item).yml))
YML_FILES = $(YML_FILES_ORIGINAL)
$(foreach item, $(FILES_TO_IGNORE), \
	$(eval YML_FILES=$(filter-out $(item), $(YML_FILES))) \
 )
YML_FAKE_OBJECT = $(patsubst %.yml,%.fakeobject,$(YML_FILES))
YML_FILES := $(sort $(YML_FILES))

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
fmgr_pkg_footer_policy.yml: fmgr_pm_pkg_adom.fakeobject
fmgr_pkg_footer_policy__fact.yml: fmgr_pkg_footer_policy.fakeobject
fmgr_application_list_entries.yml: fmgr_application_list.fakeobject
fmgr_application_list_entries_parameters.yml: fmgr_application_list_entries.fakeobject
fmgr_application_list_entries_parameters__fact.yml: fmgr_application_list_entries_parameters.fakeobject
fmgr_firewall_vip46_dynamicmapping.yml: fmgr_firewall_vip46.fakeobject fmgr_dvm_cmd_add_device.fakeobject
	@echo "[CHECK] detected dependency for $@..."

%.fakeobject:%.yml
	@echo "[RUN] running testcase $< ..."
	@ansible-playbook -i hosts $< >/tmp/runtime.test 2>/tmp/ignore
	@touch $@

.PHONY:clean
clean:
	@rm -f *.fakeobject

.PHOONY: stats
stats:
	@echo "[STATS] `ls *.fakeobject |wc -l`/`ls *.yml |wc -l` pass"
