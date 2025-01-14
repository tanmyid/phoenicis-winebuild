#!/usr/bin/env python

from core.Container import Container
from core.Environment import Environment
from builders.WineBuilder import WineBuilder

environment = Environment("wine_osxcross", "linux", "amd64")
environment.build()

container = Container(environment)
container.start()


builder = WineBuilder(container, [{
    "name": "appwiz-disable_mono_and_gecko_cx21",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
}, {
    "name": "winemac-allow_customization_bundle_name_cx",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
},{
    "name": "winemac-allow_customization_hide_icon_cx",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
}, {
    "name": "winemac-exit_app_with_cmd_q_cx21",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
}, {
    "name": "loader-shape3D-name_cx21",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
}, {
    "name": "winemenubuilder-disable-cxmenu_cx21",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
}, {
    "name": "shell32-disable-lnk",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
}, {
    "name": "advapi-report-real-username_cx21",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
}, {
    "name": "shell32-disable-recents-documents",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
}, {
    "name": "winemac-restore-spec",
    "operatingSystems": "darwin",
    "architectures": ["amd64"]
}])

builder.build("darwin", "amd64", "winecx-21.0.0", "cx", "https://github.com/PhoenicisOrg/winecx")
builder.archive("shape3D_wine_21_2.tar.gz")
