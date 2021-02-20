from torchvision.datasets import VisionDataset
from typing import Callable, Optional
from pathlib import Path
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


class Dataset(VisionDataset):
    def __init__(
            self,
            root: str,
            transforms: Optional[Callable] = None,
            transform: Optional[Callable] = None,
            target_transform: Optional[Callable] = None,
    ) -> None:
        super(Dataset, self).__init__(root, transforms, transform, target_transform)
        self.data = list(Path(self.root).glob("*/*"))

        self.label = {
            'busaiku': 0,
            'eraser': 1,
            'ikemen': 2,
            'pencil': 3,
            'room': 4,
            'smartphone': 5,
            'towl': 6}

        self.targets = [self.label[path.parent.stem] for path in self.data]

    def __getitem__(self, index: int):
        # img = (self.data[index])
        # return img

        img, target = self.data[index], int(self.targets[index])

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.open(img).convert('RGB')

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self) -> int:
        return len(self.data)


if __name__ == '__main__':
    dataset = Dataset("images")
    print(f"{len(dataset)=}")
    print(f"{dataset[0]=}")
    print(f"{dataset[1]=}")
