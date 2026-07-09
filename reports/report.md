# Findings of the Analysis

## Dataset Overview

The Kenya Agriculture dataset was successfully processed using Apache Spark following a complete big data analytics workflow comprising data loading, cleaning, transformation, and exploratory data analysis.

### Dataset Summary

| Metric | Value |
|---------|------:|
| Original Records | 24,233 |
| Records After Cleaning | 23,502 |
| Columns | 17 |
| Missing Values Removed | 731 |
| Duplicate Records | 0 |

During data cleaning, 731 records with missing values in the **Value** column were removed. No duplicate records or invalid negative values were found. Column names were standardized to improve consistency across the analysis.

---

# Transformation Results

The cleaned dataset was divided into separate analytical datasets according to the agricultural element to enable focused analysis.

| Agricultural Element | Records |
|----------------------|--------:|
| Production | 9,278 |
| Yield | 5,164 |
| Area Harvested | 5,100 |
| Stocks | 768 |
| Producing Animals/Slaughtered | 1,176 |
| Yield/Carcass Weight | 1,020 |
| Milk Animals | 255 |
| Laying | 741 |

Each transformed dataset contains five analytical variables:

- Item
- Element
- Year
- Unit
- Value

---

# Exploratory Data Analysis Findings

## 1. Production Trends Over Time

Agricultural production generally increased over the years.

The total production recorded:

- **Lowest production year:** **1961** with approximately **10.32 million tonnes**
- **Highest production year:** **2024** with approximately **76.01 million tonnes**

The results indicate substantial long-term growth in Kenya's agricultural production.

---

## 2. Highest Producing Agricultural Commodities

The analysis identified the following commodities as contributing the highest total production.

| Rank | Commodity |
|-----:|-----------|
| 1 | Sugar Crops Primary |
| 2 | Sugar cane |
| 3 | Cereals, primary |
| 4 | Milk, Total |
| 5 | Maize (corn) |
| 6 | Raw milk of cattle |
| 7 | Roots and Tubers, Primary |
| 8 | Fruit Primary |
| 9 | Vegetables Primary |
| 10 | Hen eggs in shell |

Sugar crops and cereals dominate Kenya's agricultural production, with maize remaining one of the country's most significant food crops.

---

## 3. Lowest Producing Agricultural Commodities

The commodities with the smallest recorded production totals were:

- Whey, dry
- Areca nuts
- Vanilla, raw
- Artichokes
- Abaca (Manila hemp)
- Nutmeg, mace and cardamoms
- Apricots
- Whole milk, evaporated
- Asparagus
- Ginger, raw

These commodities contribute only a very small proportion of Kenya's overall agricultural output.

---

## 4. Production Statistics

Summary statistics for the Production dataset:

| Statistic | Value |
|-----------|-------:|
| Records | 9,278 |
| Mean Production | 253,978.06 |
| Minimum Production | 0 |
| Maximum Production | 9,365,300 |
| Standard Deviation | 785,014.70 |

The large standard deviation indicates considerable variation in production levels among different agricultural commodities.

---

## 5. Area Harvested

Area harvested contains **5,100** observations representing **96 unique agricultural commodities**.

Summary statistics:

| Statistic | Value |
|-----------|-------:|
| Mean | 106,449.59 |
| Minimum | 1 |
| Maximum | 2,940,254 |

This indicates substantial differences in land allocation among crops.

---

## 6. Yield Analysis

Yield contains **5,164** observations covering **97 agricultural commodities**.

Summary statistics:

| Statistic | Value |
|-----------|-------:|
| Mean Yield | 7,511.13 |
| Minimum | 33.3 |
| Maximum | 121,184.5 |

Yield measures agricultural productivity per unit area and provides insights into production efficiency.

---

## 7. Agricultural Commodity Coverage

The dataset contains a diverse range of agricultural commodities across different elements.

| Agricultural Element | Unique Items |
|----------------------|-------------:|
| Production | 161 |
| Yield | 97 |
| Area Harvested | 96 |
| Producing Animals/Slaughtered | 23 |
| Yield/Carcass Weight | 20 |
| Stocks | 12 |
| Milk Animals | 5 |
| Laying | 2 |

Production covers the widest range of agricultural commodities in the dataset.

---

## 8. Measurement Units

Different agricultural indicators are recorded using different measurement units.

Examples include:

- tonnes (t)
- hectares (ha)
- kilograms per hectare (kg/ha)
- number of animals
- grams per animal
- thousands of animals

These units reflect the diversity of crop and livestock information contained in the dataset.

---

# Research Questions Answered

### 1. How has agricultural production changed over time?

Agricultural production has generally increased over the study period, rising from approximately **10.32 million tonnes in 1961** to **76.01 million tonnes in 2024**.

---

### 2. Which crops have the highest production?

The highest-producing agricultural commodities include Sugar Crops Primary, Sugar cane, Cereals (primary), Milk (total), and Maize.

---

### 3. Which crops have the lowest production?

The lowest production levels were observed for commodities such as Whey (dry), Areca nuts, Vanilla, Artichokes, and Abaca.

---

### 4. Which year recorded the highest agricultural production?

**2024** recorded the highest agricultural production in the dataset.

---

### 5. Which year recorded the lowest agricultural production?

**1961** recorded the lowest agricultural production.

---

### 6. What is the average agricultural production?

The average production value across all production records is **253,978.06**.

---

### 7. How many different crops are represented?

The Production dataset contains **161 unique agricultural commodities**.

---

### 8. Which production units are used?

Production data is primarily recorded in **tonnes (t)**, while other agricultural elements use hectares, kilograms per hectare, animal counts, and livestock-specific units.

---

# Conclusion

The analysis demonstrates that Apache Spark can efficiently process and analyze agricultural datasets containing thousands of records. Following data cleaning and transformation, the dataset provided valuable insights into Kenya's agricultural sector.

The results indicate long-term growth in agricultural production, with sugar crops, cereals, milk, and maize contributing the largest production volumes. Production, yield, harvested area, and livestock indicators collectively provide a comprehensive view of Kenya's agricultural performance and can support evidence-based planning, policy formulation, and future predictive analytics.