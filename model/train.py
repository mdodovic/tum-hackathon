import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim

from model import PeopleNumberPredictionModel
from data_load import TrainDataset

if __name__ == "__main__":

    out_classes = 6
    net = PeopleNumberPredictionModel(out_classes)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    ############### Load data
    data = []
    targets = []
    ##############data = []
    targets = []

    trainloader = TrainDataset(data, targets)

    for epoch in range(2):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                    (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Finished Training')