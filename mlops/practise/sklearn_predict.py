import mlflow
logged_model = 'runs:/26bb721b00304fc8894a16733ff31074/log_reg_model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Next, let’s briefly look at how you can load the models logged by MLFlow.
# Go back to the experiment and click a run. Note the run ID at the top and
# copy it. Then, go back to the notebook, and run the following. Note that
# there is a placeholder for the run ID

# Predict on a Pandas DataFrame.
import pandas as pd

data_path = "creditcard_pred.csv"
data = pd.read_csv(data_path)

print(loaded_model.predict(pd.DataFrame(data)))