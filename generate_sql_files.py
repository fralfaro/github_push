import pandas as pd
import os

# Datos inventados para el DataFrame
data = {
    "object_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "definition": [
        "CREATE PROCEDURE dbo.uspExample1 AS SELECT * FROM Table1",
        "CREATE PROCEDURE dbo.uspExample2 AS SELECT * FROM Table2",
        "CREATE PROCEDURE dbo.uspExample3 AS SELECT * FROM Table3",
        "CREATE PROCEDURE dbo.uspExample4 AS SELECT * FROM Table4",
        "CREATE PROCEDURE dbo.uspExample5 AS SELECT * FROM Table5",
        "CREATE PROCEDURE dbo.uspExample6 AS SELECT * FROM Table6",
        "CREATE PROCEDURE dbo.uspExample7 AS SELECT * FROM Table7",
        "CREATE PROCEDURE dbo.uspExample8 AS SELECT * FROM Table8",
        "CREATE PROCEDURE dbo.uspExample9 AS SELECT * FROM Table9",
        "CREATE PROCEDURE dbo.uspExample10 AS SELECT * FROM Table10",
    ]
}

# Crear DataFrame con los datos
df = pd.DataFrame(data)

# Crear carpeta para guardar los archivos SQL
output_dir = "sql_queries"
os.makedirs(output_dir, exist_ok=True)

# Guardar cada definición en un archivo .sql
for index, row in df.iterrows():
    object_id = row['object_id']
    definition = row['definition'].replace("dbo", "new_dbo")  # Reemplazar 'dbo' por 'new_dbo'
    file_path = os.path.join(output_dir, f"{object_id}.sql")
    with open(file_path, "w") as file:
        file.write(definition)

print(f"SQL files have been saved in the directory: {output_dir}")