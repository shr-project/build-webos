#!/bin/bash

SCRIPTDIR=/OE/lge/layers/scripts

BASE="origin/master"
BRANCHES="\
  ose-master \
  scarthgap \
  styhead \
  walnascar \
  whinlatter \
  master \
"
${SCRIPTDIR}/rebase-multiple.sh ${BASE} "${BRANCHES}" $1

BASE="scarthgap"
BRANCHES="\
  scarthgap \
  jansa/scarthgap \
  jansa/styhead \
  jansa/walnascar \
  jansa/whinlatter \
  jansa/master \
"
${SCRIPTDIR}/rebase-multiple.sh ${BASE} "${BRANCHES}" skip_ru

BASE="jansa/scarthgap"
BRANCHES="\
  jansa/scarthgap \
  jansa/nodistro-scarthgap \
  jansa/nodistro-styhead \
  jansa/nodistro-walnascar \
  jansa/nodistro-whinlatter \
  jansa/nodistro-master \
"
${SCRIPTDIR}/rebase-multiple.sh ${BASE} "${BRANCHES}" skip_ru
