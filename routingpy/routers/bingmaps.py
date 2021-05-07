# -*- coding: utf-8 -*-
# Copyright (C) 2021 GIS OPS UG
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#

from .base import Router, DEFAULT
from routingpy import convert
from routingpy import utils
from routingpy.direction import Direction, Directions
from routingpy.isochrone import Isochrone, Isochrones
from routingpy.matrix import Matrix


class BingMaps(Router):
    """Performs requests to the Bing Maps API services."""

    _DEFAULT_BASE_URL = "https://graphhopper.com/api/1"
