RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	date --utc +%Y%m%d%H%M%S > VERSION
	${RPMBUILD} --define "_version %(cat VERSION)" -ba rockit-cloudwatcher.spec
	${RPMBUILD} --define "_version %(cat VERSION)" -ba python3-rockit-cloudwatcher.spec

	mv build/noarch/*.rpm .
	rm -rf build VERSION

install:
	@python3 setup.py install
	@cp cloudwatcherd cloudwatcher /bin/
	@cp cloudwatcherd@.service /usr/lib/systemd/system/
	@cp completion/cloudwatcher /etc/bash_completion.d/
	@install -d /etc/cloudwatcherd
	@echo ""
	@echo "Installed server, client, and service files."
	@echo "Now copy the relevant json config files to /etc/cloudwatcherd/"
