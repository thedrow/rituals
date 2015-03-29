# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation, no-self-use
""" Provider for unknown SCM systems.
"""
# Copyright ⓒ  2015 Jürgen Hermann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# The full LICENSE file and source are available at
#    https://github.com/jhermann/rituals
from __future__ import absolute_import, unicode_literals, print_function

from .. import notify
from .base import ProviderBase


class NullProvider(ProviderBase):
    """ Stub provider for unknown SCM systems.

        This implements the provider interface, mostly emitting warnings.
    """
    key = 'unknown'


    def workdir_is_clean(self, quiet=False):
        """Check for uncommitted changes, return `True` if everything is clean."""
        if not quiet:
            notify.warning('Unsupported SCM: Cannot check for uncommitted changes,'
                           ' assuming you did it!')

        return True


    def add_file(self, filename):
        """Stage a file for committing, or commit it directly (depending on the SCM)."""
        notify.warning('Unsupported SCM: Please commit the file "{}"'.format(filename))


    def commit(self, message):
        """Commit pending changes."""
        notify.warning('Unsupported SCM: Make sure you commit pending changes for "{}"!'.format(message))


    def tag(self, label):
        """Tag the current workdir state."""
        notify.warning('Unsupported SCM: Make sure you apply the "{}" tag after commit!'.format(label))
