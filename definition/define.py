"""

"""

import os
import mmap
import struct

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

    ### 0 frame buffer mapping ###
    fd_frbuf = open("/dev/fb0", 'wb+')

    fd_frbuf_val = struct.unpack('i', fd_frbuf.read(4))[0]
    print(fd_frbuf_val)

    if fd_frbuf_val < 1:
        print("invalid fb0 device file \n")

    # mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
    ptr_frbuf = mmap.mmap(fileno=fd_frbuf.fileno(), length=all_disp_address,access=mmap.MAP_SHARED, prot=mmap.PROT_READ|mmap.PROT_WRITE,  offset=0)
    print("fb0 has allocated memory address {:#08x}".format(ptr_frbuf))

    # ### 1 frame buffer mapping ###
    # fd_frbuf_2 = open("/dev/fb1", 'wb+')
    #
    # fd_frbuf_2_val = struct.unpack('i', fd_frbuf_2.read(4))[0]
    # print(fd_frbuf_2_val)
    #
    # if fd_frbuf_2_val < 1:
    #     print("invalid fb0 device file \n")
    #
    # # mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
    # ptr_frbuf_2 = mmap.mmap(fileno=fd_frbuf.fileno(), length=all_disp_address,access=mmap.MAP_SHARED, prot=mmap.PROT_READ|mmap.PROT_WRITE,  offset=0)
    # print("fb0 has allocated memory address {:#08x}".format(ptr_frbuf))





    fd_frbuf.close()




platform_init()
