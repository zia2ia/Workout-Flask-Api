from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.exc import IntegrityError

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workout.db'
db = SQLAlchemy(app)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String(20), nullable = False)
    weight = db.Column(db.Integer, nullable = True)
    reps = db.Column(db.Integer, nullable = True)

    __table_args__ = (
        CheckConstraint("(reps >= 1 AND reps <= 200) OR reps is NULL", name = "check_reps_range"),
        CheckConstraint("(weight >= 1 AND weight <= 1000) or weight is NULL", name = "check_weight_range"),
    )

@app.route("/")
def home():
    return jsonify({"message": "home page of workout tracker api"})


@app.route('/workout', methods = ["GET"])
def get_workouts():
    result = []
    workouts = Workout.query.all()
    if len(workouts) == 0:
        return jsonify({"message" : "database is empty"})
    for workout in workouts:
        data = {"id": workout.id, 
                "type": workout.type, 
                "name": workout.name, 
                "weight": workout.weight, 
                "reps": workout.reps}
        
        
        result.append(data)
    
    return jsonify({"workout": result})

@app.route("/workout/<int:id>", methods = ["GET"])
def get_workout_id(id):    
    workout = Workout.query.get_or_404(id)
    data = {"id": workout.id, 
                "type": workout.type, 
                "name": workout.name, 
                "weight": workout.weight, 
                "reps": workout.reps}

    return jsonify({"workout": data})

@app.route("/workout", methods = ["POST"])
def create_workout():
    if request.json.get("type") is None or request.json.get("name") is None or request.json.get("type") == "" or request.json.get("name") == "":
        return jsonify({"message" : "constraint violated : name or type are missing"}), 400
    if request.json.get("weight") is None or request.json.get("reps") is None:
        return jsonify({"message" : "constraint violated : weight or reps are missing"}), 400
    try:
        new_workout = Workout(type = request.json["type"], name = request.json["name"], 
                        weight = request.json["weight"], reps = request.json["reps"])
        db.session.add(new_workout)
        db.session.commit()
        return jsonify({"id": new_workout.id, 
                        "type": new_workout.type, 
                        "name": new_workout.name, 
                        "weight (lbs)": new_workout.weight, 
                        "reps": new_workout.reps}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message" : "constraint violeated : invalid rep or weight range"}), 400

@app.route("/workout/<id>", methods = ["DELETE"])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message" : "workout deletion successful"})


@app.route("/workout/<id>", methods = ["PUT"])
def update_workout(id):
    workout = Workout.query.get_or_404(id)

    data = request.json
    
    new_type = data.get("type")
    new_name = data.get("name")
    new_weight = data.get("weight")
    new_reps = data.get("reps")

    if new_type is not None:
        workout.type = new_type
    if new_name is not None:
        workout.name = new_name
    if new_weight is not None:
        workout.weight = new_weight
    if new_reps is not None:
        workout.reps = new_reps
    
    db.session.commit()
    return jsonify({"id": workout.id, 
                    "type": workout.type, 
                    "name": workout.name, 
                    "weight": workout.weight, 
                    "reps": workout.reps, 
                    "message": "workout update successful"
                    }), 201

if __name__ == "__main__":
    app.run(debug=True)
    
