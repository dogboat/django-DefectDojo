
from abc import abstractmethod, abstractproperty, ABC
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from django import template
from django.utils.text import capfirst
from django.utils.translation import pgettext, npgettext, gettext_lazy as _

from dojo.models import System_Settings


register = template.Library()



class V2OrgListLabels:
    label = _("List Organizations")


class V2OrgMembersLabels:
    label = _("Members")
    delete_label = _("Delete Organization Member")
    delete_success = _("Organization member deleted successfully.")
    add_label = _("Add Organization Member")
    add_success = _("Organization members added successfully.")
    edit_label = _("Edit Organization Member")
    edit_success = _("Organization member updated successfully")
    minimum_number_label = _("There must be at least one owner for Organization %(name)s.")



class V2OrgGroupsLabels:
    label = _("Groups")

    add_label = _("Add Organization Group")
    add_success = _("Organization groups added successfully.")
    edit_label = _("Edit Organization Group")
    edit_success = _("Organization group updated successfully.")
    delete_label = _("Delete Organization Group")
    delete_success = _("Organization group deleted successfully.")

    can_access = _("Organizations this Group can access")
    no_access = _("This Group cannot access any Organizations.")


class V2OrgXUserLabels:
    label = _("Organizations this User can access")
    no_access = _("This User is not assigned to any Organizations.")

    add_organizations = _("Add Organizations")
    add_users = _("Add Members")

    delete_label = _("Delete Organization Member")
    delete_success = _("Organization member deleted successfully.")
    add_label = _("Add Organization Member")
    add_success = _("Organization members added successfully.")
    edit_label = _("Edit Organization Member")
    edit_success = _("Organization member updated successfully")
    minimum_number_label = _("There must be at least one owner for Organization %(name)s.")


class V2OrgXGroupLabels:
    label = _("Organizations this Group can access")
    no_access = _("This Group cannot access any Organizations.")

    add_organizations = _("Add Organizations")
    num_organizations = _("Number of Organizations")

    add_label = _("Add Organization Group")
    add_success = _("Organization groups added successfully.")

    edit_label = _("Edit Organization Group")
    edit_success = _("Organization group updated successfully.")

    delete_label = _("Delete Organization Group")
    delete_success = _("Organization group deleted successfully.")


class V2OrgMetricsLabels:
    by_findings = _("Organization Metrics by Findings")
    by_endpoints = _("Organization Metrics by Affected Endpoints")
    type_counts_error = _("Please choose month and year and the Organization.")


class V2OrgRelationshipsLabels:
    users = V2OrgXUserLabels()
    groups = V2OrgXGroupLabels()
    metrics = V2OrgMetricsLabels()


class V2AssetXGroupLabels:
    label = _("Assets this Group can access")
    no_access = _("This Group cannot access any Assets.")

    add_label = _("Add Asset Group")
    add_success = _("Asset Groups added successfully.")

    edit_label = _("Edit Asset Group")
    edit_success = _("Asset Group updated successfully.")

    delete_label = _("Delete Asset Group")
    delete_success = _("Asset Group deleted successfully.")

    add_asset = _("Add Assets")
    num_assets = _("Number of Assets")


class V2AssetXUserLabels:
    label = _("Assets this User can access")
    no_access = _("This User is not assigned to any Assets.")

    member_label = _("Asset Member")

    add_label = _("Add Asset Member")
    add_success = _("Asset members added successfully.")

    edit_label = _("Edit Asset Member")
    edit_success = _("Asset member updated successfully.")

    delete_label = _("Delete Asset Member")
    delete_success = _("Asset member deleted successfully.")

    add_assets = _("Add Assets")
    add_users = _("Add Users")


class V2AssetRelationshipsLabels:
    users = V2AssetXUserLabels()
    groups = V2AssetXGroupLabels()

    global_role_help = _("The global role will be applied to all Organizations and Assets.")


class V2OrgFields:
    critical_product = _("Critical Asset")
    key_product = _("Key Asset")
    #members = V2OrgMembersLabels()
    #groups = V2OrgGroupsLabels()
    add_group = _("Add Organization Group")


class V2OrgUpdateLabels:
    label = _("Edit Organization")
    label_with_name = _("Edit Organization %(name)s")
    success = _("Organization updated successfully.")
    failure = _("Organization not updated.")


class V2OrgsGroupsLabels:
    label = _("Groups")


class V2OrgDeleteLabels:
    label = _("Delete Organization")
    label_with_name = _("Delete Organization %(name)s")
    confirm = _("Deleting this Organization will remove any related objects associated with it. These relationships are listed below:")
    success = _("Organization and relationships removed.")
    success_async = _("Organization and relationships will be removed in the background.")
    failure = _("Organization not deleted.")


class V2CreateOrgLabels:
    label = _("Add Organization")
    success = _("Organization added successfully.")
    failure = _("Organization not added.")


class V2ReadOrgLabels:
    label = _("View Organization")


class V2OrgFilterLabels:
    label = _("Organization")
    label_help = _("Search for Organization names that are an exact match")

    name = _("Organization Name")
    name_help = _("Search for Organization names that are an exact match")

    name_exact = _("Exact Organization Name")

    name_contains = _("Organization Name Contains")
    name_contains_help = _("Search for Organization names that contain a given pattern")

    tags = _("Tags (Organization)")


