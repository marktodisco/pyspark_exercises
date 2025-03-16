from pathlib import Path


exercises = sorted(list(Path(".").rglob("Exercises.ipynb")))
pyspark_solutions = sorted(list(Path(".").rglob("Solutions_PySpark.ipynb")))


print(f"{len(pyspark_solutions)} of {len(exercises)} completed")
print(f"Progress: {len(pyspark_solutions) / len(exercises):.2%}")
