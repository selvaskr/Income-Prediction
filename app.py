from flask import Flask,render_template,request
import numpy as np
import pickle
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method== "POST":
        name=request.form["name"]
        age=request.form["Age"]
        fnwglt=request.form["Fnwglt"]
        years=request.form["Education_years"]
        martial_status=request.form["Marital_status"]
        occupation=request.form["Occupation"]
        relationship=request.form["Relationship"]
        sex=request.form["Sex"]
        hours=request.form["Hoursperweek"]
        gain=request.form['Gain']
        loss=request.form['Loss']
        mstatus={
            'Married'       :0,
            'Never-Married' :1,
            'Other'         :2
        }
        job={
            'Adm-clerical'      :0,
            'Armed-Forces'      :1,
            'Craft-repair'      :2,
            'Exec-managerial'   :3,
            'Farming-fishing'   :4,
            'Handlers-cleaners' :5,
            'Machine-op-inspct' :6,
            'Other-service'     :7,
            'Priv-house-serv'   :8,
            'Prof-specialty'    :9,
            'Protective-serv'   :10,
            'Sales'             :11,
            'Tech-support'      :12,
            'Transport-moving'  :13
        }

        relation={
            'Husband'        :0,
            'Not-in-family'  :1,
            'Other-relative' :2,
            'Own-child'      :3,
            'Unmarried'      :4,
            'Wife'           :5
        }
        gender={
            'Female':0,
            'Male'  :1
        }
        
        

        
        martial_status=mstatus[martial_status]
        occupation=job[occupation]
        relationship=relation[relationship]
        sex=gender[sex]
        
        model = pickle.load(open("income_pred.pkl","rb"))
        array = [[age,fnwglt,years,martial_status,occupation,relationship,sex,gain,loss,hours,]]
        print(array)
        array = [np.array(array[0],dtype = 'float64')]
        print(array)
        result=model.predict(array)
        if result==[0]:
            income=name+" makes Income of Below $50K/year"
        else:
            income=name+" makes Income of Above $50K/year"
        return render_template('index.html',n=income)

if __name__=='__main__':    
    app.run(debug=True)