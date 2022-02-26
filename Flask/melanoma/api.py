import os
import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np

import albumentations as A
from albumentations.pytorch import ToTensorV2

from PIL import Image
import pretrainedmodels

from flask import Flask, render_template, request

app = Flask(__name__)
UPLOAD_FOLDER = "C:\\Users\\hong\\flask\\melanoma\\static"
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
MODEL = None


class SEResnext50_32x4d(nn.Module):
    def __init__(self, pretrained='imagenet'):
        super(SEResnext50_32x4d, self).__init__()
        self.base_model = pretrainedmodels.__dict__['se_resnext50_32x4d'](
            pretrained=pretrained)  # 마지막 fc layer output : 2048

        self.linear = nn.Linear(2048, 1)  # binary classification

    def forward(self, image):
        batch_size, _, _, _ = image.shape
        x = self.base_model.features(image)  # (1, 2048, 7, 7)
        x = F.adaptive_avg_pool2d(x, 1).reshape(batch_size, -1)  # (1, 2048, 1, 1) -> (1, 2048)
        out = torch.sigmoid(self.linear(x))  # (1, 1)
        return out


class Dataset(torch.utils.data.Dataset):
    def __init__(self, data_path, transform=None):
        self.data_path = data_path
        self.transform = transform

    def __len__(self):
        return 1

    def __getitem__(self, idx):
        image = np.array(Image.open(self.data_path))

        if self.transform is not None:
            image = self.transform(image=image)['image']

        return image


def predict(image_path, model):
    mean = (0.485, 0.456, 0.406)
    std = (0.229, 0.224, 0.225)
    aug = A.Compose(
        [
            A.Normalize(mean, std, max_pixel_value=255.0, always_apply=True),
            ToTensorV2(),
        ]
    )

    test_dataset = Dataset(image_path, transform=aug)

    test_loader = torch.utils.data.DataLoader(
        test_dataset, batch_size=1, shuffle=False, num_workers=0
    )

    model.eval()
    with torch.no_grad():
        for idx, inputs in enumerate(test_loader):
            inputs = inputs.to(DEVICE)
            outputs = model(inputs)

    return outputs.item()


@app.route('/', methods=['GET','POST'])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]  # html 에서 input태그 name으로 가져옴
        if image_file:  # 파일이 있다면
            image_location = os.path.join(  # 이미지 저장할 폴더
                UPLOAD_FOLDER,
                image_file.filename
            )
            image_file.save(image_location)  # 이미지 저장
            pred = predict(image_location, MODEL)

            return render_template('index.html', prediction=pred, image_loc=image_file.filename)
    return render_template('index.html', prediction=0, image_loc=None)


if __name__ == "__main__":
    MODEL = SEResnext50_32x4d(pretrained='imagenet')
    MODEL.load_state_dict(torch.load('ckpt.pt'))
    MODEL.to(DEVICE)
    app.run(port=8000, debug=True)