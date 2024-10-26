from flask import Flask, request, jsonify
import io
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/process_images', methods=['GET'])
def process_images():
    print("call recieved")
    
    try:
        # Extract data from the request
        #img = request.files['image'].read()
        #depth = request.files['depth'].read()
        #conf = request.files['confidence'].read()

        #float_array = [float(x) for x in request.form.getlist('intrinsics')]
        #bool_flag = request.form.get('flags').lower() == 'true'

        # Convert byte images to PIL Images
        #image1 = Image.open(io.BytesIO(img))
        #image2 = Image.open(io.BytesIO(depth))

        # Perform operations on images (example: blend images)
        #blended_image = Image.blend(image1, image2, 0.5)

        # Prepare response
        response = {
            'status': 'success',
            'message': 'Images processed successfully'
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
@app.route('/')
def health_check():
    # Basic check: If this route responds, the app is running
    status = 'OK'
    response = {
        'status': status,
    }
    
    return jsonify(response), 200 if status == 'OK' else 500
if __name__ == '__main__':
    app.run(debug=True)
