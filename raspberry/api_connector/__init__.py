import sys

if __name__ != '__main__':
    sys.path.extend(sys.modules[__name__].__path__)

from face_rec_api import check_image