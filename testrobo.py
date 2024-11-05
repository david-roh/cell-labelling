import argparse
import inference

# Set up argument parser
parser = argparse.ArgumentParser(description="Run inference on an image.")
parser.add_argument("image_path", type=str, help="Path to the image file")

# Parse arguments
args = parser.parse_args()

# Run inference
model = inference.get_model("sem-2n8iq/3")
results = model.infer(image=args.image_path)
print(results)