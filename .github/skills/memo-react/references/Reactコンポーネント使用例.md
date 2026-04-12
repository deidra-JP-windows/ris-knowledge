# Reactコンポーネント使用例

## 目的
- Reactでよく使うコンポーネントとAPIの最小実装例を、参照しやすい形でまとめる。

## 使用例一覧

| 種類 | 何ができるか | 最小コード例 |
|---|---|---|
| 関数コンポーネント | `props`を受け取りUIを描画 | `function UserCard({ name }) { return <p>{name}</p>; }` |
| ローカル状態 (`useState`) | 入力値や開閉状態などを保持 | `const [open, setOpen] = useState(false);` |
| 副作用 (`useEffect`) | データ取得、購読、タイマー処理 | `useEffect(() => { fetchData(); }, []);` |
| 条件付き表示 | 状態に応じて表示を切り替え | `{loading ? <Spinner /> : <List />}` |
| リスト描画 | 配列データを反復表示 | `{items.map((item) => <li key={item.id}>{item.name}</li>)}` |
| 親子通信 (コールバック) | 子から親へイベント通知 | `<Child onSave={handleSave} />` |
| Context (`useContext`) | 全体でテーマ/認証情報を共有 | `const theme = useContext(ThemeContext);` |
| メモ化 (`React.memo`) | 不要な再レンダリングを抑制 | `const Row = memo(function Row({ value }) { ... });` |
| 遅延読み込み (`lazy` + `Suspense`) | 初期ロードを軽量化 | `<Suspense fallback={<p>loading...</p>}><Page /></Suspense>` |
| エラー境界 | 例外時に代替UIを表示 | `<ErrorBoundary><App /></ErrorBoundary>` |

## 実装サンプル

### 1. 関数コンポーネント + `props`

- このコンポーネントは、親から受け取ったデータをそのまま描画できる。

```tsx
export function UserCard({ name }: { name: string }) {
  return <p>{name}</p>;
}
```

### 2. `useState` で開閉状態を管理

- このコンポーネントは、クリック操作に応じて表示/非表示を切り替えて描画できる。

```tsx
import { useState } from "react";

export function TogglePanel() {
  const [open, setOpen] = useState(false);

  return (
    <section>
      <button onClick={() => setOpen((prev) => !prev)}>
        {open ? "閉じる" : "開く"}
      </button>
      {open && <p>パネルの内容</p>}
    </section>
  );
}
```

### 3. `useEffect` で初回データ取得

- このコンポーネントは、初回表示時にAPIからデータを取得し、loading/error/success を描き分けできる。

```tsx
import { useEffect, useState } from "react";

type User = { id: number; name: string };

export function UserList() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;

    async function loadUsers() {
      try {
        const response = await fetch("/api/users");
        if (!response.ok) throw new Error("failed to fetch users");
        const data = (await response.json()) as User[];
        if (active) setUsers(data);
      } catch {
        if (active) setError("ユーザー取得に失敗しました");
      } finally {
        if (active) setLoading(false);
      }
    }

    loadUsers();
    return () => {
      active = false;
    };
  }, []);

  if (loading) return <p>loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### 4. Contextで全体テーマを参照

- このコンポーネントは、ツリー上位の共有値（テーマなど）を受け取って一貫した見た目を描画できる。

```tsx
import { createContext, useContext } from "react";

const ThemeContext = createContext("light");

function Header() {
  const theme = useContext(ThemeContext);
  return <header data-theme={theme}>Header</header>;
}

export function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Header />
    </ThemeContext.Provider>
  );
}
```

### 5. 遅延読み込み

- このコンポーネントは、重い画面を必要時に読み込み、読み込み中UIを描画できる。

```tsx
import { Suspense, lazy } from "react";

const SettingsPage = lazy(() => import("./SettingsPage"));

export function AppRouter() {
  return (
    <Suspense fallback={<p>ページを読み込み中...</p>}>
      <SettingsPage />
    </Suspense>
  );
}
```

## HTMLからの実行起点

Reactの各コンポーネントは、基本的に次の経路で実行される。

1. `index.html` の `div#root` がマウント先になる。
2. `main.tsx` (または `index.tsx`) で `createRoot(...).render(<App />)` を実行する。
3. `App` から子コンポーネントが順に評価・描画される。

```html
<!-- index.html -->
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.tsx"></script>
</body>
```

```tsx
// main.tsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { App } from "./App";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

| コンポーネント | HTMLのどこから実行されるか | 実行のトリガー |
|---|---|---|
| `UserCard` | `index.html` の `#root` にマウントされた `App` 配下で実行 | 親が `<UserCard />` を描画した時 |
| `TogglePanel` | `index.html` の `#root` にマウントされた `App` 配下で実行 | `App` などが `<TogglePanel />` を描画した時 |
| `UserList` | `index.html` の `#root` にマウントされた `App` 配下で実行 | 初回描画時に `useEffect` が走り、状態更新で再描画 |
| `Header` (Context例) | `index.html` の `#root` にマウントされた `App` 配下で実行 | `<ThemeContext.Provider>` 配下で `<Header />` が描画された時 |
| `AppRouter` / `SettingsPage` | `index.html` の `#root` にマウントされた `App` 配下で実行 | `AppRouter` 描画時に `SettingsPage` を遅延ロード |

補足:
- ReactコンポーネントはHTMLから直接呼び出されるのではなく、`#root` を起点にJS/TS側のツリーとして実行される。
- どのコンポーネントも「最終的な入口」は `index.html` の `#root` だが、直接の呼び出し元は親コンポーネントになる。

## AIに指示するときの最小テンプレート

```text
- コンポーネント名: UserList
- 役割: ユーザー一覧を表示し、項目クリックを親に通知
- props: users(User[]), onSelect(userId: number)
- state: loading, error をローカル管理
- 非同期: 初回に /api/users を取得
- UI要件: loading/error/empty/success の4状態を表示
- アクセシビリティ: button に aria-label を付与
```

## 使い分けメモ
- まずは関数コンポーネント + `useState` + `useEffect` を基本にする。
- 状態が複数コンポーネントに散るなら `Context` または状態管理ライブラリを検討する。
- 画面初期表示が重いときは `lazy` + `Suspense` を適用する。
- 再レンダリングが多い箇所にだけ `memo` や `useMemo` を使う。
