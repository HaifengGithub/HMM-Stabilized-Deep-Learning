import torch
import torch.utils.data
import torchvision.models as models
from torch import nn
from torch.nn import Sequential, Linear, ReLU, Dropout

class swinnet(nn.Module):
    def __init__(self):
        super(swinnet, self).__init__()
        swinb_pretrained = models.swin_b(pretrained=True)
        self.feature = torch.nn.Sequential(*list(swinb_pretrained.children())[:-1])
        self.fc1 = Sequential(
            nn.Linear(1024, 1024, bias=True),
            nn.ReLU(),
            # nn.Dropout(0.5),
            nn.Linear(1024, 2, bias=True),
        )
        self.fc2 = Sequential(
            nn.Linear(1024, 1024, bias=True),
            nn.ReLU(),
            # nn.Dropout(0.5),
            nn.Linear(1024, 2, bias=True),
        )
        self.fc3 = Sequential(
            nn.Linear(1024, 1024, bias=True),
            nn.ReLU(),
            # nn.Dropout(0.5),
            nn.Linear(1024, 2, bias=True),
        )
        self.fc4 = Sequential(
            nn.Linear(1024, 1024, bias=True),
            nn.ReLU(),
            # nn.Dropout(0.5),
            nn.Linear(1024, 2, bias=True),
        )
        self.fc5 = Sequential(
            nn.Linear(1024, 1024, bias=True),
            nn.ReLU(),
            # nn.Dropout(0.5),
            nn.Linear(1024, 2, bias=True),
        )
        self.fc6 = Sequential(
            nn.Linear(1024, 1024, bias=True),
            nn.ReLU(),
            # nn.Dropout(0.5),
            nn.Linear(1024, 2, bias=True),
        )
        self.fc7 = Sequential(
            nn.Linear(1024, 1024, bias=True),
            nn.ReLU(),
            # nn.Dropout(0.5),
            nn.Linear(1024, 2, bias=True),
        )

    def forward(self, x):
        x = self.feature(x)
        x = x.reshape([-1,1024])
        x1 = self.fc1(x)
        x2 = self.fc2(x)
        x3 = self.fc3(x)
        x4 = self.fc4(x)
        x5 = self.fc5(x)
        x6 = self.fc6(x)
        x7 = self.fc7(x)
        return (x1, x2, x3, x4, x5, x6, x7)