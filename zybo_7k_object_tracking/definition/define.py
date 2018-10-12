"""

"""
import sys

import mmap
import ctypes

VDMA_MAP_SIZE = 0x100  # UIO - VDMA
VDMA_ADDR = 0x43C00000
VDMA_ADDR_2 = 0x43c40000
VDMA_BYPASS = (0x43c40000 + (0x1000 * 4))
VDMA_INSERT = (0x43c40000 + (0x2000 * 4))
FRBUF_ADDR_0 = 0x1E000000
FRBUF_ADDR_1 = 0x1E280000
FRBUF_ADDR_2 = 0x1E500000
FRBUF_ADDR_3 = 0x1E780000
PIXEL_NUM_OF_BYTES = 2
HORIZONTAL_PIXELS = 1280
VERTICAL_LINES = 1024
HORIZ_PIXELS_SMALL = 640
VERT_LINES_SMALL = 480
N_BUFFERS = 2


## platform_init #######################################################################################################
def platform_init():

    all_disp_address = HORIZONTAL_PIXELS * VERTICAL_LINES * PIXEL_NUM_OF_BYTES
    all_disp_small = HORIZ_PIXELS_SMALL * VERT_LINES_SMALL * PIXEL_NUM_OF_BYTES


    def file_mmap(file_path, mode = "rb+"):
        # try:
        with open(file_path, mode) as fd_frbuf:
             print(fd_frbuf.fileno())
             # mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

             ptr_frbuf = mmap.mmap(fileno=fd_frbuf.fileno(), length=all_disp_address, access=mmap.ACCESS_WRITE, offset=0)
             print(file_path, "has allocated memory address :", ptr_frbuf)
             for cont in range(0, all_disp_address):
                 ptr_frbuf[cont] = '0'

             print(ptr_frbuf.readline())

             ptr_frbuf.close()
             # buf = 'kjasifdubasd'
             #
             #
             # n = id(ptr_frbuf) * 0xFFFFFFFFFFFFFFFF
             # signed = ctypes.c_long(n).value
             # print("-------",(hex(signed)),"-------")
             # print(type(ptr_frbuf))
             #
             #
             # ctypes.memset(hex(signed), 0,all_disp_address)






        # except Exception as error:
        #     print("{}".format(error))

        return fd_frbuf

    fb0_path = "/dev/fb0"
    fd_frbuf_0 = file_mmap(fb0_path)


platform_init()
