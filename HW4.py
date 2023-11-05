import datasets

dataset = datasets.load_dataset("conll2003")

train_data = dataset['train']
valid_data = dataset['validation']
test_data = dataset['test']