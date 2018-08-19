#!/bin/bash

yum -y update
yum -y install readline-devel zlib-devel bzip2-devel sqlite-devel openssl-devel \
    libXext.x86_64 libSM.x86_64 libXrender.x86_64 gcc gcc-c++ libffi-devel python-devel
