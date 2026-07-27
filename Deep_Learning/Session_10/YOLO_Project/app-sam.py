from ultralytics import FastSAM

# Define an inference source
source = r"Deep_Learning/Session_10/YOLO_Project/bus.jpg"

# Create a FastSAM model
model = FastSAM("FastSAM-s.pt")  # or FastSAM-x.pt

# Run inference on an image
everything_results = model(source, device="cpu", retina_masks=True, imgsz=1024, conf=0.4, iou=0.9)

# Run inference with bboxes prompt
results = model(source, bboxes=[439, 437, 524, 709])

# Run inference with points prompt
results = model(source, points=[[200, 200]], labels=[1])

# Run inference with texts prompt
results = model(source, texts="a photo of a dog")

# Run inference with bboxes and points and texts prompt at the same time
results = model(source, bboxes=[439, 437, 524, 709], points=[[200, 200]], labels=[1], texts="a photo of a dog")