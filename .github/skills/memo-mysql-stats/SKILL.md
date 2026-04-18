---
name: memo-mysql-stats
description: "MySQLの統計関数と集計関数を日本語で整理するスキル。AVG、SUM、COUNT、MIN/MAX、分散/標準偏差、GROUP BY、HAVING、ウィンドウ関数のSQL使用例をまとめるときに使う。"
argument-hint: "目的（例: 集計SQL作成、統計指標比較、レポート用クエリ設計）を指定してください"
user-invocable: true
---

# MySQL統計関数・集計関数整理スキル

## このスキルでできること
- MySQLでよく使う集計関数（`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`）の整理
- 統計関数（`STDDEV_SAMP`, `VAR_SAMP` など）の使い分け
- `GROUP BY` / `HAVING` / ウィンドウ関数を含む実用SQL例の提示
- 分析クエリの読みやすい書き方（CTE、命名、丸め処理）の標準化

## 使うタイミング
- ダッシュボード用のKPI集計SQLを作るとき
- 売上やセンサー値などの分布をSQLだけで確認したいとき
- バッチ処理前にSQLで傾向値・ばらつきを確認したいとき

## 進め方
1. 何を1行に集約するか（粒度）を決める。
2. `GROUP BY` キーを確定し、基礎集計を作る。
3. 必要に応じて標準偏差・分散・相関の統計関数を追加する。
4. ウィンドウ関数で累積値や順位を補強する。
5. `HAVING` で集計後条件をかけ、出力用途に合わせて整形する。

## 参照メモ
- [MySQL統計関数と集計関数ガイド](./references/MySQL統計関数と集計関数ガイド.md)
