import pandas as pd
import numpy as np

def generate_data():
    data = {
        "experience": np.random.randint(1, 10, 100),
        "education_level": np.random.randint(1, 5, 100),
        "performance_score": np.random.randint(50, 100, 100)
    }

    df = pd.DataFrame(data)
    df.to_csv("data/employee_data.csv", index=False)
    print("Data generated successfully")

if __name__ == "__main__":
    generate_data()