#!/usr/bin/env python3
"""
Quick test to verify all countries are available in the dashboard
"""

# Test to verify dashboard countries list includes Pakistan
from pyspark.sql import SparkSession
import sys

print("🔍 Testing country availability...")

# Initialize minimal Spark session
spark = SparkSession.builder \
    .appName("CountryTest") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()

try:
    # Load and check countries
    df = spark.read.csv("GlobalLandTemperaturesByCity.csv", header=True, inferSchema=True)
    countries = df.select("Country").distinct().orderBy("Country").collect()
    countries_list = [row['Country'] for row in countries]
    
    print(f"📊 Total countries found: {len(countries_list)}")
    print(f"🔍 Pakistan in list: {'Pakistan' in countries_list}")
    print(f"🇵🇰 Pakistan position: {countries_list.index('Pakistan') + 1 if 'Pakistan' in countries_list else 'Not found'}")
    
    # Show countries around Pakistan alphabetically
    print("\n📝 Countries starting with 'P':")
    p_countries = [c for c in countries_list if c.startswith('P')]
    for i, country in enumerate(p_countries, 1):
        print(f"   {i}. {country}")
    
    # Check first 30 countries (the previous limit)
    print(f"\n🔢 First 30 countries:")
    for i, country in enumerate(countries_list[:30], 1):
        print(f"   {i:2d}. {country}")
        
    print(f"\n✅ All {len(countries_list)} countries should now be available in the Global Comparison dropdown!")
    
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    spark.stop()
