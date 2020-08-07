# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.pat_daterangepicker.testing import COLLECTIVE_PAT_DATERANGEPICKER_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.pat_daterangepicker is properly installed."""

    layer = COLLECTIVE_PAT_DATERANGEPICKER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.pat_daterangepicker is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.pat_daterangepicker'))

    def test_browserlayer(self):
        """Test that ICollectivePatDaterangepickerLayer is registered."""
        from collective.pat_daterangepicker.interfaces import (
            ICollectivePatDaterangepickerLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectivePatDaterangepickerLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_PAT_DATERANGEPICKER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.pat_daterangepicker'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.pat_daterangepicker is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.pat_daterangepicker'))

    def test_browserlayer_removed(self):
        """Test that ICollectivePatDaterangepickerLayer is removed."""
        from collective.pat_daterangepicker.interfaces import \
            ICollectivePatDaterangepickerLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectivePatDaterangepickerLayer,
            utils.registered_layers())
