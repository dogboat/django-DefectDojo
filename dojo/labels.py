
from abc import abstractmethod, abstractproperty, ABC
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from django import template
from django.utils.text import capfirst
from django.utils.translation import pgettext, npgettext, gettext_lazy as _

from dojo.models import System_Settings


register = template.Library()


pgettext("term.v2.Organization", "product type")
pgettext("term.v3.Organization", "organization")
pgettext("term.v2.Asset", "product type")
pgettext("term.v3.Asset", "asset")


class OrganizationPhraseSet(ABC):
    @property
    @abstractmethod
    def object_label(self) -> str:
        pass

    @property
    @abstractmethod
    def options_label(self) -> str:
        pass

    @property
    @abstractmethod
    def report_label(self) -> str:
        pass

    @property
    @abstractmethod
    def add_label(self) -> str:
        pass

    @property
    @abstractmethod
    def edit_label(self) -> str:
        pass


"""
    labels.organization.label
    
    labels.organization.fields
        
        labels.organization.fields.critical_product.label
        labels.organization.fields.key_product.label

    labels.organization.options.label

    labels.organization.report.label

    labels.organization.list.label
    
    labels.organization.edit.label
    labels.organization.edit.success
    labels.organization.edit.failure
    
    labels.organization.new.label
    labels.organization.new.success
    labels.organization.new.failure
    
    labels.organization.delete.label
    labels.organization.delete.confirm
    labels.organization.delete.success
    labels.organization.delete.failure
    
"""

class AssetPhraseSet(ABC):
    @property
    @abstractmethod
    def object_label(self) -> str:
        pass


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




class V2OrgFields:
    critical_product = _("Critical Asset")
    key_product = _("Key Asset")
    members = V2OrgMembersLabels()
    groups = V2OrgGroupsLabels()
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
    name = _("Organization Name")
    name_help = _("Search for Organization names that are an exact match")
    name_exact = _("Exact Organization Name")
    name_contains = _("Organization Name Contains")
    name_contains_help = _("Search for Organization names that contain a given pattern")


class V2OrganizationLabels:
    label = _("Organization")
    label_plural = _("Organizations")
    label_all = _("All Organizations")
    none_found_label = _("No Organizations found")
    fields = V2OrgFields()
    filters = V2OrgFilterLabels()

    create = V2CreateOrgLabels()
    read = V2ReadOrgLabels()
    update = V2OrgUpdateLabels()
    delete = V2OrgDeleteLabels()

    options_label = _("Organization Options")
    report_label = _("Organization Report")
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
    name = _("Asset Name")
    name_exact = _("Exact Asset Name")
    name_contains = _("Asset Name Contains")


class V2AssetDeleteLabels:
    label = _("Delete Asset")
    success = _("Asset and relationships removed.")
    success_async = _("Asset and relationships will be removed in the background.")
    failure = _("Asset not deleted.")


class V2AssetUpdateLabels:
    label = _("Edit Asset")
    # label_with_name = _("Edit Asset %(name)s")
    success = _("Asset updated successfully.")
    failure = _("Asset not updated.")


class V2AssetLabels:
    label = _("Asset")
    label_plural = _("Assets")
    manager = _("Asset Manager")
    notifications_help = _("These are your personal settings for this Asset.")
    none_found_label = _("No Assets found.")
    label_all = _("All Assets")
    options_label = _("Asset Options")
    options_menu_label = _("Asset Options Menu")
    count_label = _("Asset Count")
    engagements_by = _("Engagements by Asset")
    lifecycle = _("Asset Lifecycle")

    add_tracking_files = _("Add Asset Tracking Files")
    view_tracking_files = _("View Asset Tracking Files")
    report_label = _("Asset Report")
    close_findings = _("Close old findings within this Asset")
    close_findings_help = _("This affects findings within the same product.")
    enable_tag_inheritance = _("Enable Asset Tag Inheritance")
    enable_tag_inheritance_help = _("Enables Asset tag inheritance. Any tags added on an Asset will automatically be added to all Engagements, Tests, and Findings.")

    create = V2AssetCreateLabels()
    update = V2AssetUpdateLabels()
    delete = V2AssetDeleteLabels()
    fields = V2AssetFieldsLabels()
    list = V2AssetListLabels()
    filters = V2AssetFilterLabels()


class V2UserLabels:
    label = _("User")
    label_all = _("All Users")

    whatever = _("Organizations this User can access")
    w_no_cces = _("This User is not assigned to any Organizations.")

    wahtervr = _("Assets this User can access")
    no_cces = _("This User is not assigned to any Assets.")



class V2GroupLabels:
    label = _("Group")
    label_all = _("All Groups")

    whatever = _("Organizations this Group can access")
    w_no_cces = _("This Group cannot access any Organizations.")

    wahtervr = _("Assets this Group can access")
    no_cces = _("This Group cannot access any Assets.")


class PhraseSet:
    #org = _("organization")
    #org_plural = _("organizations")

    # orgs
    # {{object}}
    # {{object}} options
    # {{object}} report
    # add {{object}}
    # no {{object}} found
    # add {{object}} member
    # add {{object}} group
    # register a new {{object}}
    # edit {{object}}


    # assets
    # {{object}}
    # critical {{object}}
    # key {{object}}


    pass


@dataclass(frozen=True)
class Label:
    _singular: str
    _plural: Optional[str] = None
    msgctxt: Optional[str] = None

    def _singular_localized(self) -> str:
        return pgettext(self.msgctxt, self._singular) if self.msgctxt else self._singular

    def _plural_localized(self, count: int) -> str:
        return npgettext(self.msgctxt or "", self._singular, self._plural or self._default_plural(), count)

    def _default_plural(self) -> str:
        # Apologies for the Anglocentrism
        return f"{self._singular}s"

    @property
    def cap(self):
        return capfirst(self._singular_localized())

    @property
    def plural(self):
        return self._plural_localized(2)

    @property
    def plural_cap(self):
        return self.plural.capitalize()

    def __str__(self):
        return self._singular_localized()

def easy_plural(s):
    return Label(s, f"{s}s")

# Want: To force all versions to respond to all things

class LabelableThing(ABC):
    @property
    @abstractmethod
    def organization(self) -> OrganizationPhraseSet:
        pass

    @property
    @abstractmethod
    def asset(self) -> AssetPhraseSet:
        pass


class V2Labels(LabelableThing):
    def __init__(self):
        self._organization = V2OrganizationLabels()
        self._asset = V2AssetLabels()

    @property
    def asset(self):
        return self._asset

    @property
    def organization(self):
        return self._organization

MyV3Labels = {
    'register_new_label': _("Register a new Organization"),
    'list_label':  _("List Organizations"),
    'add_successful_label': _("Organization added successfully"),
}

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

# labels.Organization.plural

def format_label(label, args):
    if not args:
        return label

    label_str = str(label)

