from flask import Flask, request, jsonify
import io
from PIL import Image
import numpy as np
import json

app = Flask(__name__)

@app.route('/process_images', methods=['POST'])
def process_images():
    print("call recieved")
    print(request.files)
    
    try:
        # Extract data from the request
        img = request.files['image'].read()
        print('here')
        depth = request.files['depth'].read()
        print('here2')
        conf = request.files['confidence'].read()
        print('here3')

        print(request.form['intrinsics'])
    

        intrinsics = json.load(request.form['intrinsics'])
        print('here4')

        isDepthAvailable = json.load(request.form['flags'])
        print('here5')

        print("intrinsics = "+intrinsics)

        print("depth flag = "+isDepthAvailable)

        # Convert byte images to PIL Images
        image1 = Image.open(io.BytesIO(img))
        print("input frame size = "+image1.size)
        image2 = Image.open(io.BytesIO(depth))
        print("depth frame size = "+image2.size)

        # Perform operations on images (example: blend images)
        blended_image = Image.blend(image1, image2, 0.5)

        # Convert blended image to numpy array
        img_array = np.array(blended_image)

        # Prepare response
        response = {
            'status': 'success',
            'message': 'Images processed successfully',
            'object_size': img_array.mean()

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
