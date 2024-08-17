import torch
import lightning.pytorch as pl
from lightning.pytorch import LightningModule, LightningDataModule
from lightning.pytorch.loggers import TensorBoardLogger
from torch.utils.data import DataLoader, TensorDataset
import torch.nn.functional as F


class CombDataModule(LightningDataModule):
    def __init__(self, X_train, y_train, X_test, y_test, batch_size=32):
        super().__init__()
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.batch_size = batch_size

    def setup(self, stage=None):
        # Convert to tensors
        self.train_dataset = TensorDataset(torch.from_numpy(self.X_train).float(), torch.from_numpy(self.y_train).long())
        self.test_dataset = TensorDataset(torch.from_numpy(self.X_test).float(), torch.from_numpy(self.y_test).long())

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size, shuffle=False)

class OneHotDataModule(LightningDataModule):
    def __init__(self, X_train, y_train, X_test, y_test, num_tokens, batch_size=32):
        super().__init__()
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.num_tokens = num_tokens
        self.batch_size = batch_size

    def setup(self, stage=None):
        # Convert to tensors
        X_train_one_hot = torch.stack( [  F.one_hot( torch.tensor(x).long(), num_classes = self.num_tokens ).float().flatten() for x in self.X_train ])
        X_test_one_hot = torch.stack( [  F.one_hot( torch.tensor(x).long(), num_classes = self.num_tokens ).float().flatten() for x in self.X_test])

        self.train_dataset = TensorDataset(X_train_one_hot, torch.from_numpy(self.y_train).long())
        self.test_dataset = TensorDataset(X_test_one_hot, torch.from_numpy(self.y_test).long())

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle = True)

    def val_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size, shuffle = False)

