#!/bin/bash

SCRIPTDIR=/OE/lge/layers/scripts

BASE="origin/master"
BRANCHES="\
  ose-master \
  kirkstone \
  langdale \
  mickledore \
  nanbield \
  scarthgap \
  styhead \
  walnascar \
"
${SCRIPTDIR}/rebase-multiple.sh ${BASE} "${BRANCHES}" $1

BASE="kirkstone"
BRANCHES="\
  kirkstone \
  jansa/kirkstone \
  jansa/langdale \
  jansa/mickledore \
  jansa/nanbield \
  jansa/scarthgap \
  jansa/styhead \
  jansa/walnascar \
"
${SCRIPTDIR}/rebase-multiple.sh ${BASE} "${BRANCHES}" skip_ru

BASE="jansa/kirkstone"
BRANCHES="\
  jansa/kirkstone \
  jansa/nodistro-kirkstone \
  jansa/nodistro-langdale \
  jansa/nodistro-mickledore \
  jansa/nodistro-nanbield \
  jansa/nodistro-scarthgap \
  jansa/nodistro-styhead \
  jansa/nodistro-walnascar \
"
${SCRIPTDIR}/rebase-multiple.sh ${BASE} "${BRANCHES}" skip_ru
