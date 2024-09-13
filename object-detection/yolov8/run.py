from ultralytics import YOLO
# Double check the paths when running on rangpour

def train_yolov8():
    # Initialize the YOLO model
    model = YOLO('yolov8n.pt')  # Choose 'yolov8n.pt', 'yolov8s.pt', etc. depending on your needs

    # Train the model
    model.train(
        data='data.yaml',  # Path to the dataset config file
        epochs=100,               # Number of epochs to train
        name='fish_yolov8_model'  # Name for this training session
    )

if __name__ == "__main__":
    train_yolov8()
