# if you are putting your test script folders under {git project folder}/tests/, it will work fine.
# otherwise, you either add it to system path before you run or hard coded it in here.

INPUT_LIB_PATH = sys.argv[1]
sys.path.append(INPUT_LIB_PATH)

import os
import common
import basecase
import gdoc

import shutil
import browser
import time


class Case(basecase.SikuliInputLatencyCase):

    def run(self):
        # Disable Sikuli action and info log
        com = common.General()
        com.infolog_enable(0)

        ff = browser.Firefox()
        gd = gdoc.gDoc()
        ff.clickBar()
        ff.enterLink(self.INPUT_TEST_TARGET)
        gd.wait_for_loaded()

        setAutoWaitTimeout(10)
        sample2_fp = os.path.join(self.INPUT_IMG_SAMPLE_DIR_PATH, self.INPUT_IMG_OUTPUT_SAMPLE_1_NAME.replace('sample_1', 'sample_2'))

        sleep(2)
        capture_width = int(self.INPUT_RECORD_WIDTH)
        capture_height = int(self.INPUT_RECORD_HEIGHT)

        t1 = time.time()
        capimg2 = capture(0, 0, capture_width, capture_height)

        com.system_print('[log]  TYPE "a"')
        type('a')
        # In normal condition, a should appear within 100ms, but if lag happened, that could lead the show up after 100 ms, and that will cause the calculation of AIL much smaller than expected.
        sleep(0.1)

        t2 = time.time()
        com.updateJson({'t1': t1, 't2': t2}, self.INPUT_TIMESTAMP_FILE_PATH)
        shutil.move(capimg2, sample2_fp.replace(os.path.splitext(sample2_fp)[1], '.png'))


case = Case(sys.argv)
case.run()
