RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

GIT_VERSION = $(shell git name-rev --name-only --tags --no-undefined HEAD 2>/dev/null || echo git-`git rev-parse --short HEAD`)
SERVER_VERSION=$(shell awk '/Version:/ { print $$2; }' observatory-cloudwatcher-server.spec)

all:
	mkdir -p build
	cp cloudwatcherd cloudwatcherd.bak
	awk '{sub("SOFTWARE_VERSION = .*$$","SOFTWARE_VERSION = \"$(SERVER_VERSION) ($(GIT_VERSION))\""); print $0}' cloudwatcherd.bak > cloudwatcherd
	${RPMBUILD} -ba observatory-cloudwatcher-server.spec
	${RPMBUILD} -ba observatory-cloudwatcher-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-cloudwatcher.spec
	${RPMBUILD} -ba observatory-cloudwatcher-data.spec

	mv build/noarch/*.rpm .
	rm -rf build
	mv cloudwatcherd.bak cloudwatcherd

install:
	@python3 setup.py install
	@cp cloudwatcherd cloudwatcher /bin/
	@cp cloudwatcherd@.service /usr/lib/systemd/system/
	@cp completion/cloudwatcher /etc/bash_completion.d/
	@install -d /etc/cloudwatcherd
	@echo ""
	@echo "Installed server, client, and service files."
	@echo "Now copy the relevant json config files to /etc/cloudwatcherd/"
