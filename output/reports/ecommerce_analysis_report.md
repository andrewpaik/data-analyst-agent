# E-Commerce Sales Analysis Report — 2023-2024

**Date:** February 5, 2026
**Dataset:** 2,000 orders across 6 product categories, 4 regions, 4 sales channels
**Period:** January 2023 – December 2024

---

## 1. Executive Summary

- **Revenue grew 4.3% YoY** ($192,692 → $201,005), while **profit surged 11.9%** ($38,412 → $42,978), indicating improved operational efficiency and margin management.
- **Electronics dominates revenue** at $186,063 (47% of total) but carries the **highest return rate (17.9%)**, presenting a clear margin risk.
- **VIP customers receive 2× the discount** (20.1% avg vs ~10% for others) but show the **lowest return rate (10.3%)**, validating the loyalty program's retention value.
- **Product category is the strongest driver of revenue differences** (ANOVA η² = 0.19, p < 0.001), not region or channel — pricing and product mix matter more than geography.
- **Profit is highly predictable** (Random Forest R² = 0.83) with unit price and quantity explaining 80% of variance — returns, however, are essentially unpredictable from order data (AUC = 0.53).

---

## 2. Key Metrics

| Metric | 2023 | 2024 | YoY Change |
|--------|------|------|------------|
| Total Revenue | $192,692 | $201,005 | **+4.3%** |
| Total Profit | $38,412 | $42,978 | **+11.9%** |
| Orders | 1,000 | 1,000 | 0.0% |
| Avg Order Value | $192.69 | $201.00 | +4.3% |
| Return Rate | 12.0% | 12.0% | 0.0% |
| Avg Satisfaction | 3.86 | 3.84 | -0.5% |

| Segment | Revenue Share | Avg Order | Return Rate |
|---------|--------------|-----------|-------------|
| Returning | $171,510 (43.6%) | $192 | 11.5% |
| New | $144,040 (36.6%) | $201 | 13.8% |
| VIP | $78,147 (19.9%) | $200 | 10.3% |

---

## 3. Findings

### Finding 1: Electronics Is the Revenue Engine — and the Biggest Risk

