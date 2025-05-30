from ultralytics import YOLO
models = [
"yolo11n.pt", "yolo11s.pt", "yolo11m.pt", "yolo11l.pt", "yolo11x.pt",
"yolo12n.pt", "yolo12s.pt", "yolo12m.pt", "yolo12l.pt", "yolo12x.pt"
]
# 各モデルを順次処理
for model_name in models:
    print(f"処理中: {model_name}")
    model = YOLO(model_name)
    model.info()
    model.export(format="onnx", opset=17, simplify=True, 
                 nms=False, dynamic=False)
