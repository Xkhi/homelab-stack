#! /bin/bash

for volume in $(docker volume ls -q); do
	docker run --rm --name backup -v $volume:/volume -v /home/jalvare/backup:/backup busybox:latest tar -cvzf /backup/$volume-$(date +%G%m%d).tar.gz /volume
done
