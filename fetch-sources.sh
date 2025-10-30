#!/bin/bash

VERSION=9.1.1-ga
TARBALL_NAME=$VERSION.tar.gz
URL=https://github.com/openjdk/jmc/archive/refs/tags/$TARBALL_NAME

# if a jmc tarball already exists, remove it prior to downloading a new one
if [ -f $TARBALL_NAME ]; then
    rm $VERSION.tar.gz
fi

wget $URL