class V2OrganizationLabels:
    label = _("Organization")
    label_plural = _("Organizations")
    label_all = _("All Organizations")
    label_with_name = _("Organization '%(name)s'")
    none_found_label = _("No Organizations found")
    fields = V2OrgFields()
    relationships = V2OrgRelationshipsLabels()
    filters = V2OrgFilterLabels()

    create = V2CreateOrgLabels()
    read = V2ReadOrgLabels()
    update = V2OrgUpdateLabels()
    delete = V2OrgDeleteLabels()

    options_label = _("Organization Options")
    report_label = _("Organization Report")
    report_title = _("Organization Report")

    notification_created_with_name = _("Organization %(name)s as been created successfully.")

    add_label = _("Add Organization")
    edit_label = _("Edit Organization")
    register_new_label = _("Register a new Organization")
    list_label = _("List Organizations")
    add_successful_label = _("Organization added successfully.")

    list = V2OrgListLabels()



class V2AssetGroupsLabels:
    access = _("Assets this Group can access")
    no_access = _("This Group cannot access any Assets.")


class V2AssetFieldsLabels:
    groups = V2AssetGroupsLabels()


class V2AssetCreateLabels:
    label = _("Add Asset")
    success = _("Asset added successfully.")
    failure = _("Organization not added")


class V2AssetListLabels:
    label = _("Asset List")


class V2AssetFilterLabels:
    label = _("Asset")

    name = _("Asset Name")
    name_help = _("Search for Asset names that are an exact match")

    name_exact = _("Exact Asset Name")

    name_contains = _("Asset Name Contains")
    name_contains_help = _("Search for Asset names that contain a given pattern")

    tags = _("Tags (Asset)")
    tags_help = _("Filter for Assets with the given tags")
    not_tags_help = _("Filter for Assets that do not have the given tags")

    assets_without_tags = _("Assets without tags")
    assets_without_tags_help = _("Search for tags on an Asset that contain a given pattern, and exclude them")
    tags_filter_help = _("Filter Assets by the selected tags")

    csv_tags_or = _("Comma separated list of exact tags present on Asset (uses OR for multiple values)")
    csv_tags_and = _("Comma separated list of exact tags to match with an AND expression present on Asset")
    csv_tags_not = _("Comma separated list of exact tags not present on Asset")
    csv_lifecycles = _("Comma separated list of exact Asset lifecycles")

    # Used in MetricsEndpointFilter and EndpointFilter and EndpointFilterWithoutObjectLookups
    tags_asset = _("Asset Tags")
    tag_asset = _("Asset Tag")
    tag_asset_help = _("Search for tags on an Asset that are an exact match")
    not_tags_asset = _("Not Asset Tags")
    without_tags = _("Asset without tags")
    tag_asset_contains = _("Asset Tag Contains")
    tag_asset_contains_help = _("Search for tags on an Asset that contain a given pattern")
    tag_not_contain = _("Asset Tag Does Not Contain")
    tag_not_contain_help = _("Search for tags on an Asset that contain a given pattern, and exclude them")
    tag_not = _("Not Asset Tag")
    tag_not_help = _("Search for tags on an Asset that are an exact match, and exclude them")



class V2AssetDeleteLabels:
    label = _("Delete Asset")
    success = _("Asset and relationships removed.")
    success_async = _("Asset and relationships will be removed in the background.")
    failure = _("Asset not deleted.")


class V2AssetUpdateLabels:
    label = _("Edit Asset")
    # label_with_name = _("Edit Asset %(name)s")
    success = _("Asset updated successfully.")
    sla_changed = _("All SLA expiration dates for Findings within this Asset will be recalculated asynchronously for the newly assigned SLA configuration.")
    failure = _("Asset not updated.")



class V2AssetLabels:
    label = _("Asset")
    label_plural = _("Assets")
    label_with_name = _("Asset '%(name)s'")

    manager = _("Asset Manager")
    notifications_help = _("These are your personal settings for this Asset.")
    none_found_label = _("No Assets found.")
    label_all = _("All Assets")
    options_label = _("Asset Options")
    options_menu_label = _("Asset Options Menu")
    count_label = _("Asset Count")
    engagements_by = _("Engagements by Asset")
    lifecycle = _("Asset Lifecycle")
    tag_label = _("Asset Tag")
    tag_counts_error = _("Please choose month and year and the Asset Tag.")
    notification_created_with_name = _("Asset %(name)s as been created successfully.")

    add_tracking_files = _("Add Asset Tracking Files")
    view_tracking_files = _("View Asset Tracking Files")
    report_label = _("Asset Report")

    report_title = _("Asset Report")

    close_findings = _("Close old findings within this Asset")
    close_findings_help = _("This affects findings within the same product.")
    enable_tag_inheritance = _("Enable Asset Tag Inheritance")
    enable_tag_inheritance_help = _("Enables Asset tag inheritance. Any tags added on an Asset will automatically be added to all Engagements, Tests, and Findings.")
    endpoint_help = _("The Asset this Endpoint should be associated with.")

    create = V2AssetCreateLabels()
    update = V2AssetUpdateLabels()
    delete = V2AssetDeleteLabels()

    list = V2AssetListLabels()

    filters = V2AssetFilterLabels()
    relationships = V2AssetRelationshipsLabels()


class V2Labels:
    def __init__(self):
        self._organization = V2OrganizationLabels()
        self._asset = V2AssetLabels()

    @property
    def asset(self):
        return self._asset

    @property
    def organization(self):
        return self._organization


class V3Labels:
    def __init__(self):
        self._organization = V2OrganizationLabels()
        self._asset = V2AssetLabels()

    @property
    def asset(self):
        return self._asset

    @property
    def organization(self):
        return self._organization


mah_map = {
    System_Settings.LabelsVersions.V2: V2Labels(),
    System_Settings.LabelsVersions.V3: V3Labels(),
}


def get_labels_version():
    return System_Settings.objects.get().labels_version


def get_labels():
    labels_version = get_labels_version()
    return V3Labels()
    #return {
    #    'organization': MyV3Labels # mah_map.get(labels_version, V2Labels())
    #}
