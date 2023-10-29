import sqlite3

# https://zenn.dev/yutabeee/articles/66eeff0ac1de36
def test():
    # データベース接続を作成
    conn = sqlite3.connect('example.db')

    # 分離レベルを 'SERIALIZABLE' に設定
    conn.isolation_level = 'SERIALIZABLE'

    # カーソルを取得
    c = conn.cursor()

    try:
        # トランザクション開始
        c.execute('BEGIN')

        # ここでトランザクションに含まれる一連の操作を実行

        # トランザクション確定（コミット）
        conn.commit()

    except Exception as e:
        # エラーが発生した場合、トランザクションを中断（ロールバック）
        conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        # トランザクション終了
        c.close()
        conn.close()