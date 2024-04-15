def メールテンプレート作成(名前, 挨拶文章):
    """
    メールのテンプレートを作成する関数 📧
    
    引数:
    - 名前: 宛先の名前 (str)
    - 挨拶文章: メールの冒頭の挨拶文 (str)
    
    返り値:
    - メールテンプレート (str)
    """
    
    メールテンプレ = f"""
件名: 【重要】新サービスのお知らせ

{名前} 様

{挨拶文章}

この度、新サービス「AIアシスタント」のリリースが決定いたしましたので、お知らせいたします。

"""
    
    return メールテンプレ

# 関数の使用例 🌟
名前リスト = ["佐藤", "鈴木", "高橋", "田中", "伊藤", "渡辺", "山本", "中村", "小林", "加藤", 
          "吉田", "山田", "佐々木", "山口", "松本", "井上", "木村", "林", "斎藤", "清水"]

挨拶文章 = """
平素より大変お世話になっております。
"""

# 名前リストの各名前に対してループ処理を行う 🔁
for 名前 in 名前リスト:
    メールテンプレ = メールテンプレート作成(名前, 挨拶文章)
    print(メールテンプレ)

書き出す = print


書き出す(メールテンプレ)