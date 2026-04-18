# MySQL統計関数と集計関数ガイド

## 1. 前提: サンプルテーブル

```sql
CREATE TABLE sales (
  id BIGINT PRIMARY KEY,
  sold_at DATETIME NOT NULL,
  store_id INT NOT NULL,
  product_id INT NOT NULL,
  qty INT NOT NULL,
  unit_price DECIMAL(10,2) NOT NULL
);
```

売上金額は `qty * unit_price` とする。

## 1-1. 各カラムの日本語説明
- `id`: 売上レコードを一意に識別するID。
- `sold_at`: 売上が発生した日時。
- `store_id`: 売上が発生した店舗ID。
- `product_id`: 売れた商品ID。
- `qty`: 販売数量（個数）。
- `unit_price`: 商品1単位あたりの単価。
- `qty * unit_price`（計算列）: 売上金額。クエリ内で都度計算する派生値。

## 2. 基本の集計関数

### 2-1. 件数: `COUNT`
```sql
SELECT COUNT(*) AS row_count
FROM sales;
```

### 2-2. 合計: `SUM`
```sql
SELECT SUM(qty * unit_price) AS total_amount
FROM sales;
```

### 2-3. 平均: `AVG`
```sql
SELECT AVG(qty * unit_price) AS avg_amount
FROM sales;
```

### 2-4. 最小・最大: `MIN`, `MAX`
```sql
SELECT
  MIN(qty * unit_price) AS min_amount,
  MAX(qty * unit_price) AS max_amount
FROM sales;
```

## 3. GROUP BY と HAVING

### 3-1. 店舗ごとの日次売上
```sql
SELECT
  DATE(sold_at) AS sold_date,
  store_id,
  SUM(qty * unit_price) AS daily_sales,
  COUNT(*) AS tx_count
FROM sales
GROUP BY DATE(sold_at), store_id
ORDER BY sold_date, store_id;
```

### 3-2. 集計後の条件で絞る（HAVING）
```sql
SELECT
  store_id,
  SUM(qty * unit_price) AS total_sales
FROM sales
GROUP BY store_id
HAVING SUM(qty * unit_price) >= 100000;
```

## 4. 統計関数（分散・標準偏差）

### 4-1. 標本標準偏差と標本分散
```sql
SELECT
  STDDEV_SAMP(qty * unit_price) AS stddev_amount,
  VAR_SAMP(qty * unit_price) AS var_amount
FROM sales;
```

### 4-2. 母集団として扱う場合
```sql
SELECT
  STDDEV_POP(qty * unit_price) AS stddev_pop_amount,
  VAR_POP(qty * unit_price) AS var_pop_amount
FROM sales;
```

## 5. 実務で頻出の集計パターン

### 5-1. 月次KPI（売上、平均、ばらつき）
```sql
SELECT
  DATE_FORMAT(sold_at, '%Y-%m') AS ym,
  SUM(qty * unit_price) AS sales_total,
  AVG(qty * unit_price) AS sales_avg,
  STDDEV_SAMP(qty * unit_price) AS sales_stddev,
  COUNT(*) AS tx_count
FROM sales
GROUP BY DATE_FORMAT(sold_at, '%Y-%m')
ORDER BY ym;
```

### 5-2. 商品別の売上構成比
```sql
WITH by_product AS (
  SELECT
    product_id,
    SUM(qty * unit_price) AS product_sales
  FROM sales
  GROUP BY product_id
)
SELECT
  product_id,
  product_sales,
  ROUND(
    product_sales / SUM(product_sales) OVER (),
    4
  ) AS sales_ratio
FROM by_product
ORDER BY product_sales DESC;
```

## 6. ウィンドウ関数との組み合わせ

