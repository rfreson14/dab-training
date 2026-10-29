import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--env", default="dev-test")
parser.add_argument("--run_date", default="2026-10-29")
args = parser.parse_args()

print(f"Running in {args.env} for {args.run_date}")
df = spark.range(10).withColumnRenamed("id", "n")
print(f"Row count: {df.count()}")