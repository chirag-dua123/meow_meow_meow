
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tempfile


def main():
	p = Path(__file__).resolve()
	root = p
	for _ in range(10):
		if (root / 'data').exists():
			break
		if root.parent == root:
			break
		root = root.parent
	data_path = root / 'data' / 'pokemon.csv'
	outputs = root / 'outputs'
	print('DEBUG: root =', root)
	print('DEBUG: data_path =', data_path)
	print('DEBUG: outputs =', outputs)
	print('DEBUG: outputs exists before mkdir =', outputs.exists())
	try:
		outputs.mkdir(parents=True, exist_ok=True)
		test_file = outputs / '.write_test'
		with open(test_file, 'w', encoding='utf-8') as tf:
			tf.write('x')
		test_file.unlink()
		print('DEBUG: outputs writable')
	except Exception:
		outputs = Path(tempfile.gettempdir()) / 'ai_engineer_eda_outputs'
		outputs.mkdir(parents=True, exist_ok=True)
		print('DEBUG: falling back to temp directory', outputs)

	df = pd.read_csv(data_path)
	if '#' in df.columns:
		df = df.rename(columns={'#': 'ID'})
	df.columns = [c.strip() for c in df.columns]
	if df['Legendary'].dtype == object:
		df['Legendary'] = df['Legendary'].map({'True': True, 'False': False}).fillna(False)

	num_cols = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
	for c in num_cols:
		if c in df.columns:
			df[c] = pd.to_numeric(df[c], errors='coerce')

	df = df[df['Name'].notna()]
	df = df.dropna(subset=['Total'])
	if 'Type 2' in df.columns:
		df['Type 2'] = df['Type 2'].fillna('')

	clean_path = outputs / 'pokemon_clean.csv'
	print('DEBUG: will write cleaned csv to', clean_path)
	df.to_csv(clean_path, index=False)

	stats_cols = [c for c in num_cols if c in df.columns]
	corr = df[stats_cols].corr()

	plt.figure(figsize=(8, 6))
	sns.heatmap(corr, annot=True, fmt='.2f', cmap='vlag', center=0)
	plt.title('Stats Correlation')
	heatmap_path = outputs / 'pokemon_stats_correlation.png'
	plt.tight_layout()
	plt.savefig(heatmap_path)
	plt.close()

	plt.figure(figsize=(6, 6))
	sns.boxplot(x='Legendary', y='Attack', data=df)
	plt.title('Attack by Legendary Status')
	boxplot_path = outputs / 'attack_legendary_boxplot.png'
	plt.tight_layout()
	plt.savefig(boxplot_path)
	plt.close()

	corr_with_total = corr['Total'].drop('Total').abs().sort_values(ascending=False)
	top_stat = corr_with_total.index[0]
	top_stat_val = corr_with_total.iloc[0]

	if 'Type 1' in df.columns:
		median_total_by_type1 = df.groupby('Type 1')['Total'].median().sort_values(ascending=False)
		top_types = median_total_by_type1.head(5).to_dict()
	else:
		top_types = {}

	top_pokemon = df.sort_values('Total', ascending=False).head(10)[['Name', 'Type 1', 'Type 2', 'Total', 'Legendary']]

	attack_legend = df[df['Legendary'] == True]['Attack'].dropna()
	attack_non = df[df['Legendary'] == False]['Attack'].dropna()
	if len(attack_legend) > 1 and len(attack_non) > 1:
		try:
			from scipy import stats as ss
			tstat, pval = ss.ttest_ind(attack_legend, attack_non, equal_var=False)
		except Exception:
			combined = np.concatenate([attack_legend.values, attack_non.values])
			n1 = len(attack_legend)
			obs = attack_legend.mean() - attack_non.mean()
			rng = np.random.default_rng(42)
			perms = 5000
			diffs = []
			for _ in range(perms):
				rng.shuffle(combined)
				diff = combined[:n1].mean() - combined[n1:].mean()
				diffs.append(diff)
			diffs = np.array(diffs)
			pval = (np.abs(diffs) >= abs(obs)).sum() / perms
			tstat = obs
	else:
		tstat, pval = float('nan'), float('nan')

	report_lines = []
	report_lines.append('Data cleaning: kept rows with numeric stats, filled Type 2 empties, mapped Legendary to bool.')
	report_lines.append('')
	report_lines.append(f'Insight 1: Stat most correlated with Total: {top_stat} (abs corr {top_stat_val:.2f})')
	report_lines.append('')
	report_lines.append('Insight 2: Top types by median Total:')
	for t, val in list(top_types.items()):
		report_lines.append(f'- {t}: median Total = {val}')
	report_lines.append('')
	report_lines.append('Insight 3: Top 10 Pokémon by Total:')
	for _, row in top_pokemon.iterrows():
		report_lines.append(f'- {row.Name} ({row["Type 1"]}/{row["Type 2"]}) Total={row.Total}, Legendary={row.Legendary}')
	report_lines.append('')
	report_lines.append('Statistical comparison: Attack Legendary vs Non-Legendary')
	report_lines.append(f't-statistic={tstat:.3f}, p-value={pval:.5f}')
	if pval == pval and pval < 0.05:
		report_lines.append('Conclusion: Difference in Attack between Legendary and non-Legendary is statistically significant (p<0.05).')
	elif pval == pval:
		report_lines.append('Conclusion: No statistically significant difference in Attack (p>=0.05).')
	else:
		report_lines.append('Conclusion: Not enough data to run t-test.')
	report_lines.append('')
	report_lines.append('Saved cleaned CSV to: {}'.format(clean_path.as_posix()))
	report_lines.append('Saved correlation heatmap to: {}'.format(heatmap_path.as_posix()))
	report_lines.append('Saved Attack boxplot to: {}'.format(boxplot_path.as_posix()))

	with open(outputs / 'EDA_report.txt', 'w', encoding='utf-8') as f:
		f.write('\n'.join(report_lines))

	print('\n'.join(report_lines))


if __name__ == '__main__':
	main()
