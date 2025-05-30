import onnx

def extract_yolo11(input_file, output_file):
    output_names = [
        "/model.23/Concat_output_0",
        "/model.23/Concat_1_output_0", 
        "/model.23/Concat_2_output_0"
    ]
    onnx.utils.extract_model(input_file, output_file, 
                             ["images"], output_names)

def extract_yolo12(input_file, output_file):
    output_names = [
        "/model.21/Concat_output_0",
        "/model.21/Concat_1_output_0", 
        "/model.21/Concat_2_output_0"
    ]
    onnx.utils.extract_model(input_file, output_file, 
                            ["images"], output_names)

# YOLO11モデル処理
yolo11_models = ["yolo11n.onnx", "yolo11s.onnx", 
                "yolo11m.onnx", "yolo11l.onnx", "yolo11x.onnx"]

for model in yolo11_models:
    extract_yolo11(model, model.replace(".onnx", "-cut.onnx"))

# YOLO12モデル処理
yolo12_models = ["yolo12n.onnx", "yolo12s.onnx", 
                "yolo12m.onnx", "yolo12l.onnx", "yolo12x.onnx"]
for model in yolo12_models:
    extract_yolo12(model, model.replace(".onnx", "-cut.onnx"))
