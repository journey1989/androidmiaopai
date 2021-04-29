from base.config import REPORT_PATH,TEST_PATH
import pytest

if __name__ == '__main__':
    pytest.main(["-v", "-s", "%sAMP_my.py" % TEST_PATH, "--alluredir=%s" % REPORT_PATH])









