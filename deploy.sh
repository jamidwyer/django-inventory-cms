#!/bin/bash
hostname=$(curl 159.65.177.10/metadata/v1/hostname)
docker run -d -p 8000:8000 --name hord-cms-"$hostname" jami/hord-cms:"$hostname"