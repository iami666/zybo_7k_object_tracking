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

    """ file_mmap """ ###############################################################################
    def file_mmap(file_path, mode="rb+"):
        try:
            with open(file_path, mode) as fd_frbuf:
                 # print(fd_frbuf.fileno())

                 # mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
                 frbuf = mmap.mmap(fd_frbuf.fileno(),
                                       all_disp_address,
                                       mmap.MAP_SHARED,
                                       mmap.PROT_READ|mmap.PROT_WRITE,
                                       0
                                       )
                 ptr_frbuf = ctypes.c_uint32.from_buffer(frbuf)
                 print("[INFO] " + file_path + " has allocated memory address : " +  hex(ctypes.addressof(ptr_frbuf)))

                 # cdef int cont
                 # for cont in range(0, all_disp_address):
                 #     ptr_frbuf[cont] = 0


        except Exception as error:
            print("{}".format(error))


        return ptr_frbuf

    # frame buffer check
    fb0_path = "/dev/fb0"
    fd_frbuf = file_mmap(fb0_path)

    fb1_path = "/dev/fb1"
    fd_frbuf_2 = file_mmap(fb1_path)

    fb2_path = "/dev/fb2"
    fd_frbuf_3 = file_mmap(fb2_path)

    fb3_path = "/dev/fb3"
    fd_frbuf_4 = file_mmap(fb3_path)

    # vdm memory check
    try:
        fd_vdm_path = "/dev/mem"
        mode = "rb+"
        with open(fd_vdm_path, mode) as fd_vdm:
            print("[INFO] " + fd_vdm_path + " checked")

    except Exception as error:
        print("{}".format(error))


def main():
    platform_init()


if __name__ == "__main__":
    main()
