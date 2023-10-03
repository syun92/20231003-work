from math import ceil

""" タクシーの運賃計算
    タクシーの運賃を計算するコードを作成せよ
    * 初乗り運賃は 1700m までは610円とする
    * 1700mを超えるとその後は 315m毎に 80円増えるものとする
    * 引数として走行距離(整数でm単位)が渡されるものとする
    * 戻り値は金額(整数値)とする
    * 1mでも超えれば80円単位でかかるものとする
    * 0mおよびマイナスの場合はNoneを返す
    # 初乗りの距離までは定額610円
    min = 610 # 初乗り運賃
    assert calc_account(1000) == min
    assert calc_account(1700) == min
    assert calc_account(1701) == 690 # 1mでも超えれば増える
    assert calc_account(2015) == 690
    assert calc_account(2016) == 770
    assert calc_account(0) == None
    assert calc_account(-10) == None
"""

def calc_account(m):
    if m <= 0:
        # 0mおよびマイナスの場合
        return None
    elif 1700 < m:
        # 1700を超えた場合
        extension_kyori = m - 1700
        extension_round = ceil(extension_kyori / 315)
        extension_money = extension_round * 80 + 610
        return extension_money
    else:
        # 1700までの場合
        return 610

if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


