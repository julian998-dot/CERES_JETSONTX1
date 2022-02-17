import torch

BATCH_SIZE = 4 # increase / decrease according to GPU memeory
RESIZE_TO = 512 # resize the image for training and transforms
NUM_EPOCHS = 5 # number of epochs to train for

DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# training images and XML files directory
TRAIN_DIR = '..\\plant_diseasedt\\train\\'
# validation images and XML files directory
VALID_DIR = '..\\plant_diseasedt\\test\\'

# classes: 0 index is reserved for background
CLASSES = [
    'background', 'sano', 'tizon_tardio', 'tizon_temprano'
]
NUM_CLASSES = 4

# whether to visualize images after crearing the data loaders
VISUALIZE_TRANSFORMED_IMAGES = False

# location to save model and plots
OUT_DIR = '../outputs'
SAVE_PLOTS_EPOCH = 2 # save loss plots after these many epochs
SAVE_MODEL_EPOCH = 2 # save model after these many epochs