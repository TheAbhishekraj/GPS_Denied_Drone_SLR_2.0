#!/usr/bin/env python3
"""
Script 2: Generate Figures for the Systematic Review
Input:  data/processed/database_final_231.csv
Output: analysis/output/figures/*.png
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================================================
# CONFIG – Relative paths (assumes running from project root)
# ============================================================
INPUT_FILE = 'data/processed/database_final_231.csv'
OUTPUT_DIR = 'analysis/output/figures'

# ============================================================
# LOAD DATA
# ============================================================
df = pd.read_csv(INPUT_FILE)
print(f"✅ Loaded {len(df)} papers for figures")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
# SET STYLE
# ============================================================
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# ============================================================
# FIGURE 1: Publications Over Time
# ============================================================
fig, ax = plt.subplots()
year_counts = df['Year'].value_counts().sort_index()
year_counts.plot(kind='bar', ax=ax, color='steelblue')
ax.set_title('Publications over Time (2015–2025)', fontsize=14)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Publications')
for i, v in enumerate(year_counts):
    ax.text(i, v + 0.5, str(v), ha='center', va='bottom')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/fig1_publications_over_time.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figure 1: Publications over time")

# ============================================================
# FIGURE 2: Sensor Types
# ============================================================
fig, ax = plt.subplots()
sensor_counts = df['Sensor Type'].value_counts().head(10)
sensor_counts.plot(kind='barh', ax=ax, color='coral')
ax.set_title('Top 10 Sensor Configurations', fontsize=14)
ax.set_xlabel('Number of Papers')
ax.invert_yaxis()
for i, v in enumerate(sensor_counts):
    ax.text(v + 0.5, i, str(v), va='center')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/fig2_sensor_types.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figure 2: Sensor types")

# ============================================================
# FIGURE 3: Navigation Methods
# ============================================================
fig, ax = plt.subplots()
method_counts = df['Navigation Method'].value_counts()
method_counts.plot(kind='bar', ax=ax, color='mediumseagreen')
ax.set_title('Navigation Methods', fontsize=14)
ax.set_xlabel('Method')
ax.set_ylabel('Number of Papers')
for i, v in enumerate(method_counts):
    ax.text(i, v + 0.5, str(v), ha='center', va='bottom')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/fig3_navigation_methods.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figure 3: Navigation methods")

# ============================================================
# FIGURE 4: Indoor vs Outdoor
# ============================================================
fig, ax = plt.subplots()
indoor_outdoor = df['Indoor/Outdoor'].value_counts()
colors = ['#2ecc71', '#e67e22', '#3498db']
indoor_outdoor.plot(kind='pie', ax=ax, autopct='%1.1f%%', colors=colors, startangle=90)
ax.set_title('Indoor vs Outdoor vs Mixed', fontsize=14)
ax.set_ylabel('')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/fig4_indoor_outdoor.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figure 4: Indoor vs Outdoor")

# ============================================================
# FIGURE 5: Real Flight vs Simulation
# ============================================================
fig, ax = plt.subplots()
real_counts = df['Real Flight'].value_counts()
real_counts.plot(kind='bar', ax=ax, color=['#27ae60', '#c0392b'])
ax.set_title('Real Flight vs Simulation-Only', fontsize=14)
ax.set_xlabel('Real Flight')
ax.set_ylabel('Number of Papers')
for i, v in enumerate(real_counts):
    ax.text(i, v + 0.5, str(v), ha='center', va='bottom')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/fig5_real_vs_sim.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Figure 5: Real vs Simulation")

# ============================================================
# FIGURE 6: ATE RMSE Distribution
# ============================================================
ate = df[(df['Localization metric'] == 'ATE RMSE (m)') & (df['Real Flight'] == 'Yes')]
if len(ate) > 0:
    fig, ax = plt.subplots()
    ax.boxplot(ate['Reported numeric value'].dropna(), vert=True)
    ax.set_title('Distribution of ATE RMSE (m) for Real Flight Studies', fontsize=14)
    ax.set_ylabel('ATE RMSE (m)')
    ax.set_xticklabels(['ATE RMSE'])
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig6_ate_rmse_distribution.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✅ Figure 6: ATE RMSE distribution")
else:
    print("⚠️ No ATE RMSE data for Figure 6")

print("\n✅ All figures generated in analysis/output/figures/")

# ============================================================
# FIGURE 7: ATE RMSE by Sensor Type (Accuracy Comparison)
# ============================================================
if len(ate) > 0:
    ate_sensor = ate.dropna(subset=['Sensor Type', 'Reported numeric value']).copy()
    sensor_counts = ate_sensor['Sensor Type'].value_counts()
    keep_sensors = sensor_counts[sensor_counts >= 3].index
    ate_filtered = ate_sensor[ate_sensor['Sensor Type'].isin(keep_sensors)]

    if len(ate_filtered) > 0:
        order = ate_filtered.groupby('Sensor Type')['Reported numeric value'].median().sort_values().index

        fig, ax = plt.subplots(figsize=(12, 7))
        # Use hue to avoid deprecation warning, with legend=False
        sns.boxplot(data=ate_filtered, x='Sensor Type', y='Reported numeric value',
                    order=order, hue='Sensor Type', palette='Set3', showfliers=False, legend=False)
        sns.swarmplot(data=ate_filtered, x='Sensor Type', y='Reported numeric value',
                      order=order, color='black', alpha=0.6, size=4)

        ax.set_title('ATE RMSE by Sensor Type (Real Flight Studies)', fontsize=14)
        ax.set_xlabel('Sensor Type')
        ax.set_ylabel('ATE RMSE (m)')
        # Rotate x‑axis labels correctly
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/fig7_ate_rmse_by_sensor.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ Figure 7: ATE RMSE by sensor type")
    else:
        print("⚠️ Not enough sensor groups (≥3 papers) for Figure 7")
else:
    print("⚠️ No ATE RMSE data for Figure 7")
    
# # ============================================================
# FIGURE 8: Mean ATE RMSE by Sensor Type (± SD)
# ============================================================
if len(ate) > 0:
    ate_sensor = ate.dropna(subset=['Sensor Type', 'Reported numeric value']).copy()
    sensor_counts = ate_sensor['Sensor Type'].value_counts()
    keep_sensors = sensor_counts[sensor_counts >= 3].index
    ate_filtered = ate_sensor[ate_sensor['Sensor Type'].isin(keep_sensors)]

    if len(ate_filtered) > 0:
        # Compute mean and standard deviation per sensor type
        stats = ate_filtered.groupby('Sensor Type')['Reported numeric value'].agg(['mean', 'std', 'count'])
        stats = stats.sort_values('mean')   # best on the left

        fig, ax = plt.subplots(figsize=(12, 7))
        # Bar plot with error bars (mean ± SD)
        bars = ax.bar(stats.index, stats['mean'], yerr=stats['std'],
                      capsize=5, color='teal', edgecolor='black', alpha=0.8)
        ax.set_title('Mean ATE RMSE by Sensor Type (± Standard Deviation)', fontsize=16)
        ax.set_xlabel('Sensor Type', fontsize=14)
        ax.set_ylabel('Mean ATE RMSE (m)', fontsize=14)
        ax.tick_params(axis='x', labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        # Rotate x‑axis labels
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        # Add mean values on top of bars
        for i, v in enumerate(stats['mean']):
            ax.text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom', fontsize=9)
        # Add number of papers (n) below x‑axis labels for transparency
        for i, n in enumerate(stats['count']):
            ax.text(i, -0.08, f'n={n}', ha='center', va='top', fontsize=9, transform=ax.get_xaxis_transform())
        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/fig8_ate_rmse_mean_by_sensor.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ Figure 8: Mean ATE RMSE by sensor type (±SD)")
    else:
        print("⚠️ Not enough sensor groups (≥3 papers) for Figure 8")
else:
    print("⚠️ No ATE RMSE data for Figure 8")
    
  # ============================================================
# FIGURE 9: Median ATE RMSE by Sensor Type (with IQR)
# ============================================================
if len(ate) > 0:
    ate_sensor = ate.dropna(subset=['Sensor Type', 'Reported numeric value']).copy()
    # Keep only sensor types with at least 3 papers
    sensor_counts = ate_sensor['Sensor Type'].value_counts()
    keep_sensors = sensor_counts[sensor_counts >= 3].index
    ate_filtered = ate_sensor[ate_sensor['Sensor Type'].isin(keep_sensors)]

    if len(ate_filtered) > 0:
        # Compute median, quartiles, and count
        stats = ate_filtered.groupby('Sensor Type')['Reported numeric value'].agg(
            median='median',
            q25=lambda x: x.quantile(0.25),
            q75=lambda x: x.quantile(0.75),
            count='count'
        )
        stats['iqr'] = stats['q75'] - stats['q25']
        # Sort by median (best performance on the left)
        stats = stats.sort_values('median')

        fig, ax = plt.subplots(figsize=(12, 7))
        bars = ax.bar(
            stats.index,
            stats['median'],
            yerr=stats['iqr'],
            capsize=5,
            color='coral',
            edgecolor='black',
            alpha=0.8,
            error_kw={'ecolor': 'black', 'linewidth': 1.5}
        )
        ax.set_title('Median ATE RMSE by Sensor Type (Interquartile Range)', fontsize=16)
        ax.set_xlabel('Sensor Type', fontsize=14)
        ax.set_ylabel('Median ATE RMSE (m)', fontsize=14)
        ax.tick_params(axis='x', labelsize=12)
        ax.tick_params(axis='y', labelsize=12)

        # Rotate x‑axis labels
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

        # Add median values on top of bars
        for i, v in enumerate(stats['median']):
            ax.text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom', fontsize=9)

        # Add sample size (n) below x‑axis labels
        for i, n in enumerate(stats['count']):
            ax.text(i, -0.08, f'n={n}', ha='center', va='top', fontsize=9, transform=ax.get_xaxis_transform())

        ax.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/fig9_ate_rmse_median_by_sensor.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ Figure 9: Median ATE RMSE by sensor type (IQR)")
    else:
        print("⚠️ Not enough sensor groups (≥3 papers) for Figure 9")
else:
    print("⚠️ No ATE RMSE data for Figure 9")
    
    