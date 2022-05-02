from flask import *
from flask_bootstrap import Bootstrap
from PIL import Image
from colorthief import ColorThief
import os

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    current_image = "static/assets/images/cycling_1.jpg"
    ct = ColorThief(current_image)
    palette = ct.get_palette(color_count=11)

    if request.method == 'POST':

        if request.files['file'].filename == '':
            flash('No file selected')
            return redirect(url_for('home', image=current_image, colors=palette))
        else:
            data = request.files['file']
            image = Image.open(data)
            image.save(current_image)

            num_colors = int(request.form['num_colors'])
            print(num_colors)
            ct = ColorThief(current_image)
            palette = ct.get_palette(color_count=num_colors)

    return render_template('index.html', image=current_image, colors=palette)


if __name__ == "__main__":
    app.run(debug=True)
