OBJS=bplay.o
BIN=bplay
LDFLAGS+=-L/opt/vc/lib/ -lopenmaxil -lbcm_host -lvcos -lvchiq_arm -lpthread
LDFLAGS+= -I/opt/vc/include -I/opt/vc/include/interface/vcos/pthreads
LDFLAGS+= -I/opt/vc/include/interface/vmcs_host -I./ -I/opt/vc/include/interface/vcos
LDFLAGS+= -I/opt/vc/include/interface/vmcs_host/linux -I/opt/vc/include/interface/vchiq_arm

all: bplay
