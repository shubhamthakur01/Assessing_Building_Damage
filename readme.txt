This is the latest version of Damage assessment web app.

Here are the latest changes.
1. app.py has been changed from flask-ngrok version to flask version.(commented out lines with _ngrok, seaborn)
app.run(host = "0.0.0.0", port = 80, debug = True)
2. cache removal has been added. pipeline.py is called.
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

3. pipeline1 is latest and uptodate. RGB to BGR is done
cv2.imwrite('static/masked_image.png', cv2.cvtColor(output, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_PNG_COMPRESSION, 9])

4. app.py calls pipeline.py(cuda version)
5. html templates are updated and old ones are removed. index.html and complete1.html. complete1.html loads pre event and masked image.
6. old css templates are removed. only 4 images exist in assets which are the only ones used.
7. weights folder contains only required weights. 
8. Post_image and the content written for pst event image has been changed to pre image.
9. Home button has been added to complete1.html


How to run on google colab

1. open google colab and navigate to the Web_App_Final folder.
2. app.py file in this folder is designed for simple flask and not flask ngrok. so move app.py file in this folder to zoo(or any other) floder and move app.py from Web App folder to this folder.
3. !pip install flask-ngrok
4. !pip install flask==0.12.2
5. !python app.py


