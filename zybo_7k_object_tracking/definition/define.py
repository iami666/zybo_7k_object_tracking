"""

"""
import sys

import mmap
import ctypes
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

    """ file_mmap """  ###############################################################################

    def file_mmap(file_path, len, inval=0, mode="rb+"):
        try:
            fd_frbuf = open(file_path, mode)
            # print(fd_frbuf.fileno())
            # mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
            frbuf = mmap.mmap(fd_frbuf.fileno(),
                              len,
                              mmap.MAP_SHARED,
                              mmap.PROT_READ | mmap.PROT_WRITE,
                              offset=0
                              )

            # convert frbuf object into buffer pointer
            # ptr_frbuf = ctypes.c_uint32.from_buffer(frbuf)
            ptr_frbuf = ctypes.c_char_p.from_buffer(frbuf)

            print("[INFO] " + file_path + " has allocated memory address : " + hex(ctypes.addressof(ptr_frbuf)))

            ctypes.memset(ctypes.addressof(ptr_frbuf), inval, len)

        except Exception as error:
            print("{}".format(error))
            sys.exit(-1)

        return fd_frbuf, ptr_frbuf

    #  frame buffer check
    mode = "rb+"
    fb0_path = "/dev/fb0"
    fd_frbuf_1_obj, fd_frbuf_1 = file_mmap(fb0_path, len=all_disp_address, inval=50)

    fb1_path = "/dev/fb1"
    fd_frbuf_2_obj, fd_frbuf_2 = file_mmap(fb1_path, len=all_disp_small, inval=200)


    fb2_path = "/dev/fb2"
    fd_frbuf_3_obj, fd_frbuf_3 = file_mmap(fb2_path, len=all_disp_small)

    fb3_path = "/dev/fb3"
    fd_frbuf_4_obj, fd_frbuf_4 = file_mmap(fb3_path, len=all_disp_small)

    """ vdm memory check """

    fd_vdm_path = "/dev/mem"

    try:
        fd_vdm = open(fd_vdm_path, mode)
        # print(fd_vdm.fileno())
        print("[INFO] " + fd_vdm_path + " checked")

    except Exception as error:
        print("{}".format(error))
        sys.exit(-1)

    """ mmap the VDMA device for VDM access """
    # mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
    vdma_buf = mmap.mmap(fd_vdm.fileno(), VDMA_MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ|mmap.PROT_WRITE,
                         offset=VDMA_ADDR)

    ptr_vdm = ctypes.c_uint.from_buffer(vdma_buf)

    print("[INFO] " + fd_vdm_path + " has allocated virtual address : " + hex(ctypes.addressof(ptr_vdm)))



    vdma_buf[5*4:6*4] = struct.pack("I", FRBUF_ADDR_0)
    vdma_buf[7 * 4:8 * 4] = struct.pack("I", 2)  # use internal fifos to trigger xfer
    vdma_buf[8 * 4:9 * 4] = struct.pack("I", 20480)
    vdma_buf[6 * 4:7 * 4] = struct.pack("I", 0x10300)  # turn vesa master xfer on
    vdma_buf[0x0D * 4:0x0E * 4] = struct.pack("I", 200)  # no. FIFO threshhol ..max.. 240
    # ptr_vdm_mm = memoryview(vdma_buf)
    #
    # ptr_vdm_mm[5*4:6*4] = struct.pack("I", FRBUF_ADDR_0)
    # ptr_vdm_mm[7 * 4:8 * 4] = struct.pack("I", 2)  # use internal fifos to trigger xfer
    # ptr_vdm_mm[8 * 4:9 * 4] = struct.pack("I", 20480)
    # ptr_vdm_mm[6 * 4:7 * 4] = struct.pack("I", 0x10300)  # turn vesa master xfer on
    # ptr_vdm_mm[0x0D * 4:0x0E * 4] = struct.pack("I", 200)  # no. FIFO threshhol ..max.. 240
    # ptr_vdm_mm[4 * 4:5 * 4] = struct.pack("I", FRBUF_ADDR_0)
    # ptr_vdm_mm[6 * 4:7 * 4] = struct.pack("I", 2)  # use internal fifos to trigger xfer
    # ptr_vdm_mm[7 * 4:8 * 4] = struct.pack("I", 20480)
    # ptr_vdm_mm[5 * 4:6 * 4] = struct.pack("I", 0x10300)  # turn vesa master xfer on
    # ptr_vdm_mm[0x0C * 4:0x0D * 4] = struct.pack("I", 200)  # no. FIFO threshhol ..max.. 240
    # print("[INFO] VDMA configuration end.....\n")

    """ 2nd VDMA config """
    vdma_buf_2 = mmap.mmap(fd_vdm.fileno(), VDMA_MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE,
                           offset=VDMA_ADDR_2)

    ptr_vdm_2 = ctypes.c_uint.from_buffer(vdma_buf_2)

    print("[INFO] RTC has virtual address : " + hex(ctypes.addressof(ptr_vdm_2)))

    vdma_buf_2[5 * 4:6 * 4] = struct.pack("I", FRBUF_ADDR_1)
    vdma_buf_2[4 * 4:5 * 4] = struct.pack("I", FRBUF_ADDR_1)  # use internal fifos to trigger xfer
    vdma_buf_2[7 * 4:8 * 4] = struct.pack("I", 2)

    ring_buf_size = int((all_disp_small / 128) - 1)
    vdma_buf_2[8 * 4:9 * 4] = struct.pack("I", ring_buf_size)  # turn vesa master xfer on
    vdma_buf_2[6 * 4:7 * 4] = struct.pack("I", 0x00010300)  # no. FIFO threshhol ..max.. 240
    print("[INFO] RTC configuration end.....\n")

    # ptr_vdm_mm_2 = memoryview(vdma_buf_2)
    #
    # ptr_vdm_mm_2[4 * 4:5 * 4] = struct.pack("I", FRBUF_ADDR_1)
    # ptr_vdm_mm_2[3 * 4:4 * 4] = struct.pack("I", FRBUF_ADDR_1)  # use internal fifos to trigger xfer
    # ptr_vdm_mm_2[6 * 4:7 * 4] = struct.pack("I", 2)
    # #
    # # ring_buf_size = int((all_disp_small / 128) - 1)
    # # ptr_vdm_mm_2[7 * 4:8 * 4] = struct.pack("I", ring_buf_size)  # turn vesa master xfer on
    # # ptr_vdm_mm_2[5 * 4:6 * 4] = struct.pack("I", 0x00010300)  # no. FIFO threshhol ..max.. 240
    # # print("[INFO] RTC configuration end.....\n")

    """ config VDMA bypass """


    vdma_buf_4 = mmap.mmap(fd_vdm.fileno(), VDMA_MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE,
                           offset=VDMA_BYPASS)

    ptr_vdm_4 = ctypes.c_uint.from_buffer(vdma_buf_4)

    print("[INFO] VDMA_BYPASS has virtual address : " + hex(ctypes.addressof(ptr_vdm_4)))

    vdma_buf_4[0x0D * 4:0x0E * 4] = struct.pack("I", (1 << 30))

    # ptr_vdm_mm_4 = memoryview(vdma_buf_4)
    #
    # ptr_vdm_mm_4[0x0D * 4:0x0E * 4] = struct.pack("I", (1 << 30))

    print("[INFO] DMA_RTC_BYPASS configuration end....\n")

    """ config for child window size """
    vdma_buf_3 = mmap.mmap(fd_vdm.fileno(), VDMA_MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ|mmap.PROT_WRITE, offset=VDMA_INSERT)

    ptr_vdm_3 = ctypes.c_uint.from_buffer(vdma_buf_3)

    print("[INFO] RTC_small window allocated virtual address : " + hex(ctypes.addressof(ptr_vdm_3)))
    vdma_buf_3[6 * 4:7 * 4] = struct.pack("I", ((75 << 16) + (HORIZ_PIXELS_SMALL + 75)))
    vdma_buf_3[7 * 4:8 * 4] = struct.pack("I", ((150 << 16) + (VERT_LINES_SMALL + 150)))
    vdma_buf_3[5 * 4:6 * 4] = struct.pack("I", 0x70B)
    print("[INFO] RTC_small window configuration end....\n")


    # ptr_vdm_mm_3 = memoryview(vdma_buf_3)
    #
    # ptr_vdm_mm_3[5 * 4:6 * 4] = struct.pack("I", ((75 << 16) + (HORIZ_PIXELS_SMALL + 75)))
    # ptr_vdm_mm_3[6 * 4:7 * 4] = struct.pack("I", ((150 << 16) + (VERT_LINES_SMALL + 150)))
    # ptr_vdm_mm_3[4 * 4:5 * 4] = struct.pack("I", 0x70B)
    # print("[INFO] RTC_small window configuration end....\n")

    fd_frbuf_1_obj.close()
    fd_frbuf_2_obj.close()
    fd_frbuf_3_obj.close()
    fd_frbuf_4_obj.close()
# vdma_buf.close()

def main():
    platform_init()


if __name__ == "__main__":
    main()
