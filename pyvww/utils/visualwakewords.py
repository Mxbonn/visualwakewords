import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from pycocotools.coco import COCO


class VisualWakeWords(COCO):
    def __init__(self, *args):
        super(VisualWakeWords, self).__init__(*args)

    def showAnns(self, anns):
        """
        Display the specified annotations.
        :param anns (array of object): annotations to display
        :return: None
        """
        if len(anns) == 0:
            return 0
        ax = plt.gca()
        ax.set_autoscale_on(False)
        for ann in anns:
            c = (np.random.random((1, 3)) * 0.6 + 0.4).tolist()[0]
            if ann['category_id'] == 1:
                [x, y, width, height] = ann['bbox']
                rect = patches.Rectangle((x, y), width, height, edgecolor=c, facecolor=c, linewidth=2, alpha=0.4)
                ax.add_patch(rect)

    def download(self, *args):
        raise AttributeError("Cannot download Visual Wake Words Dataset. "
                             "See instructions on github.com/Mxbonn/visualwakewords to create"
                             "the Visual Wake Words Dataset.")

    def loadRes(self, resFile):
        raise AttributeError("Method not implemented for the Visual Wake Words Dataset.")

    def annToRLE(self, ann):
        raise AttributeError("Method not implemented for the Visual Wake Words Dataset.")

    def annToMask(self, ann):
        raise AttributeError("Method not implemented for the Visual Wake Words Dataset.")

