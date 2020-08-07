# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import collective.pat_daterangepicker


class CollectivePat_DaterangepickerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.pat_daterangepicker)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.pat_daterangepicker:default')


COLLECTIVE_PAT_DATERANGEPICKER_FIXTURE = CollectivePat_DaterangepickerLayer()


COLLECTIVE_PAT_DATERANGEPICKER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PAT_DATERANGEPICKER_FIXTURE,),
    name='CollectivePat_DaterangepickerLayer:IntegrationTesting',
)


COLLECTIVE_PAT_DATERANGEPICKER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PAT_DATERANGEPICKER_FIXTURE,),
    name='CollectivePat_DaterangepickerLayer:FunctionalTesting',
)


COLLECTIVE_PAT_DATERANGEPICKER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_PAT_DATERANGEPICKER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectivePat_DaterangepickerLayer:AcceptanceTesting',
)
