import json
import random
from typing import List, Dict, Optional

# JSONファイルのパス
file_path = "text.json"


# 1. ローカルのtext.jsonファイルを読み取り、text属性の値を出力する
def read_json(file_path: str) -> Dict:
    """
    JSONファイルを読み取り、データを辞書として返す。

    Args:
        file_path (str): JSONファイルのパス。

    Returns:
        dict: JSONファイルの内容を辞書として返す。
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    print("text属性の値:", data.get("text", "text属性が見つかりません"))
    return data


# 2. 読み取ったファイルの、users属性に格納されたキーバリューリストを配列に格納（users配列）
def get_users(data: Dict) -> List[Dict]:
    """
    JSONデータからusers属性を取得し、リストとして返す。

    Args:
        data (dict): JSONデータ。

    Returns:
        list: users属性のリスト。
    """
    users = data.get("users", [])
    print("users配列:", users)
    return users


# 3. 指定されたユーザIDとランダムなサイコロの値が一致するか確認
def find_user_by_dice(users: List[Dict], user_id: int) -> Optional[int]:
    """
    ランダムなサイコロの値を生成し、指定されたユーザIDと一致するか確認する。

    Args:
        users (list): ユーザのリスト。
        user_id (int): 確認するユーザID。

    Returns:
        Optional[int]: 一致したユーザID、またはNone。
    """
    dice_roll = random.randint(1, 6)
    print(f"サイコロの結果: {dice_roll}")

    if user_id == dice_roll:
        print("一致したuser_id:", user_id)
        return user_id
    else:
        print("サイコロの値と一致しませんでした。")
        return None


# 4. 一致したuserがinputで文字列を入力し、ファイルのtext属性の値を書き換える
def update_name(data: Dict, user: Optional[int]) -> bool:
    """
    一致したユーザが入力した新しい値でtext属性を更新する。

    Args:
        data (dict): JSONデータ。
        user (Optional[int]): 一致したユーザID。

    Returns:
        bool: 更新が成功した場合はTrue、失敗した場合はFalse。
    """
    if user:
        new_name = input("新しいtextを入力してください: ").strip()
        if not new_name:
            print("入力が空のため、text属性を更新できませんでした。")
            return False
        data["text"] = new_name
        print("text属性が更新されました:", new_name)
        return True
    else:
        print("userが選択されていないため、text属性を更新できません。")
        return False


# 5. ファイルを保存する
def save_json(file_path: str, data: Dict) -> None:
    """
    JSONデータをファイルに保存する。

    Args:
        file_path (str): 保存先のファイルパス。
        data (dict): 保存するJSONデータ。
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("ファイルが保存されました。")


# ユーザが存在するか確認する関数
def validate_user_existence(users: List[Dict], user_id: int) -> Optional[Dict]:
    """
    指定されたユーザIDが存在するか確認する。

    Args:
        users (list): ユーザのリスト。
        user_id (int): 確認するユーザID。

    Returns:
        Optional[dict]: 一致したユーザ情報、またはNone。
    """
    user = next((u for u in users if u.get("id") == user_id), None)
    if not user:
        print("指定されたユーザIDが見つかりませんでした。")
        return None
    return user


# メイン処理
def main() -> None:
    """
    メイン処理を実行する。
    ユーザIDの入力、JSONデータの読み取り、ユーザ確認、
    サイコロの一致確認、text属性の更新、ファイル保存を行う。
    """
    try:
        user_id = int(input("ユーザIDを入力してください: ").strip())
    except ValueError:
        print("無効なユーザIDです。数値を入力してください。")
        return

    data = read_json(file_path)
    users = get_users(data)

    # ユーザの存在確認
    user = validate_user_existence(users, user_id)
    if not user:
        return

    # サイコロの結果と一致するか確認
    user = find_user_by_dice(users, user_id)
    if not update_name(data, user):
        return

    save_json(file_path, data)


if __name__ == "__main__":
    main()
