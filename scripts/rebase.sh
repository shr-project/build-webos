#!/bin/bash

SCRIPTDIR=/OE/lge/layers/scripts

RELEASE="master"
BUILD="webos"

BUILD_BRANCH="jansa/nodistro-whinlatter"
BRANCH="jansa/${RELEASE}"
BASE_LAYERS=" \
  meta-webosose \
  meta-qt6 \
  meta-oe \
  meta-raspberrypi \
  meta-virtualization \
  meta-security \
  meta-clang \
  oe-core \
  bitbake \
"

${SCRIPTDIR}/update-layers.sh ${BRANCH} ${BUILD_BRANCH} "${BASE_LAYERS}" build-${BUILD}-${RELEASE}
