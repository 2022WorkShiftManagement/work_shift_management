# 選択するカラーを取得
def get_color(key=None):
    color = {
        "FF0000": "レッド",
        "FF3399": "ピンク",
        "FF9100": "オレンジ",
        "FFD400": "イエロー",
        "008000": "グリーン",
        "B2D235": "イエローグリーン",
        "67A7CC": "スカイブルー",
        "0067C0": "ブルー",
        "5F4894": "パープル",
        "717375": "グレー"
    }

    if key:
        return color[key]

    return color
