from src.model.train import train_model

if __name__ == "__main__":
    train_model("data/employee_data.csv", "models/model.pkl")