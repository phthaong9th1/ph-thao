import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Nhập dữ liệu (Mục 2 & 4)
data = {
    'Cong ty': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Doanh thu': [3, 6, 9, 10, 12, 15, 18, 20, 25, 8, 14, 22],
    'Loi nhuan': [1.1, 2.0, 3.2, 3.4, 3.9, 5.0, 6.2, 6.6, 8.2, 2.5, 4.5, 7.5],
    'Label': ['Kem', 'Kem', 'Binh thuong', 'Binh thuong', 'Binh thuong', 'Tot', 'Tot', 'Tot', 'Xuat sac', 'Kem', 'Binh thuong', 'Xuat sac']
}
df = pd.DataFrame(data)

# 2. Phân tích kết quả (Mục 2)
df['Ty_le_LN'] = (df['Loi nhuan'] / df['Doanh thu'] * 100).round(2)
print("--- KẾT QUẢ PHÂN TÍCH ---")
print(df)

# 3. Trực quan hóa dữ liệu (Mục 5 - Yêu cầu dùng Seaborn)
plt.figure(figsize=(10, 5))
sns.barplot(x='Label', y='Doanh thu', data=df, palette='viridis')
plt.title('Doanh thu trung binh theo tung nhom phan loai')
plt.show()