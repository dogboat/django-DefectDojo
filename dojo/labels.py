from django.utils.translation import gettext_lazy as _

from dojo.models import System_Settings


"""
    _label -> short label, used for UI/API fields
    _message -> a longer message displayed as a toast or displayed on the page
    _help -> helptext (for help_text kwargs/popover content)
    
    
"""


class K:
    ORG_LABEL = "org.label"
    ORG_PLURAL_LABEL = "org.plural_label"
    ORG_ALL_LABEL = "org.all_label"
    ORG_WITH_NAME_LABEL = "org.with_name_label"
    ORG_NONE_FOUND_MESSAGE = "org.none_found_label"
    ORG_REPORT_LABEL = "org.report_label"
    ORG_REPORT_TITLE = "org.report_title"
    ORG_REPORT_WITH_NAME_TITLE = "org.report_with_name_title"
    ORG_METRICS_BY_FINDINGS_LABEL = "org.metrics_by_findings_label"
    ORG_METRICS_BY_ENDPOINTS_LABEL = "org.metrics_by_endpoints_label"
    ORG_METRICS_TYPE_COUNTS_ERROR_MESSAGE = "org.metrics_type_counts_error_message"
    ORG_OPTIONS_LABEL = "org.options_label"
    ORG_NOTIFICATION_WITH_NAME_CREATED_MESSAGE = "org.notification_with_name_created_message"
    ORG_CRITICAL_PRODUCT_LABEL = "org.critical_product_label"
    ORG_KEY_PRODUCT_LABEL = "org.key_product_label"
    ORG_FILTERS_LABEL = "org.filters.label"
    ORG_FILTERS_LABEL_HELP = "org.filters.label_help"
    ORG_FILTERS_NAME_LABEL = "org.filters.name_label"
    ORG_FILTERS_NAME_HELP = "org.filters.name_help"
    ORG_FILTERS_NAME_EXACT_LABEL = "org.filters.name_exact_label"
    ORG_FILTERS_NAME_CONTAINS_LABEL = "org.filters.name_contains_label"
    ORG_FILTERS_NAME_CONTAINS_HELP = "org.filters.name_contains_help"
    ORG_FILTERS_TAGS_LABEL = "org.filters.tags_label"
    ORG_USERS_LABEL = "org.users.label"
    ORG_USERS_NO_ACCESS_MESSAGE = "org.users.no_access_message"
    ORG_USERS_ADD_ORGANIZATIONS_LABEL = "org.users.add_organizations_label"
    ORG_USERS_DELETE_LABEL = "org.users.delete_label"
    ORG_USERS_DELETE_SUCCESS_MESSAGE = "org.users.delete_success_message"
    ORG_USERS_ADD_LABEL = "org.users.add_label"
    ORG_USERS_ADD_SUCCESS_MESSAGE = "org.users.add_success_message"
    ORG_USERS_UPDATE_LABEL = "org.users.update_label"
    ORG_USERS_UPDATE_SUCCESS_MESSAGE = "org.users.update_success_message"
    ORG_USERS_MINIMUM_NUMBER_WITH_NAME_MESSAGE = "org.users.minimum_number_with_name_message"
    ORG_GROUPS_LABEL = "org.groups.label"
    ORG_GROUPS_NO_ACCESS_MESSAGE = "org.groups.no_access_message"
    ORG_GROUPS_ADD_ORGANIZATIONS_LABEL = "org.groups.add_organizations_label"
    ORG_GROUPS_NUM_ORGANIZATIONS_LABEL = "org.groups.num_organizations_label"
    ORG_GROUPS_ADD_LABEL = "org.groups.add_label"
    ORG_GROUPS_ADD_SUCCESS_MESSAGE = "org.groups.add_success_message"
    ORG_GROUPS_UPDATE_LABEL = "org.groups.update_label"
    ORG_GROUPS_UPDATE_SUCCESS_MESSAGE = "org.groups.update_success_message"
    ORG_GROUPS_DELETE_LABEL = "org.groups.delete_label"
    ORG_GROUPS_DELETE_SUCCESS_MESSAGE = "org.groups.delete_success_message"
    ORG_CREATE_LABEL = "org.create.label"
    ORG_CREATE_SUCCESS_MESSAGE = "org.create.success_message"
    ORG_READ_LABEL = "org.read.label"
    ORG_READ_LIST_LABEL = "org.read.list_label"
    ORG_UPDATE_LABEL = "org.update.label"
    ORG_UPDATE_WITH_NAME_LABEL = "org.update.with_name_label"
    ORG_UPDATE_SUCCESS_MESSAGE = "org.update.success_message"
    ORG_DELETE_LABEL = "org.delete.label"
    ORG_DELETE_WITH_NAME_LABEL = "org.delete.with_name_label"
    ORG_DELETE_CONFIRM_MESSAGE = "org.delete.confirm_message"
    ORG_DELETE_SUCCESS_MESSAGE = "org.delete.success_message"
    ORG_DELETE_SUCCESS_ASYNC_MESSAGE = "org.delete.success_async_message"
    ASSET_LABEL = "asset.label"
    ASSET_PLURAL_LABEL = "asset.plural_label"
    ASSET_ALL_LABEL = "asset.all_label"
    ASSET_WITH_NAME_LABEL = "asset.with_name_label"
    ASSET_NONE_FOUND_MESSAGE = "asset.none_found_label"
    ASSET_MANAGER_LABEL = "asset.manager_label"
    ASSET_GLOBAL_ROLE_HELP = "asset.global_role_help"
    ASSET_NOTIFICATIONS_HELP = "asset.notifications_help"
    ASSET_OPTIONS_LABEL = "asset.options_label"
    ASSET_OPTIONS_MENU_LABEL = "asset.options_menu_label"
    ASSET_COUNT_LABEL = "asset.count_label"
    ASSET_ENGAGEMENTS_BY_LABEL = "asset.engagements_by_label"
    ASSET_LIFECYCLE_LABEL = "asset.lifecycle_label"
    ASSET_TAG_LABEL = "asset.tag_label"
    ASSET_METRICS_TAG_COUNTS_ERROR_MESSAGE = "asset.metrics_tag_counts_error_message"
    ASSET_NOTIFICATION_WITH_NAME_CREATED_MESSAGE = "asset.notification_with_name_created_message"
    ASSET_REPORT_LABEL = "asset.report_label"
    ASSET_REPORT_TITLE = "asset.report_title"
    ASSET_REPORT_WITH_NAME_TITLE = "asset.report_with_name_title"
    ASSET_TRACKING_FILES_ADD_LABEL = "asset.tracking_files_add_label"
    ASSET_TRACKING_FILES_VIEW_LABEL = "asset.tracking_files_view_label"
    ASSET_FINDINGS_CLOSE_LABEL = "asset.findings_close_label"
    ASSET_FINDINGS_CLOSE_HELP = "asset.findings_close_help"
    ASSET_TAG_INHERITANCE_ENABLE_LABEL = "asset.tag_inheritance_enable_label"
    ASSET_TAG_INHERITANCE_ENABLE_HELP = "asset.tag_inheritance_enable_help"
    ASSET_ENDPOINT_HELP = "asset.endpoint_help"
    ASSET_CREATE_LABEL = "asset.create.label"
    ASSET_CREATE_SUCCESS_MESSAGE = "asset.create.success_message"
    ASSET_READ_LIST_LABEL = "asset.read.list_label"
    ASSET_UPDATE_LABEL = "asset.update.label"
    ASSET_UPDATE_SUCCESS_MESSAGE = "asset.update.success_message"
    ASSET_UPDATE_SLA_CHANGED_MESSAGE = "asset.update.sla_changed_message"
    ASSET_DELETE_LABEL = "asset.delete.label"
    ASSET_DELETE_WITH_NAME_LABEL = "asset.delete.with_name_label"
    ASSET_DELETE_CONFIRM_MESSAGE = "asset.delete.confirm_message"
    ASSET_DELETE_SUCCESS_MESSAGE = "asset.delete.success_message"
    ASSET_DELETE_SUCCESS_ASYNC_MESSAGE = "asset.delete.success_async_message"
    ASSET_FILTERS_LABEL = "asset.filters.label"
    ASSET_FILTERS_NAME_LABEL = "asset.filters.name_label"
    ASSET_FILTERS_NAME_HELP = "asset.filters.name_help"
    ASSET_FILTERS_NAME_EXACT = "asset.filters.name_exact"
    ASSET_FILTERS_NAME_CONTAINS_LABEL = "asset.filters.name_contains_label"
    ASSET_FILTERS_NAME_CONTAINS_HELP = "asset.filters.name_contains_help"
    ASSET_FILTERS_TAGS_LABEL = "asset.filters.tags_label"
    ASSET_FILTERS_TAGS_HELP = "asset.filters.tags_help"
    ASSET_FILTERS_NOT_TAGS_HELP = "asset.filters.not_tags_help"
    ASSET_FILTERS_ASSETS_WITHOUT_TAGS_LABEL = "asset.filters.assets_without_tags_label"
    ASSET_FILTERS_ASSETS_WITHOUT_TAGS_HELP = "asset.filters.assets_without_tags_help"
    ASSET_FILTERS_TAGS_FILTER_HELP = "asset.filters.tags_filter_help"
    ASSET_FILTERS_CSV_TAGS_OR_HELP = "asset.filters.csv_tags_or_help"
    ASSET_FILTERS_CSV_TAGS_AND_HELP = "asset.filters.csv_tags_and_help"
    ASSET_FILTERS_CSV_TAGS_NOT_HELP = "asset.filters.csv_tags_not_help"
    ASSET_FILTERS_CSV_LIFECYCLES_HELP = "asset.filters.csv_lifecycles_help"
    ASSET_FILTERS_TAGS_ASSET_LABEL = "asset.filters.tags_asset_label"
    ASSET_FILTERS_TAG_ASSET_LABEL = "asset.filters.tag_asset_label"
    ASSET_FILTERS_TAG_ASSET_HELP = "asset.filters.tag_asset_help"
    ASSET_FILTERS_NOT_TAGS_ASSET_LABEL = "asset.filters.not_tags_asset_label"
    ASSET_FILTERS_WITHOUT_TAGS_LABEL = "asset.filters.without_tags_label"
    ASSET_FILTERS_TAG_ASSET_CONTAINS_LABEL = "asset.filters.tag_asset_contains_label"
    ASSET_FILTERS_TAG_ASSET_CONTAINS_HELP = "asset.filters.tag_asset_contains_help"
    ASSET_FILTERS_TAG_NOT_CONTAIN_LABEL = "asset.filters.tag_not_contain_label"
    ASSET_FILTERS_TAG_NOT_CONTAIN_HELP = "asset.filters.tag_not_contain_help"
    ASSET_FILTERS_TAG_NOT_LABEL = "asset.filters.tag_not_label"
    ASSET_FILTERS_TAG_NOT_HELP = "asset.filters.tag_not_help"
    ASSET_USERS_ACCESS_LABEL = "asset.users.access_label"
    ASSET_USERS_NO_ACCESS_MESSAGE = "asset.users.no_access_message"
    ASSET_USERS_ADD_LABEL = "asset.users.add_label"
    ASSET_USERS_USERS_ADD_LABEL = "asset.users.users_add_label"
    ASSET_USERS_MEMBER_LABEL = "asset.users.member_label"
    ASSET_USERS_MEMBER_ADD_LABEL = "asset.users.member_add_label"
    ASSET_USERS_MEMBER_ADD_SUCCESS_MESSAGE = "asset.users.member_add_success_message"
    ASSET_USERS_MEMBER_UPDATE_LABEL = "asset.users.member_update_label"
    ASSET_USERS_MEMBER_UPDATE_SUCCESS_MESSAGE = "asset.users.member_update_success_message"
    ASSET_USERS_MEMBER_DELETE_LABEL = "asset.users.member_delete_label"
    ASSET_USERS_MEMBER_DELETE_SUCCESS_MESSAGE = "asset.users.member_delete_success_message"
    ASSET_GROUPS_ACCESS_LABEL = "asset.groups.access_label"
    ASSET_GROUPS_NO_ACCESS_MESSAGE = "asset.groups.no_access_message"
    ASSET_GROUPS_MEMBER_LABEL = "asset.groups.member_label"
    ASSET_GROUPS_ADD_LABEL = "asset.groups.add_label"
    ASSET_GROUPS_ADD_SUCCESS_MESSAGE = "asset.groups.add_success_message"
    ASSET_GROUPS_UPDATE_LABEL = "asset.groups.update_label"
    ASSET_GROUPS_UPDATE_SUCCESS_MESSAGE = "asset.groups.update_success_message"
    ASSET_GROUPS_DELETE_LABEL = "asset.groups.delete_label"
    ASSET_GROUPS_DELETE_SUCCESS_MESSAGE = "asset.groups.delete_success_message"
    ASSET_GROUPS_ADD_ASSETS_LABEL = "asset.groups.add_assets_label"
    ASSET_GROUPS_NUM_ASSETS_LABEL = "asset.groups.num_assets_label"


