from torchvision.datasets import VisionDataset
from PIL import Image
import os
import os.path
from pyvww.utils import VisualWakeWords


class VisualWakeWordsClassification(VisionDataset):
    """`Visual Wake Words <https://arxiv.org/abs/1906.05721>`_ Dataset.
    Args:
        root (string): Root directory where COCO images are downloaded to.
        annFile (string): Path to json visual wake words annotation file.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.ToTensor``
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.
    """
    def __init__(self, root, annFile, transform=None, target_transform=None, transforms=None):
        super(VisualWakeWordsClassification, self).__init__(root, transforms, transform, target_transform)
        self.vww = VisualWakeWords(annFile)
        self.ids = list(sorted(self.vww.imgs.keys()))

    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            tuple: Tuple (image, target). target is the index of the target class.
        """
        vww = self.vww
        img_id = self.ids[index]
        ann_ids = vww.getAnnIds(imgIds=img_id)
        if ann_ids:
            target = vww.loadAnns(ann_ids)[0]['category_id']
        else:
            target = 0

        path = vww.loadImgs(img_id)[0]['file_name']

        img = Image.open(os.path.join(self.root, path)).convert('RGB')
        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        return len(self.ids)
