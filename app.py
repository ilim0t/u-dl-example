import cv2
import torch
from torchvision import transforms
from model import Net
from PIL import Image


capture = cv2.VideoCapture(0)
use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")
model = Net().to(device)
model.load_state_dict(torch.load("cnn.pt"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

idx2label = {0: 'busaiku', 1: 'eraser', 2: 'ikemen', 3: 'pencil', 4: 'room', 5: 'smartphone', 6: 'towl'}

while(True):
    ret, frame = capture.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # frame = frame.transpose(2,0,1)
    img = Image.fromarray(img)
    img = transform(img).to(device)
    predict = model(img[None])
    label = idx2label[predict.argmax().item()]
    prob = predict[0, predict.argmax().item()]
    cv2.imshow('frame', frame)
    print(f"{label=},\t{prob=}")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