V2_LABELS = {
    K.ORG_LABEL: _("Product Type"),
    K.ORG_PLURAL_LABEL: _("Product Types"),
    K.ORG_ALL_LABEL: _("All Product Types"),
    K.ORG_WITH_NAME_LABEL: _("Product Type '%(name)s'"),
    K.ORG_NONE_FOUND_MESSAGE: _("No Product Types found"),
    K.ORG_REPORT_LABEL: _("Product Type Report"),
    K.ORG_REPORT_TITLE: _("Product Type Report"),
    K.ORG_REPORT_WITH_NAME_TITLE: _("Product Type Report: %(name)s"),
    K.ORG_METRICS_BY_FINDINGS_LABEL: _("Product Type Metrics by Findings"),
    K.ORG_METRICS_BY_ENDPOINTS_LABEL: _("Product Type Metrics by Affected Endpoints"),
    K.ORG_METRICS_TYPE_COUNTS_ERROR_MESSAGE: _("Please choose month and year and the Product Type."),
    K.ORG_OPTIONS_LABEL: _("Product Type Options"),
    K.ORG_NOTIFICATION_WITH_NAME_CREATED_MESSAGE: _("Product Type %(name)s as been created successfully."),
    K.ORG_CRITICAL_PRODUCT_LABEL: _("Critical Product"),
    K.ORG_KEY_PRODUCT_LABEL: _("Key Product"),
    K.ORG_FILTERS_LABEL: _("Product Type"),
    K.ORG_FILTERS_LABEL_HELP: _("Search for Product Type names that are an exact match"),
    K.ORG_FILTERS_NAME_LABEL: _("Product Type Name"),
    K.ORG_FILTERS_NAME_HELP: _("Search for Product Type names that are an exact match"),
    K.ORG_FILTERS_NAME_EXACT_LABEL: _("Exact Product Type Name"),
    K.ORG_FILTERS_NAME_CONTAINS_LABEL: _("Product Type Name Contains"),
    K.ORG_FILTERS_NAME_CONTAINS_HELP: _("Search for Product Type names that contain a given pattern"),
    K.ORG_FILTERS_TAGS_LABEL: _("Tags (Product Type)"),
    K.ORG_USERS_LABEL: _("Product Types this User can access"),
    K.ORG_USERS_NO_ACCESS_MESSAGE: _("This User is not assigned to any Product Types."),
    K.ORG_USERS_ADD_ORGANIZATIONS_LABEL: _("Add Product Types"),
    K.ORG_USERS_DELETE_LABEL: _("Delete Product Type Member"),
    K.ORG_USERS_DELETE_SUCCESS_MESSAGE: _("Product Type member deleted successfully."),
    K.ORG_USERS_ADD_LABEL: _("Add Product Type Member"),
    K.ORG_USERS_ADD_SUCCESS_MESSAGE: _("Product Type members added successfully."),
    K.ORG_USERS_UPDATE_LABEL: _("Edit Product Type Member"),
    K.ORG_USERS_UPDATE_SUCCESS_MESSAGE: _("Product Type member updated successfully"),
    K.ORG_USERS_MINIMUM_NUMBER_WITH_NAME_MESSAGE: _("There must be at least one owner for Product Type %(name)s."),
    K.ORG_GROUPS_LABEL: _("Product Types this Group can access"),
    K.ORG_GROUPS_NO_ACCESS_MESSAGE: _("This Group cannot access any Product Types."),
    K.ORG_GROUPS_ADD_ORGANIZATIONS_LABEL: _("Add Product Types"),
    K.ORG_GROUPS_NUM_ORGANIZATIONS_LABEL: _("Number of Product Types"),
    K.ORG_GROUPS_ADD_LABEL: _("Add Product Type Group"),
    K.ORG_GROUPS_ADD_SUCCESS_MESSAGE: _("Product Type groups added successfully."),
    K.ORG_GROUPS_UPDATE_LABEL: _("Edit Product Type Group"),
    K.ORG_GROUPS_UPDATE_SUCCESS_MESSAGE: _("Product Type group updated successfully."),
    K.ORG_GROUPS_DELETE_LABEL: _("Delete Product Type Group"),
    K.ORG_GROUPS_DELETE_SUCCESS_MESSAGE: _("Product Type group deleted successfully."),
    K.ORG_CREATE_LABEL: _("Add Product Type"),
    K.ORG_CREATE_SUCCESS_MESSAGE: _("Product Type added successfully."),
    K.ORG_READ_LABEL: _("View Product Type"),
    K.ORG_READ_LIST_LABEL: _("List Product Types"),
    K.ORG_UPDATE_LABEL: _("Edit Product Type"),
    K.ORG_UPDATE_WITH_NAME_LABEL: _("Edit Product Type %(name)s"),
    K.ORG_UPDATE_SUCCESS_MESSAGE: _("Product Type updated successfully."),
    K.ORG_DELETE_LABEL: _("Delete Product Type"),
    K.ORG_DELETE_WITH_NAME_LABEL: _("Delete Product Type %(name)s"),
    K.ORG_DELETE_CONFIRM_MESSAGE: _(
        "Deleting this Product Type will remove any related objects associated with it. These relationships are listed below:"),
    K.ORG_DELETE_SUCCESS_MESSAGE: _("Product Type and relationships removed."),
    K.ORG_DELETE_SUCCESS_ASYNC_MESSAGE: _("Product Type and relationships will be removed in the background."),
    K.ASSET_LABEL: _("Product"),
    K.ASSET_PLURAL_LABEL: _("Products"),
    K.ASSET_ALL_LABEL: _("All Products"),
    K.ASSET_WITH_NAME_LABEL: _("Product '%(name)s'"),
    K.ASSET_NONE_FOUND_MESSAGE: _("No Products found."),
    K.ASSET_MANAGER_LABEL: _("Product Manager"),
    K.ASSET_GLOBAL_ROLE_HELP: _("The global role will be applied to all Product Types and Products."),
    K.ASSET_NOTIFICATIONS_HELP: _("These are your personal settings for this Product."),
    K.ASSET_OPTIONS_LABEL: _("Product Options"),
    K.ASSET_OPTIONS_MENU_LABEL: _("Product Options Menu"),
    K.ASSET_COUNT_LABEL: _("Product Count"),
    K.ASSET_ENGAGEMENTS_BY_LABEL: _("Engagements by Product"),
    K.ASSET_LIFECYCLE_LABEL: _("Product Lifecycle"),
    K.ASSET_TAG_LABEL: _("Product Tag"),
    K.ASSET_METRICS_TAG_COUNTS_ERROR_MESSAGE: _("Please choose month and year and the Product Tag."),
    K.ASSET_NOTIFICATION_WITH_NAME_CREATED_MESSAGE: _("Product %(name)s as been created successfully."),
    K.ASSET_REPORT_LABEL: _("Product Report"),
    K.ASSET_REPORT_TITLE: _("Product Report"),
    K.ASSET_REPORT_WITH_NAME_TITLE: _("Product Report: %(name)s"),
    K.ASSET_TRACKING_FILES_ADD_LABEL: _("Add Product Tracking Files"),
    K.ASSET_TRACKING_FILES_VIEW_LABEL: _("View Product Tracking Files"),
    K.ASSET_FINDINGS_CLOSE_LABEL: _("Close old findings within this Product"),
    K.ASSET_FINDINGS_CLOSE_HELP: _("This affects findings within the same product."),
    K.ASSET_TAG_INHERITANCE_ENABLE_LABEL: _("Enable Product Tag Inheritance"),
    K.ASSET_TAG_INHERITANCE_ENABLE_HELP: _(
        "Enables Product tag inheritance. Any tags added on an Product will automatically be added to all Engagements, Tests, and Findings."),
    K.ASSET_ENDPOINT_HELP: _("The Product this Endpoint should be associated with."),
    K.ASSET_CREATE_LABEL: _("Add Product"),
    K.ASSET_CREATE_SUCCESS_MESSAGE: _("Product added successfully."),
    K.ASSET_READ_LIST_LABEL: _("Product List"),
    K.ASSET_UPDATE_LABEL: _("Edit Product"),
    K.ASSET_UPDATE_SUCCESS_MESSAGE: _("Product updated successfully."),
    K.ASSET_UPDATE_SLA_CHANGED_MESSAGE: _(
        "All SLA expiration dates for Findings within this Product will be recalculated asynchronously for the newly assigned SLA configuration."),
    K.ASSET_DELETE_LABEL: _("Delete Product"),
    K.ASSET_DELETE_WITH_NAME_LABEL: _("Delete Product %(name)s"),
    K.ASSET_DELETE_CONFIRM_MESSAGE: _(
        "Deleting this Product will remove any related objects associated with it. These relationships are listed below: "),
    K.ASSET_DELETE_SUCCESS_MESSAGE: _("Product and relationships removed."),
    K.ASSET_DELETE_SUCCESS_ASYNC_MESSAGE: _("Product and relationships will be removed in the background."),
    K.ASSET_FILTERS_LABEL: _("Product"),
    K.ASSET_FILTERS_NAME_LABEL: _("Product Name"),
    K.ASSET_FILTERS_NAME_HELP: _("Search for Product names that are an exact match"),
    K.ASSET_FILTERS_NAME_EXACT: _("Exact Product Name"),
    K.ASSET_FILTERS_NAME_CONTAINS_LABEL: _("Product Name Contains"),
    K.ASSET_FILTERS_NAME_CONTAINS_HELP: _("Search for Product names that contain a given pattern"),
    K.ASSET_FILTERS_TAGS_LABEL: _("Tags (Product)"),
    K.ASSET_FILTERS_TAGS_HELP: _("Filter for Products with the given tags"),
    K.ASSET_FILTERS_NOT_TAGS_HELP: _("Filter for Products that do not have the given tags"),
    K.ASSET_FILTERS_ASSETS_WITHOUT_TAGS_LABEL: _("Products without tags"),
    K.ASSET_FILTERS_ASSETS_WITHOUT_TAGS_HELP: _(
        "Search for tags on an Product that contain a given pattern, and exclude them"),
    K.ASSET_FILTERS_TAGS_FILTER_HELP: _("Filter Products by the selected tags"),
    K.ASSET_FILTERS_CSV_TAGS_OR_HELP: _(
        "Comma separated list of exact tags present on Product (uses OR for multiple values)"),
    K.ASSET_FILTERS_CSV_TAGS_AND_HELP: _(
        "Comma separated list of exact tags to match with an AND expression present on Product"),
    K.ASSET_FILTERS_CSV_TAGS_NOT_HELP: _("Comma separated list of exact tags not present on Product"),
    K.ASSET_FILTERS_CSV_LIFECYCLES_HELP: _("Comma separated list of exact Product lifecycles"),
    K.ASSET_FILTERS_TAGS_ASSET_LABEL: _("Product Tags"),
    K.ASSET_FILTERS_TAG_ASSET_LABEL: _("Product Tag"),
    K.ASSET_FILTERS_TAG_ASSET_HELP: _("Search for tags on an Product that are an exact match"),
    K.ASSET_FILTERS_NOT_TAGS_ASSET_LABEL: _("Not Product Tags"),
    K.ASSET_FILTERS_WITHOUT_TAGS_LABEL: _("Product without tags"),
    K.ASSET_FILTERS_TAG_ASSET_CONTAINS_LABEL: _("Product Tag Contains"),
    K.ASSET_FILTERS_TAG_ASSET_CONTAINS_HELP: _("Search for tags on an Product that contain a given pattern"),
    K.ASSET_FILTERS_TAG_NOT_CONTAIN_LABEL: _("Product Tag Does Not Contain"),
    K.ASSET_FILTERS_TAG_NOT_CONTAIN_HELP: _(
        "Search for tags on an Product that contain a given pattern, and exclude them"),
    K.ASSET_FILTERS_TAG_NOT_LABEL: _("Not Product Tag"),
    K.ASSET_FILTERS_TAG_NOT_HELP: _("Search for tags on an Product that are an exact match, and exclude them"),
    K.ASSET_USERS_ACCESS_LABEL: _("Products this User can access"),
    K.ASSET_USERS_NO_ACCESS_MESSAGE: _("This User is not assigned to any Products."),
    K.ASSET_USERS_ADD_LABEL: _("Add Products"),
    K.ASSET_USERS_USERS_ADD_LABEL: _("Add Users"),
    K.ASSET_USERS_MEMBER_LABEL: _("Product Member"),
    K.ASSET_USERS_MEMBER_ADD_LABEL: _("Add Product Member"),
    K.ASSET_USERS_MEMBER_ADD_SUCCESS_MESSAGE: _("Product members added successfully."),
    K.ASSET_USERS_MEMBER_UPDATE_LABEL: _("Edit Product Member"),
    K.ASSET_USERS_MEMBER_UPDATE_SUCCESS_MESSAGE: _("Product member updated successfully."),
    K.ASSET_USERS_MEMBER_DELETE_LABEL: _("Delete Product Member"),
    K.ASSET_USERS_MEMBER_DELETE_SUCCESS_MESSAGE: _("Product member deleted successfully."),
    K.ASSET_GROUPS_ACCESS_LABEL: _("Products this Group can access"),
    K.ASSET_GROUPS_NO_ACCESS_MESSAGE: _("This Group cannot access any Products."),
    K.ASSET_GROUPS_MEMBER_LABEL: _("Product Group"),
    K.ASSET_GROUPS_ADD_LABEL: _("Add Product Group"),
    K.ASSET_GROUPS_ADD_SUCCESS_MESSAGE: _("Product Groups added successfully."),
    K.ASSET_GROUPS_UPDATE_LABEL: _("Edit Product Group"),
    K.ASSET_GROUPS_UPDATE_SUCCESS_MESSAGE: _("Product Group updated successfully."),
    K.ASSET_GROUPS_DELETE_LABEL: _("Delete Product Group"),
    K.ASSET_GROUPS_DELETE_SUCCESS_MESSAGE: _("Product Group deleted successfully."),
    K.ASSET_GROUPS_ADD_ASSETS_LABEL: _("Add Products"),
    K.ASSET_GROUPS_NUM_ASSETS_LABEL: _("Number of Products"),
}


