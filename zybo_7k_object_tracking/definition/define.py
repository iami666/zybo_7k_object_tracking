"""
This script contains
 - constants regarding memrory addresses and display pixels info
 - memory mapping of all the framebuffer and VDMA registers
 - wabcam check

"""
import sys
import mmap
import ctypes
import struct
import collections
import logging

log = logging.getLogger("__main__." + __name__)

# -----------------------------------------------
# registers addresses
VDMA_ADDR = 0x43C00000
VDMA_ADDR_2 = 0x43c40000
VDMA_BYPASS = (0x43c40000 + (0x1000 * 4))
VDMA_INSERT = (0x43c40000 + (0x2000 * 4))
FRBUF_ADDR_0 = 0x1E000000
FRBUF_ADDR_1 = 0x1E280000
FRBUF_ADDR_2 = 0x1E500000
FRBUF_ADDR_3 = 0x1E780000

# -----------------------------------------------
# display pixels info
VDMA_MAP_SIZE = 0x100  # UIO - VDMA
PIXEL_NUM_OF_BYTES = 2
HORIZONTAL_PIXELS = 1280
VERTICAL_LINES = 1024
HORIZ_PIXELS_SMALL = 640
VERT_LINES_SMALL = 480
N_BUFFERS = 2

# -----------------------------------------------
ALL_DISP_ADDRESS = HORIZONTAL_PIXELS * VERTICAL_LINES * PIXEL_NUM_OF_BYTES
ALL_DISP_SMALL = HORIZ_PIXELS_SMALL * VERT_LINES_SMALL * PIXEL_NUM_OF_BYTES

VID_FRAME_SIZE = (HORIZ_PIXELS_SMALL, VERT_LINES_SMALL)
VID_FRAME_CENTER = (50 + HORIZ_PIXELS_SMALL) / 2


# ------------------------------------------------------------------------------
# """ platform_init """
# ------------------------------------------------------------------------------