- **What:** Electronics accounts for 47% of revenue ($186,063) despite being only 25% of orders. Average order value is $366 — 2.5× the next category (Home & Garden at $206).
- **So What:** This concentration creates revenue dependency. Electronics also has the highest return rate at 17.9% (vs 5.2% for Books), meaning ~$33K in revenue is at risk from returns annually.
- **Now What:** Investigate root causes of Electronics returns (defects vs buyer's remorse). Consider targeted return-reduction initiatives (better product descriptions, sizing guides for accessories) to protect the highest-value category.

### Finding 2: Profit Grew Faster Than Revenue — Margins Are Improving

- **What:** Revenue grew 4.3% YoY but profit grew 11.9%. Average profit margin across all orders is ~20%.
- **So What:** The business is becoming more efficient. This could be driven by better cost management, category mix shifts, or strategic discounting.
- **Now What:** Identify which specific changes drove the disproportionate profit improvement and double down. Track cost-of-goods trends by category to sustain the momentum.

### Finding 3: VIP Discounts Are Working — But at a Cost

- **What:** VIP customers receive an average 20.1% discount (vs 9.9% for Returning and 9.8% for New). Despite this, VIPs have the lowest return rate (10.3%) and comparable satisfaction scores (3.84).
- **So What:** The VIP discount program successfully drives loyalty and reduces returns, but the heavy discounting compresses margins. The profit margin difference between segments is statistically significant (ANOVA p < 0.001, η² = 0.18).
- **Now What:** Analyze VIP LTV to confirm the discount investment pays off over the customer lifecycle. Consider tiered discounting to reduce blanket discount rates while maintaining loyalty.

### Finding 4: Product Category Drives Revenue — Not Region or Channel

- **What:** ANOVA testing shows product category explains 19.3% of revenue variance (F = 95.2, p < 0.001), while region explains only 0.2% (F = 1.6, p = 0.19 — not significant).
- **So What:** Geographic expansion or channel optimization will yield minimal revenue impact compared to product strategy. The business is nationally consistent but product-dependent.
- **Now What:** Focus strategic investment on product category expansion and pricing optimization rather than regional marketing campaigns. Explore adjacent product categories to Electronics that might carry high AOV with lower return rates.

### Finding 5: Return Behavior Cannot Be Predicted from Order Data

- **What:** A Random Forest classifier trained on order features (price, quantity, discount, age, category, segment) achieved only 0.53 AUC — barely better than a coin flip.
- **So What:** Returns appear to be driven by factors not captured in the transactional data (product quality, shipping damage, customer expectations, etc.).
- **Now What:** Collect additional data to improve return prediction: product reviews, order notes, shipping carrier, packaging type. Consider post-purchase surveys for returned items.

### Finding 6: Returned Orders Have Higher Revenue

- **What:** Average revenue for returned orders ($243) is significantly higher than non-returned orders ($190) (t-test p = 0.002, Cohen's d = 0.19).
- **So What:** Higher-value purchases are more likely to be returned, potentially because customers are more deliberate about expensive purchases. This small but significant effect concentrates return costs on the most valuable transactions.
- **Now What:** Implement enhanced purchase confidence measures for high-AOV orders: detailed product specs, comparison tools, liberal return policies that emphasize exchanges over refunds.

### Finding 7: Books Have Exceptional Retention

- **What:** Books have the lowest return rate at just 5.2% — less than half the overall average. They also carry a solid profit margin (20.3%) despite low AOV ($51).
- **So What:** While Books contribute only 2.9% of revenue, they represent a reliable, low-risk category with loyal customers.
- **Now What:** Use Books as a customer acquisition channel — low price point and low returns make them ideal for first-time buyer campaigns. Cross-sell higher-AOV categories to Books customers.

---

## 4. Recommendations

| Priority | Action | Expected Impact | Effort |
|----------|--------|----------------|--------|
| **HIGH** | Investigate and reduce Electronics return rate from 18% → 12% | ~$10K annual profit recovery | Medium |
| **HIGH** | Analyze VIP lifetime value to validate 20% discount investment | Data-driven discount optimization | Low |
| **MEDIUM** | Collect post-return survey data to understand return drivers | Enable predictive return models | Low |
| **MEDIUM** | Use Books as low-risk acquisition entry point, then cross-sell | Incremental new customer revenue | Medium |
| **LOW** | Implement high-AOV purchase confidence features | Reduce returns on largest orders | Medium |
| **LOW** | Test reduced VIP discount tiers (15% vs 20%) via A/B testing | Margin improvement without churn | High |

---

## 5. Methodology

### Data
- **Source:** `ecommerce_sales_2023_2024.csv` (2,020 raw rows, 16 columns)
- **Cleaning:** Removed 20 duplicates, imputed 283 missing values (median strategy), standardized category names (19 → 6 after fixing whitespace/casing), flagged 31 price outliers
- **Final dataset:** 2,000 rows × 24 columns (8 derived features added)

### Statistical Tests
- **ANOVA** (one-way) for comparing means across 3+ groups, with η² effect sizes
- **Chi-square test** for categorical associations, with Cramér's V
- **Independent t-test** for two-group mean comparisons, with Cohen's d
- **Pearson/Spearman correlations** for bivariate relationships
- **OLS regression** for multivariate profit modeling (R² = 0.575)
- **Logistic regression** for return probability modeling

### Predictive Models
- **Profit prediction:** Random Forest Regressor (R² = 0.83, RMSE = $22.57, 5-fold CV R² = 0.81 ± 0.05)
- **Return prediction:** Random Forest Classifier (AUC = 0.53 — not viable for production use)
- **Train/test split:** 80/20, stratified for classification
- **All significance tests** used α = 0.05 threshold

### Assumptions & Caveats
- Missing values were imputed with median; results may be slightly compressed toward central tendency
- 31 extreme price outliers were flagged but retained — excluding them would lower revenue metrics
- Return behavior analysis is limited to order-level features; customer history and product-level data would improve models
- Correlation ≠ causation — YoY improvements may reflect external factors not captured in the data

---

## 6. Appendix

### A. Visualizations

| # | Chart | File |
|---|-------|------|
| 1 | Numeric variable distributions | `01_numeric_distributions.png` |
| 2 | Categorical variable distributions | `02_categorical_distributions.png` |
| 3 | Box plots (spread & outliers) | `03_boxplots.png` |
| 4 | Correlation heatmap | `04_correlation_heatmap.png` |
| 5 | Top correlation scatter plots | `05_scatter_top_correlations.png` |
| 6 | Monthly temporal trends | `06_temporal_trends.png` |
| 7 | Revenue by day of week | `07_revenue_by_dayofweek.png` |
| 8 | Segmentation analysis (4 panels) | `08_segmentation_analysis.png` |
| 9 | Feature importance — profit model | `09_feature_importance_profit.png` |
| 10 | Executive dashboard | `10_executive_dashboard.png` |
| 11 | Year-over-year comparison | `11_yoy_comparison.png` |
| 12 | Revenue composition by quarter | `12_revenue_composition.png` |

### B. Strong Correlations (|r| > 0.7)

| Variable Pair | Pearson r |
|---------------|-----------|
| unit_price ↔ cost | 0.939 |
| revenue ↔ net_revenue | 0.995 |
| revenue ↔ profit | 0.866 |
| profit ↔ net_revenue | 0.898 |
| discount_pct ↔ profit_margin | -0.707 |

### C. File Inventory

```
data/raw/ecommerce_sales_2023_2024.csv        — Original dataset (2,020 rows)
data/cleaned/ecommerce_sales_cleaned.csv       — Cleaned dataset (2,000 rows, 24 cols)
data/cleaned/cleaning_log.txt                  — Full cleaning transformation log
output/charts/*.png                            — 12 high-resolution visualizations
output/reports/ecommerce_analysis_report.md    — This report
```
