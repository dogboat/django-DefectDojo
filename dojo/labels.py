import abc
from abc import abstractmethod, abstractproperty
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


class PhraseSet:
    org = _("organization")
    org_plural = _("organization")


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

class LabelableThing(abc.ABC):
    @property
    @abstractmethod
    def Organization(self):
        pass

    @property
    @abstractmethod
    def Asset(self):
        pass


class V2Labels(LabelableThing):
    @property
    def Asset(self):
        return Label("product", msgctxt="term.v2.Asset")

    @property
    def Organization(self):
        return Label("product type", msgctxt="term.v2.Organization")


class V3Labels(LabelableThing):
    @property
    def Asset(self):
        return Label("asset", msgctxt="term.v3.Asset")

    @property
    def Organization(self):
        return Label("organization", msgctxt="term.v3.Organization")


mah_map = {
    System_Settings.LabelsVersions.V2: V2Labels(),
    System_Settings.LabelsVersions.V3: V3Labels(),
}


def get_labels_version():
    return System_Settings.objects.get().labels_version


def get_labels():
    labels_version = get_labels_version()
    return V3Labels() # mah_map.get(labels_version, V2Labels())

# labels.Organization.plural
