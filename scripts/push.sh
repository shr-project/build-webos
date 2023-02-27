#!/bin/sh

export DATE=`date "+%Y-%m-%d"`
for B in kirkstone langdale mickledore nanbield scarthgap styhead master; do
    git tag -a -f -m "${B}-${DATE}" "${B}-${DATE}" ${B}
    git push -f shr ${B}-${DATE} ${B} jansa/${B} jansa/nodistro-${B}
done
