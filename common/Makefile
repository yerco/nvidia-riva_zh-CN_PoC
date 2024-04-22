SRC_DIR=./riva/proto
DST_DIR=../myapp/riva_api

setup:
	@mkdir -p ${DST_DIR}
.PHONY: setup

# Requires python libraries grpcio and grpcio-tools
# 	pip3 install grpcio grpcio-tools
# linux use @sed -i -r 's/from riva.proto import (.+_pb2.*)/from . import \1/g' ${DST_DIR}/riva/proto/*_pb2*.py, line below is for mac
python: setup
	@echo "==> Generating python bindings"
	python3 -m grpc_tools.protoc --python_out=${DST_DIR} \
		--grpc_python_out=${DST_DIR} \
		-I. ${SRC_DIR}/*.proto
	# Move generated files to the desired directory and clean up
	@mkdir -p ${DST_DIR}
	@mv ${DST_DIR}/riva/proto/* ${DST_DIR}/
	@rm -rf ${DST_DIR}/riva
	sed -i '' -E 's/from riva\.proto import (.+_pb2.*)/from . import \1/g' ${DST_DIR}/*_pb2*.py
.PHONY: python

clean:
	rm -vI ${DST_DIR}/riva/proto/*.py ${DST_DIR}/riva/proto/*.go
.PHONY: clean