V3_LABELS = {
    K.ORG_LABEL: _("Organization"),
    K.ORG_PLURAL_LABEL: _("Organizations"),
    K.ORG_ALL_LABEL: _("All Organizations"),
    K.ORG_WITH_NAME_LABEL: _("Organization '%(name)s'"),
    K.ORG_NONE_FOUND_MESSAGE: _("No Organizations found"),
    K.ORG_REPORT_LABEL: _("Organization Report"),
    K.ORG_REPORT_TITLE: _("Organization Report"),
    K.ORG_REPORT_WITH_NAME_TITLE: _("Organization Report: %(name)s"),
    K.ORG_METRICS_BY_FINDINGS_LABEL: _("Organization Metrics by Findings"),
    K.ORG_METRICS_BY_ENDPOINTS_LABEL: _("Organization Metrics by Affected Endpoints"),
    K.ORG_METRICS_TYPE_COUNTS_ERROR_MESSAGE: _("Please choose month and year and the Organization."),
    K.ORG_OPTIONS_LABEL: _("Organization Options"),
    K.ORG_NOTIFICATION_WITH_NAME_CREATED_MESSAGE: _("Organization %(name)s as been created successfully."),
    K.ORG_CRITICAL_PRODUCT_LABEL: _("Critical Asset"),
    K.ORG_KEY_PRODUCT_LABEL: _("Key Asset"),
    K.ORG_FILTERS_LABEL: _("Organization"),
    K.ORG_FILTERS_LABEL_HELP: _("Search for Organization names that are an exact match"),
    K.ORG_FILTERS_NAME_LABEL: _("Organization Name"),
    K.ORG_FILTERS_NAME_HELP: _("Search for Organization names that are an exact match"),
    K.ORG_FILTERS_NAME_EXACT_LABEL: _("Exact Organization Name"),
    K.ORG_FILTERS_NAME_CONTAINS_LABEL: _("Organization Name Contains"),
    K.ORG_FILTERS_NAME_CONTAINS_HELP: _("Search for Organization names that contain a given pattern"),
    K.ORG_FILTERS_TAGS_LABEL: _("Tags (Organization)"),
    K.ORG_USERS_LABEL: _("Organizations this User can access"),
    K.ORG_USERS_NO_ACCESS_MESSAGE: _("This User is not assigned to any Organizations."),
    K.ORG_USERS_ADD_ORGANIZATIONS_LABEL: _("Add Organizations"),
    K.ORG_USERS_DELETE_LABEL: _("Delete Organization Member"),
    K.ORG_USERS_DELETE_SUCCESS_MESSAGE: _("Organization member deleted successfully."),
    K.ORG_USERS_ADD_LABEL: _("Add Organization Member"),
    K.ORG_USERS_ADD_SUCCESS_MESSAGE: _("Organization members added successfully."),
    K.ORG_USERS_UPDATE_LABEL: _("Edit Organization Member"),
    K.ORG_USERS_UPDATE_SUCCESS_MESSAGE: _("Organization member updated successfully"),
    K.ORG_USERS_MINIMUM_NUMBER_WITH_NAME_MESSAGE: _("There must be at least one owner for Organization %(name)s."),
    K.ORG_GROUPS_LABEL: _("Organizations this Group can access"),
    K.ORG_GROUPS_NO_ACCESS_MESSAGE: _("This Group cannot access any Organizations."),
    K.ORG_GROUPS_ADD_ORGANIZATIONS_LABEL: _("Add Organizations"),
    K.ORG_GROUPS_NUM_ORGANIZATIONS_LABEL: _("Number of Organizations"),
    K.ORG_GROUPS_ADD_LABEL: _("Add Organization Group"),
    K.ORG_GROUPS_ADD_SUCCESS_MESSAGE: _("Organization groups added successfully."),
    K.ORG_GROUPS_UPDATE_LABEL: _("Edit Organization Group"),
    K.ORG_GROUPS_UPDATE_SUCCESS_MESSAGE: _("Organization group updated successfully."),
    K.ORG_GROUPS_DELETE_LABEL: _("Delete Organization Group"),
    K.ORG_GROUPS_DELETE_SUCCESS_MESSAGE: _("Organization group deleted successfully."),
    K.ORG_CREATE_LABEL: _("Add Organization"),
    K.ORG_CREATE_SUCCESS_MESSAGE: _("Organization added successfully."),
    K.ORG_READ_LABEL: _("View Organization"),
    K.ORG_READ_LIST_LABEL: _("List Organizations"),
    K.ORG_UPDATE_LABEL: _("Edit Organization"),
    K.ORG_UPDATE_WITH_NAME_LABEL: _("Edit Organization %(name)s"),
    K.ORG_UPDATE_SUCCESS_MESSAGE: _("Organization updated successfully."),
    K.ORG_DELETE_LABEL: _("Delete Organization"),
    K.ORG_DELETE_WITH_NAME_LABEL: _("Delete Organization %(name)s"),
    K.ORG_DELETE_CONFIRM_MESSAGE: _("Deleting this Organization will remove any related objects associated with it. These relationships are listed below:"),
    K.ORG_DELETE_SUCCESS_MESSAGE: _("Organization and relationships removed."),
    K.ORG_DELETE_SUCCESS_ASYNC_MESSAGE: _("Organization and relationships will be removed in the background."),
    K.ASSET_LABEL: _("Asset"),
    K.ASSET_PLURAL_LABEL: _("Assets"),
    K.ASSET_ALL_LABEL: _("All Assets"),
    K.ASSET_WITH_NAME_LABEL: _("Asset '%(name)s'"),
    K.ASSET_NONE_FOUND_MESSAGE: _("No Assets found."),
    K.ASSET_MANAGER_LABEL: _("Asset Manager"),
    K.ASSET_GLOBAL_ROLE_HELP: _("The global role will be applied to all Organizations and Assets."),
    K.ASSET_NOTIFICATIONS_HELP: _("These are your personal settings for this Asset."),
    K.ASSET_OPTIONS_LABEL: _("Asset Options"),
    K.ASSET_OPTIONS_MENU_LABEL: _("Asset Options Menu"),
    K.ASSET_COUNT_LABEL: _("Asset Count"),
    K.ASSET_ENGAGEMENTS_BY_LABEL: _("Engagements by Asset"),
    K.ASSET_LIFECYCLE_LABEL: _("Asset Lifecycle"),
    K.ASSET_TAG_LABEL: _("Asset Tag"),
    K.ASSET_METRICS_TAG_COUNTS_ERROR_MESSAGE: _("Please choose month and year and the Asset Tag."),
    K.ASSET_NOTIFICATION_WITH_NAME_CREATED_MESSAGE: _("Asset %(name)s as been created successfully."),
    K.ASSET_REPORT_LABEL: _("Asset Report"),
    K.ASSET_REPORT_TITLE: _("Asset Report"),
    K.ASSET_REPORT_WITH_NAME_TITLE: _("Asset Report: %(name)s"),
    K.ASSET_TRACKING_FILES_ADD_LABEL: _("Add Asset Tracking Files"),
    K.ASSET_TRACKING_FILES_VIEW_LABEL: _("View Asset Tracking Files"),
    K.ASSET_FINDINGS_CLOSE_LABEL: _("Close old findings within this Asset"),
    K.ASSET_FINDINGS_CLOSE_HELP: _("This affects findings within the same product."),
    K.ASSET_TAG_INHERITANCE_ENABLE_LABEL: _("Enable Asset Tag Inheritance"),
    K.ASSET_TAG_INHERITANCE_ENABLE_HELP: _("Enables Asset tag inheritance. Any tags added on an Asset will automatically be added to all Engagements, Tests, and Findings."),
    K.ASSET_ENDPOINT_HELP: _("The Asset this Endpoint should be associated with."),
    K.ASSET_CREATE_LABEL: _("Add Asset"),
    K.ASSET_CREATE_SUCCESS_MESSAGE: _("Asset added successfully."),
    K.ASSET_READ_LIST_LABEL: _("Asset List"),
    K.ASSET_UPDATE_LABEL: _("Edit Asset"),
    K.ASSET_UPDATE_SUCCESS_MESSAGE: _("Asset updated successfully."),
    K.ASSET_UPDATE_SLA_CHANGED_MESSAGE: _("All SLA expiration dates for Findings within this Asset will be recalculated asynchronously for the newly assigned SLA configuration."),
    K.ASSET_DELETE_LABEL: _("Delete Asset"),
    K.ASSET_DELETE_WITH_NAME_LABEL: _("Delete Asset %(name)s"),
    K.ASSET_DELETE_CONFIRM_MESSAGE: _(
        "Deleting this Asset will remove any related objects associated with it. These relationships are listed below: "),
    K.ASSET_DELETE_SUCCESS_MESSAGE: _("Asset and relationships removed."),
    K.ASSET_DELETE_SUCCESS_ASYNC_MESSAGE: _("Asset and relationships will be removed in the background."),
    K.ASSET_FILTERS_LABEL: _("Asset"),
    K.ASSET_FILTERS_NAME_LABEL: _("Asset Name"),
    K.ASSET_FILTERS_NAME_HELP: _("Search for Asset names that are an exact match"),
    K.ASSET_FILTERS_NAME_EXACT: _("Exact Asset Name"),
    K.ASSET_FILTERS_NAME_CONTAINS_LABEL: _("Asset Name Contains"),
    K.ASSET_FILTERS_NAME_CONTAINS_HELP: _("Search for Asset names that contain a given pattern"),
    K.ASSET_FILTERS_TAGS_LABEL: _("Tags (Asset)"),
    K.ASSET_FILTERS_TAGS_HELP: _("Filter for Assets with the given tags"),
    K.ASSET_FILTERS_NOT_TAGS_HELP: _("Filter for Assets that do not have the given tags"),
    K.ASSET_FILTERS_ASSETS_WITHOUT_TAGS_LABEL: _("Assets without tags"),
    K.ASSET_FILTERS_ASSETS_WITHOUT_TAGS_HELP: _("Search for tags on an Asset that contain a given pattern, and exclude them"),
    K.ASSET_FILTERS_TAGS_FILTER_HELP: _("Filter Assets by the selected tags"),
    K.ASSET_FILTERS_CSV_TAGS_OR_HELP: _("Comma separated list of exact tags present on Asset (uses OR for multiple values)"),
    K.ASSET_FILTERS_CSV_TAGS_AND_HELP: _("Comma separated list of exact tags to match with an AND expression present on Asset"),
    K.ASSET_FILTERS_CSV_TAGS_NOT_HELP: _("Comma separated list of exact tags not present on Asset"),
    K.ASSET_FILTERS_CSV_LIFECYCLES_HELP: _("Comma separated list of exact Asset lifecycles"),
    K.ASSET_FILTERS_TAGS_ASSET_LABEL: _("Asset Tags"),
    K.ASSET_FILTERS_TAG_ASSET_LABEL: _("Asset Tag"),
    K.ASSET_FILTERS_TAG_ASSET_HELP: _("Search for tags on an Asset that are an exact match"),
    K.ASSET_FILTERS_NOT_TAGS_ASSET_LABEL: _("Not Asset Tags"),
    K.ASSET_FILTERS_WITHOUT_TAGS_LABEL: _("Asset without tags"),
    K.ASSET_FILTERS_TAG_ASSET_CONTAINS_LABEL: _("Asset Tag Contains"),
    K.ASSET_FILTERS_TAG_ASSET_CONTAINS_HELP: _("Search for tags on an Asset that contain a given pattern"),
    K.ASSET_FILTERS_TAG_NOT_CONTAIN_LABEL: _("Asset Tag Does Not Contain"),
    K.ASSET_FILTERS_TAG_NOT_CONTAIN_HELP: _("Search for tags on an Asset that contain a given pattern, and exclude them"),
    K.ASSET_FILTERS_TAG_NOT_LABEL: _("Not Asset Tag"),
    K.ASSET_FILTERS_TAG_NOT_HELP: _("Search for tags on an Asset that are an exact match, and exclude them"),
    K.ASSET_USERS_ACCESS_LABEL: _("Assets this User can access"),
    K.ASSET_USERS_NO_ACCESS_MESSAGE: _("This User is not assigned to any Assets."),
    K.ASSET_USERS_ADD_LABEL: _("Add Assets"),
    K.ASSET_USERS_USERS_ADD_LABEL: _("Add Users"),
    K.ASSET_USERS_MEMBER_LABEL: _("Asset Member"),
    K.ASSET_USERS_MEMBER_ADD_LABEL: _("Add Asset Member"),
    K.ASSET_USERS_MEMBER_ADD_SUCCESS_MESSAGE: _("Asset members added successfully."),
    K.ASSET_USERS_MEMBER_UPDATE_LABEL: _("Edit Asset Member"),
    K.ASSET_USERS_MEMBER_UPDATE_SUCCESS_MESSAGE: _("Asset member updated successfully."),
    K.ASSET_USERS_MEMBER_DELETE_LABEL: _("Delete Asset Member"),
    K.ASSET_USERS_MEMBER_DELETE_SUCCESS_MESSAGE: _("Asset member deleted successfully."),
    K.ASSET_GROUPS_ACCESS_LABEL: _("Assets this Group can access"),
    K.ASSET_GROUPS_NO_ACCESS_MESSAGE: _("This Group cannot access any Assets."),
    K.ASSET_GROUPS_MEMBER_LABEL: _("Asset Group"),
    K.ASSET_GROUPS_ADD_LABEL: _("Add Asset Group"),
    K.ASSET_GROUPS_ADD_SUCCESS_MESSAGE: _("Asset Groups added successfully."),
    K.ASSET_GROUPS_UPDATE_LABEL: _("Edit Asset Group"),
    K.ASSET_GROUPS_UPDATE_SUCCESS_MESSAGE: _("Asset Group updated successfully."),
    K.ASSET_GROUPS_DELETE_LABEL: _("Delete Asset Group"),
    K.ASSET_GROUPS_DELETE_SUCCESS_MESSAGE: _("Asset Group deleted successfully."),
    K.ASSET_GROUPS_ADD_ASSETS_LABEL: _("Add Assets"),
    K.ASSET_GROUPS_NUM_ASSETS_LABEL: _("Number of Assets"),
}


class LabelsManager(K):
    def __init__(self, labels):
        for _l, _v in K.__dict__.items():
            if not _l.startswith("__"):
                setattr(self, _l, labels[_v])


def should_use_v3_migration():
    return System_Settings.objects.get().enable_v3_migration


def get_labels() -> K:
    if should_use_v3_migration():
        return LabelsManager(V3_LABELS)
    return LabelsManager(V2_LABELS)
