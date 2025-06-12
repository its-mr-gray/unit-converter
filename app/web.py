from flask import Flask, jsonify, render_template, request

from app.converters import convert_length, convert_temp, convert_weight

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(ValueError)
@app.errorhandler(TypeError)
def handle_bad_request(e):
    return jsonify({"error": str(e)}), 400


@app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "Not Found."}), 404


@app.route("/convert/temperature")
def convert_temp_route():
    val = request.args.get("val")
    from_unit = request.args.get("from_unit")
    to_unit = request.args.get("to_unit")

    if not all([val, from_unit, to_unit]):
        return render_template("temp.html", title="Temperature Converter")

    try:
        val = float(val)
        result = convert_temp(val=val, from_unit=from_unit, to_unit=to_unit)
        return jsonify({"result": result})
    except (ValueError, TypeError):
        raise
    except Exception:
        return jsonify({"error": "Internal Server Error."}), 500


@app.route("/convert/weight")
def convert_weight_route():
    val = request.args.get("val")
    from_unit = request.args.get("from_unit")
    to_unit = request.args.get("to_unit")

    if not all([val, from_unit, to_unit]):
        return render_template("weight.html", title="Weight Converter")

    try:
        val = float(val)
        result = convert_weight(val=val, from_unit=from_unit, to_unit=to_unit)
        return jsonify({"result": result})
    except (ValueError, TypeError):
        raise
    except Exception:
        return jsonify({"error": "Internal Server Error."}), 500


@app.route("/convert/length")
def convert_length_route():
    val = request.args.get("val")
    from_unit = request.args.get("from_unit")
    to_unit = request.args.get("to_unit")

    if not all([val, from_unit, to_unit]):
        return render_template("length.html", title="Length Converter")

    try:
        val = float(val)
        result = convert_length(val=val, from_unit=from_unit, to_unit=to_unit)
        return jsonify({"result": result})
    except (ValueError, TypeError):
        raise
    except Exception:
        return jsonify({"error": "Internal Server Error."}), 500