### 6-1. 日次累積売上
```sql
WITH daily AS (
  SELECT
    DATE(sold_at) AS sold_date,
    SUM(qty * unit_price) AS daily_sales
  FROM sales
  GROUP BY DATE(sold_at)
)
SELECT
  sold_date,
  daily_sales,
  SUM(daily_sales) OVER (ORDER BY sold_date) AS cumulative_sales
FROM daily
ORDER BY sold_date;
```

### 6-2. 店舗内ランキング
```sql
SELECT
  store_id,
  product_id,
  SUM(qty * unit_price) AS product_sales,
  DENSE_RANK() OVER (
    PARTITION BY store_id
    ORDER BY SUM(qty * unit_price) DESC
  ) AS sales_rank_in_store
FROM sales
GROUP BY store_id, product_id;
```

## 7. 代表的な統計・集計関数の使い分け
- 件数確認: `COUNT(*)`
- 非NULL件数: `COUNT(col)`
- 合計: `SUM(col)`
- 平均: `AVG(col)`
- ばらつき（標本）: `STDDEV_SAMP(col)`, `VAR_SAMP(col)`
- ばらつき（母集団）: `STDDEV_POP(col)`, `VAR_POP(col)`

## 8. 注意点（MySQL実務）
- `WHERE` は集計前、`HAVING` は集計後に適用される。
- `AVG(INT列)` は小数を返すが、表示桁は `ROUND` で明示する。
- 0除算の可能性がある比率計算は `NULLIF` を使う。

```sql
SELECT
  SUM(qty) / NULLIF(COUNT(*), 0) AS avg_qty_safe
FROM sales;
```

## 9. 用語リファレンスガイド
- 集計関数: 複数行を1値に圧縮する関数（`SUM`, `AVG`, `COUNT` など）。
- 統計関数: 分散や標準偏差など分布の特徴を計算する関数。
- グループ化: 同じキーを持つ行をまとめて集計する操作（`GROUP BY`）。
- 標本分散: 標本データから母集団分散を推定する分散（分母は $n-1$）。
- 母分散: 母集団全体に対する分散（分母は $n$）。
- ウィンドウ関数: 行を減らさずに集計結果を付与する関数（`OVER` 句）。

## 10. 句と関数の概要早見表

| キーワード/式 | 何をするか | 使う場面 | 例 |
|---|---|---|---|
| `GROUP BY DATE(sold_at)` | 日時を日単位に丸めてグループ化する | 日次集計を作るとき | `GROUP BY DATE(sold_at)` |
| `GROUP BY DATE_FORMAT(sold_at, '%Y-%m')` | 日時を月単位文字列に変換して集計する | 月次KPIを作るとき | `GROUP BY DATE_FORMAT(sold_at, '%Y-%m')` |
| `HAVING` | 集計後の結果に条件をかける | 「合計が一定以上」などで絞るとき | `HAVING SUM(amount) >= 100000` |
| `PARTITION BY store_id` | ウィンドウ関数の計算対象を店舗ごとに分割する | 店舗ごとの順位・累積を出すとき | `DENSE_RANK() OVER (PARTITION BY store_id ORDER BY sales DESC)` |
| `OVER (ORDER BY sold_date)` | ウィンドウ関数の計算順序を指定する | 累積売上や移動平均を時系列で計算するとき | `SUM(daily_sales) OVER (ORDER BY sold_date)` |
| `ORDER BY` | 最終結果の表示順を並べ替える | 日付順、売上降順で見たいとき | `ORDER BY sold_date` |
| `WITH ... AS (...)` | サブクエリに名前を付けて再利用する（CTE） | 集計を段階的に読みやすく書くとき | `WITH daily AS (...) SELECT ... FROM daily` |
| `COUNT(col)` と `COUNT(*)` | `COUNT(col)` はNULLを除外、`COUNT(*)` は全行を数える | 欠損を含む列の件数確認 | `COUNT(qty)`, `COUNT(*)` |

補足:
- `GROUP BY` は行数を減らして集約する。
- `PARTITION BY` は行数を減らさず、区切り単位でウィンドウ計算する。
