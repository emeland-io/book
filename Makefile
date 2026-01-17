

.PHONY: run-server

run-server:
	hugo server -D --bind 172.29.94.79 --baseURL http://172.29.94.79:1313/book/


fetch-submodules:
	git submodule update --init --recursive

update-submodules:
	git submodule update --remote --merge