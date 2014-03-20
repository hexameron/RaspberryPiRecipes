OBJS=bplay.o
BIN=bplay
CFLAGS+=-DSTANDALONE -D__STDC_CONSTANT_MACROS -D__STDC_LIMIT_MACROS -DTARGET_POSIX -D_LINUX -fPIC -DPIC -D_REENTRANT -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -Wall -DHAVE_LIBOPENMAX=2 -DOMX -DOMX_SKIP64BIT -pipe -DUSE_EXTERNAL_OMX -DHAVE_LIBBCM_HOST -DUSE_EXTERNAL_LIBBCM_HOST -DUSE_VCHIQ_ARM
LDFLAGS+=-L/opt/vc/lib/ -lopenmaxil -lbcm_host -lvcos -lvchiq_arm -lpthread
LDFLAGS+= -I/opt/vc/include -I/opt/vc/include/interface/vcos/pthreads
LDFLAGS+= -I/opt/vc/include/interface/vmcs_host -I./ -I/opt/vc/include/interface/vcos
LDFLAGS+= -I/opt/vc/include/interface/vmcs_host/linux -I/opt/vc/include/interface/vchiq_arm

all: bplay
