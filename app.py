import io
from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    # Get form data
    origin = request.form.get("origin")
    bean_name = request.form.get("bean_name")
    bean_english_name = request.form.get("bean_english_name")
    processing = request.form.get("processing")
    roast_level = request.form.get("roast_level")
    flavor = request.form.get("flavor")
    roasting_date = request.form.get("roasting_date")

    action = request.args.get("action", "download")

    # Load assets
    template_img = Image.open("static/template.png")
    origin_img = Image.open(f"static/images/origins/{origin}.png")

    # Resize origin image to fixed height (approx 500px) while maintaining aspect ratio
    desired_origin_height = 250
    original_width, original_height = origin_img.size
    aspect_ratio = original_width / original_height
    new_origin_width = int(desired_origin_height * aspect_ratio)
    origin_img = origin_img.resize(
        (new_origin_width, desired_origin_height), Image.LANCZOS
    )

    # --- FONT LOADING ---
    try:
        font_size100 = ImageFont.truetype("static/fonts/SourceHanSerifTW-Bold.otf", 100)
        font_size80 = ImageFont.truetype("static/fonts/SourceHanSerifTW-Bold.otf", 80)
        font_size70 = ImageFont.truetype("static/fonts/SourceHanSerifTW-Bold.otf", 70)
        font_size60 = ImageFont.truetype("static/fonts/SourceHanSerifTW-Bold.otf", 60)
        font_size50 = ImageFont.truetype("static/fonts/SourceHanSerifTW-Bold.otf", 50)
        font_size40 = ImageFont.truetype("static/fonts/SourceHanSerifTW-Bold.otf", 40)
        font_size30 = ImageFont.truetype("static/fonts/SourceHanSerifTW-Bold.otf", 30)
    except IOError:
        print("Font not found, using default.")
        font_size100 = ImageFont.load_default()
        font_size80 = ImageFont.load_default()
        font_size70 = ImageFont.load_default()
        font_size60 = ImageFont.load_default()
        font_size50 = ImageFont.load_default()
        font_size40 = ImageFont.load_default()
        font_size30 = ImageFont.load_default()

    # Create a drawing context
    draw = ImageDraw.Draw(template_img)

    # Get image width for horizontal centering
    image_width = template_img.width

    # --- DRAW TEXT ---
    # Chinese Origin Name (larger)
    draw.text(
        (image_width / 2, 100),
        origin,
        font=font_size60,
        fill="#333333",
        anchor="mm",
    )
    # Bean Name (Chinese)
    draw.text(
        (image_width / 2, 210),
        bean_name,
        font=font_size100,
        fill="#333333",
        anchor="mm",
    )
    # Bean Name (English)
    draw.text(
        (image_width / 2, 320),
        bean_english_name,
        font=font_size40,
        fill="#555555",
        anchor="mm",
    )
    # Processing
    draw.text(
        (image_width / 2, 440),
        processing,
        font=font_size50,
        fill="#444444",
        anchor="mm",
    )
    # Roast Level
    draw.text(
        (image_width / 2, 560),
        roast_level,
        font=font_size50,
        fill="#666666",
        anchor="mm",
    )
    # Flavor Notes
    draw.text(
        (image_width / 2, 640), flavor, font=font_size40, fill="#444444", anchor="mm"
    )

    # Paste origin map
    origin_map_x = (template_img.width - origin_img.width) / 2
    origin_map_y = 700  # Fixed Y-coordinate for the origin map
    template_img.paste(origin_img, (int(origin_map_x), origin_map_y), origin_img)

    # If roasting date is provided, draw it below the origin map
    if roasting_date:
        roasting_date_y = 1080
        draw.text(
            (image_width / 2, roasting_date_y),
            f"{roasting_date}",
            font=font_size40,
            fill="#999999",
            anchor="mm",
        )

    # Save and send the image
    img_io = io.BytesIO()

    if action == "download_rotated":
        template_img = template_img.rotate(90, expand=True)

    template_img.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(
        img_io,
        mimetype="image/png",
        as_attachment=(action == "download"),
        download_name=f"{bean_name}.png",
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
