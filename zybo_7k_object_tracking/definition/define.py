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
    def file_mmap(file_path, len, inval=0,  mode="rb+"):
        try:
            with open(file_path, mode) as fd_frbuf:
                 # print(fd_frbuf.fileno())

                 # mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
                 frbuf = mmap.mmap(fd_frbuf.fileno(),
                                   len,
                                   mmap.MAP_SHARED,
                                   mmap.PROT_READ|mmap.PROT_WRITE,
                                   0
                                   )

                 # convert frbuf object into buffer pointer
                 # ptr_frbuf = ctypes.c_uint32.from_buffer(frbuf)
                 ptr_frbuf = ctypes.c_char_p.from_buffer(frbuf)

                 print("[INFO] " + file_path + " has allocated memory address : " +  hex(ctypes.addressof(ptr_frbuf)))

                 ctypes.memset(ctypes.addressof(ptr_frbuf), inval, all_disp_address)

        except Exception as error:
            print("{}".format(error))


        return ptr_frbuf

    # frame buffer check
    fb0_path = "/dev/fb0"
    fd_frbuf = file_mmap(fb0_path, len=all_disp_address, inval=50)

    fb1_path = "/dev/fb1"
    fd_frbuf_2 = file_mmap(fb1_path, len=all_disp_small, inval=200)

    fb2_path = "/dev/fb2"
    fd_frbuf_3 = file_mmap(fb2_path, len=all_disp_small)

    fb3_path = "/dev/fb3"
    fd_frbuf_4 = file_mmap(fb3_path, len=all_disp_small)

    # vdm memory check
    try:
        fd_vdm_path = "/dev/mem"
        mode = "rb+"
        fd_vdm =  open(fd_vdm_path, mode)
        # print(fd_vdm.fileno())
        print("[INFO] " + fd_vdm_path + " checked")

    except Exception as error:
        print("{}".format(error))

    # mmap the VDMA device for VDM access
    #mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
    # vdma_buf = mmap.mmap(fd_vdm.fileno(), int(VDMA_MAP_SIZE), mmap.MAP_SHARED, mmap.PROT_READ|mmap.PROT_WRITE, hex(VDMA_ADDR))
    vdma_buf = mmap.mmap(fd_vdm.fileno(), int(VDMA_MAP_SIZE), mmap.MAP_SHARED, mmap.PROT_READ|mmap.PROT_WRITE, 0)
    # ptr_vdm = ctypes.c_uint32.from_buffer(vdma_buf)
    ptr_vdm = ctypes.c_uint.from_buffer(vdma_buf)
    print(type(ctypes.addressof(ptr_vdm)))
    print("[INFO] " + fd_vdm_path + " has allocated virtual address : " + hex(ctypes.addressof(ptr_vdm)))
    # print("[INFO] " + fd_vdm_path + " has allocated virtual address : " + hex(ctypes.addressof(ptr_vdma)))
    # fd_vdm.close()

    vdma_buf[0] = FRBUF_ADDR_0
    # ptr_vdm[5]= FRBUF_ADDR_0
    # ptr_vdm + 7 = 2
    # ptr_vdm + 8 = 20480
    # ptr_vdm + 6 = 0x10300
    # ptr_vdm + 0x0D = 200
    # print("[INFO] VDMA configuration end.....\n")
    

def main():
    platform_init()


if __name__ == "__main__":
    main()

