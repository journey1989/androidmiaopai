from base.config import REPORT_PATH,TEST_PATH
import pytest,os,json


if __name__ == '__main__':

    # pytest.main(["-v", "-s", "%sAMP_teenagermode.py" % TEST_PATH, "--alluredir=%s" % REPORT_PATH])

    for i in os.listdir(TEST_PATH):
        if i.startswith('AMP') == True:
            pytest.main(["-v", "-s", f"%s{i}" % TEST_PATH, "--alluredir=%s" % REPORT_PATH])
