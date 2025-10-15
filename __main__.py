import torch
import torch.nn as nn
import functions_framework
from flask import Request, jsonify

# The @functions_framework.http decorator registers this function as an HTTP trigger.
@functions_framework.http
def run_pytorch_model(request: Request):
    """
    HTTP Cloud Function that initializes a model, runs inference, and returns the result.
    """
    print("--- Cloud Function Execution Start ---")

    # Define model parameters
    in_features = 10
    out_features = 5

    # Instantiate the model
    model = nn.Linear(in_features, out_features)
    print(f"Model initialized: {model}")

    # Create a dummy input tensor
    input_tensor = torch.randn(1, in_features)
    print(f"Generated random input tensor with shape: {input_tensor.shape}")

    # Set the model to evaluation mode
    model.eval()

    # Perform inference
    with torch.no_grad():
        output = model(input_tensor)

    print(f"Model produced output tensor with shape: {output.shape}")
    print(f"Output tensor:\n{output}")
    print("--- Cloud Function Execution Complete ---")

    # Return a JSON response to the caller
    return jsonify({
        "status": "success",
        "output_shape": list(output.shape),
        "output_data": output.tolist()
    })