def platform_init():
    """ This platform_init function will initialise framebuffer , VDMA register  and wabcam check  """

    """ file_mmap """
    global log

    def file_mmap(file_path, len, inval=0, mode="rb+"):
        """
        This file_mmap will check path is correct or not and then perform mmap and memset operations with
        given args.

        :param file_path: string file path (framebuffer)
        :param len: int length for addresses
        :param inval: int input values
        :param mode: string filemode

        :return: fd_frbuf : framebuffer object
                 frbuf    :  buffer array
        """
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
            ptr_frbuf = ctypes.c_char_p.from_buffer(frbuf)

            log.info(file_path + " has allocated memory address : " + hex(ctypes.addressof(ptr_frbuf)))

            ctypes.memset(ctypes.addressof(ptr_frbuf), inval, len)

        except Exception as error:
            log.error(error)
            sys.exit(-1)

        return fd_frbuf, frbuf

    #  frame buffer check
    log.info("framebuffer checking...")
    fb0_path = "/dev/fb0"
    fd_frbuf_1_obj, fd_frbuf_1 = file_mmap(fb0_path, len=ALL_DISP_ADDRESS, inval=50)

    fb1_path = "/dev/fb1"
    fd_frbuf_2_obj, fd_frbuf_2 = file_mmap(fb1_path, len=ALL_DISP_SMALL, inval=200)

    fb2_path = "/dev/fb2"
    fd_frbuf_3_obj, fd_frbuf_3 = file_mmap(fb2_path, len=ALL_DISP_SMALL)

    fb3_path = "/dev/fb3"
    fd_frbuf_4_obj, fd_frbuf_4 = file_mmap(fb3_path, len=ALL_DISP_SMALL)

    """ VDMA memory check """
    log.info("VDMA memory checking...")
    mode = "rb+"
    fd_vdm_path = "/dev/mem"

    try:
        # open uiox device for VDMA access
        fd_vdm = open(fd_vdm_path, mode)

        log.info(fd_vdm_path + " checked...")

    except Exception as error:
        log.error("{}".format(error))
        sys.exit(-1)

    """ mmap the VDMA device for VDM access """

    vdma_buf = mmap.mmap(fd_vdm.fileno(), VDMA_MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE,
                         offset=VDMA_ADDR)

    ptr_vdm = ctypes.c_uint.from_buffer(vdma_buf)

    log.info(fd_vdm_path + " has allocated virtual address : " + hex(ctypes.addressof(ptr_vdm)))

    vdma_buf[5 * 4:6 * 4] = struct.pack("I", FRBUF_ADDR_0)
    vdma_buf[7 * 4:8 * 4] = struct.pack("I", 2)  # use internal FIFOs to trigger transfer
    vdma_buf[8 * 4:9 * 4] = struct.pack("I", 20480)
    vdma_buf[6 * 4:7 * 4] = struct.pack("I", 0x10300)  # turn vesa master transfer on
    vdma_buf[0x0D * 4:0x0E * 4] = struct.pack("I", 200)  # no. FIFO threshold ..max.. 240

    log.info("VDMA configuration end...")

    """ 2nd VDMA config """

    vdma_buf_2 = mmap.mmap(fd_vdm.fileno(), VDMA_MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE,
                           offset=VDMA_ADDR_2)

    ptr_vdm_2 = ctypes.c_uint.from_buffer(vdma_buf_2)

    log.info("RTC has virtual address : " + hex(ctypes.addressof(ptr_vdm_2)))

    vdma_buf_2[5 * 4:6 * 4] = struct.pack("I", FRBUF_ADDR_1)
    vdma_buf_2[4 * 4:5 * 4] = struct.pack("I", FRBUF_ADDR_1)
    vdma_buf_2[7 * 4:8 * 4] = struct.pack("I", 2)  # use internal FIFOs to trigger transfer

    ring_buf_size = int((ALL_DISP_SMALL / 128) - 1)
    vdma_buf_2[8 * 4:9 * 4] = struct.pack("I", ring_buf_size)
    vdma_buf_2[6 * 4:7 * 4] = struct.pack("I", 0x00010300)  # enable read transfer, continuously mode
    log.info("RTC configuration end...")

    """ config VDMA bypass """

    vdma_buf_4 = mmap.mmap(fd_vdm.fileno(), VDMA_MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE,
                           offset=VDMA_BYPASS)

    ptr_vdm_4 = ctypes.c_uint.from_buffer(vdma_buf_4)

    log.info("VDMA_BYPASS has virtual address : " + hex(ctypes.addressof(ptr_vdm_4)))

    vdma_buf_4[0x0D * 4:0x0E * 4] = struct.pack("I", (1 << 30))  # DMA_RTC bypass

    log.info("DMA_RTC_BYPASS configuration end...")

    """ config for child window size """

    vdma_buf_3 = mmap.mmap(fd_vdm.fileno(), VDMA_MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE,
                           offset=VDMA_INSERT)

    ptr_vdm_3 = ctypes.c_uint.from_buffer(vdma_buf_3)

    log.info("RTC_small window allocated virtual address : " + hex(ctypes.addressof(ptr_vdm_3)))

    # small windows adjustment
    # # vdma_buf_3[6 * 4:7 * 4] = struct.pack("I", ((75 << 16) + (HORIZ_PIXELS_SMALL + 75)))
    # vdma_buf_3[6 * 4:7 * 4] = struct.pack("I", ((50 << 16) + (HORIZ_PIXELS_SMALL + 50)))
    # # vdma_buf_3[7 * 4:8 * 4] = struct.pack("I", ((150 << 16) + (VERT_LINES_SMALL + 150)))
    # vdma_buf_3[7 * 4:8 * 4] = struct.pack("I", ((50 << 16) + (VERT_LINES_SMALL + 50)))
    # vdma_buf_3[5 * 4:6 * 4] = struct.pack("I", 0x70B)

    log.info("RTC_small window configuration end...")

    """ USB CAM check """
    cam_path = "/dev/video0"
    try:
        with open(cam_path, 'r') as _:
            log.info("Camera checked...")

    except Exception as error:
        log.error(error)
        # sys.exit(-1)

    # creating  namedtupled to return mupltiple arguments
    # frame_buffers = collections.namedtuple("frame_buffers", ["fd_frbuf_1", "fd_frbuf_2", "fd_frbuf_3", "fd_frbuf_4"])
    # vdma_buffers = collections.namedtuple("vdma_buffers", ["vdma_buf", "vdma_buf_1", "vdma_buf_2", "vdma_buf_3"])

    # fram_bfs = frame_buffers(fd_frbuf_1, fd_frbuf_2, fd_frbuf_3, fd_frbuf_4)
    # vdma_bfs = vdma_buffers(vdma_buf, vdma_buf_2, vdma_buf_3, vdma_buf_4)

    # fd_frbuf_1_obj.close()
    # fd_frbuf_2_obj.close()
    # fd_frbuf_3_obj.close()
    # fd_frbuf_4_obj.close()

    # vdma_buf.close()
    log.info("platform_init ends")
    # return fram_bfs, vdma_bfs


# ----------------------------------------------------------------------------------------------------------------------
# """ main """
# ----------------------------------------------------------------------------------------------------------------------


def main():
    """
        This function is used for testing the functionalists of the class and functions
    """
    platform_init()


if __name__ == "__main__":
    main()
