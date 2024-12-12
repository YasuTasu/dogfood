from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os
from sqlalchemy import inspect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 食材モデルの定義
class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ENERC_KCAL = db.Column(db.Float, nullable=False)
    WATER = db.Column(db.Float, nullable=False)
    ILE = db.Column(db.Float, nullable=False)
    LEU = db.Column(db.Float, nullable=False)
    LYS = db.Column(db.Float, nullable=False)
    MET = db.Column(db.Float, nullable=False)
    CYS = db.Column(db.Float, nullable=False)
    PHE = db.Column(db.Float, nullable=False)
    TYR = db.Column(db.Float, nullable=False)
    THR = db.Column(db.Float, nullable=False)
    TRP = db.Column(db.Float, nullable=False)
    VAL = db.Column(db.Float, nullable=False)
    HIS = db.Column(db.Float, nullable=False)
    ARG = db.Column(db.Float, nullable=False)
    F18D2N6 = db.Column(db.Float, nullable=False)
    F18D3N3 = db.Column(db.Float, nullable=False)
    F22D6N3 = db.Column(db.Float, nullable=False)
    NAT = db.Column(db.Float, nullable=False)
    K = db.Column(db.Float, nullable=False)
    CA = db.Column(db.Float, nullable=False)
    MG = db.Column(db.Float, nullable=False)
    P = db.Column(db.Float, nullable=False)
    FE = db.Column(db.Float, nullable=False)
    ZN = db.Column(db.Float, nullable=False)
    CU = db.Column(db.Float, nullable=False)
    MN = db.Column(db.Float, nullable=False)
    YO = db.Column(db.Float, nullable=False)
    SE = db.Column(db.Float, nullable=False)
    CR = db.Column(db.Float, nullable=False)
    RETOL = db.Column(db.Float, nullable=False)
    CARTA = db.Column(db.Float, nullable=False)
    CARTB = db.Column(db.Float, nullable=False)
    CRYPXB = db.Column(db.Float, nullable=False)
    CARTBEQ = db.Column(db.Float, nullable=False)
    VITA_RAE = db.Column(db.Float, nullable=False)
    VITD = db.Column(db.Float, nullable=False)
    TOCPHA = db.Column(db.Float, nullable=False)
    TOCPHB = db.Column(db.Float, nullable=False)
    TOCPHG = db.Column(db.Float, nullable=False)
    TOCPHD = db.Column(db.Float, nullable=False)
    THIA = db.Column(db.Float, nullable=False)
    RIBF = db.Column(db.Float, nullable=False)
    NIA = db.Column(db.Float, nullable=False)
    VITB6A = db.Column(db.Float, nullable=False)
    VITB12 = db.Column(db.Float, nullable=False)
    FOL = db.Column(db.Float, nullable=False)
    PANTAC = db.Column(db.Float, nullable=False)
    NACL_EQ = db.Column(db.Float, nullable=False)

# 必要なデータ読み込み関数
def process_excel():
    excel_path = os.path.join(os.path.dirname(__file__), 'ingredients.xlsx')
    if not os.path.exists(excel_path):
        print("Excelファイル(ingredients.xlsx)が存在しません")
        return

    df = pd.read_excel(excel_path, engine='openpyxl')
    inspector = inspect(db.engine)
    if not inspector.has_table('ingredient'):
        db.create_all()

    if Ingredient.query.count() == 0:
        for index, row in df.iterrows():
            try:
                ingredient = Ingredient(
                    name=row["食品名"],
                    ENERC_KCAL=float(row["エネルギー"] if row["エネルギー"] != 'Tr' else 0),
                    WATER=float(row["水分"] if row["水分"] != 'Tr' else 0),
                    ILE=float(row["イソロイシン"] if row["イソロイシン"] != 'Tr' else 0),
                    LEU=float(row["ロイシン"] if row["ロイシン"] != 'Tr' else 0),
                    LYS=float(row["リシン（リジン）"] if row["リシン（リジン）"] != 'Tr' else 0),
                    MET=float(row["メチオニン"] if row["メチオニン"] != 'Tr' else 0),
                    CYS=float(row["シスチン"] if row["シスチン"] != 'Tr' else 0),
                    PHE=float(row["フェニルアラニン"] if row["フェニルアラニン"] != 'Tr' else 0),
                    TYR=float(row["チロシン"] if row["チロシン"] != 'Tr' else 0),
                    THR=float(row["トレオニン（スレオニン）"] if row["トレオニン（スレオニン）"] != 'Tr' else 0),
                    TRP=float(row["トリプトファン"] if row["トリプトファン"] != 'Tr' else 0),
                    VAL=float(row["バリン"] if row["バリン"] != 'Tr' else 0),
                    HIS=float(row["ヒスチジン"] if row["ヒスチジン"] != 'Tr' else 0),
                    ARG=float(row["アルギニン"] if row["アルギニン"] != 'Tr' else 0),
                    F18D2N6=float(row["リノール酸"] if row["リノール酸"] != 'Tr' else 0),
                    F18D3N3=float(row["α‐リノレン酸"] if row["α‐リノレン酸"] != 'Tr' else 0),
                    F22D6N3=float(row["ドコサヘキサエン酸"] if row["ドコサヘキサエン酸"] != 'Tr' else 0),
                    NAT=float(row["ナ ト リ ウ ム"] if row["ナ ト リ ウ ム"] != 'Tr' else 0),
                    K=float(row["カ　リ　ウ　ム"] if row["カ　リ　ウ　ム"] != 'Tr' else 0),
                    CA=float(row["カ ル シ ウ ム"] if row["カ ル シ ウ ム"] != 'Tr' else 0),
                    MG=float(row["マ グ ネ シ ウ ム"] if row["マ グ ネ シ ウ ム"] != 'Tr' else 0),
                    P=float(row["リ　ン"] if row["リ　ン"] != 'Tr' else 0),
                    FE=float(row["鉄"] if row["鉄"] != 'Tr' else 0),
                    ZN=float(row["亜　鉛"] if row["亜　鉛"] != 'Tr' else 0),
                    CU=float(row["銅"] if row["銅"] != 'Tr' else 0),
                    MN=float(row["マ　ン　ガ　ン"] if row["マ　ン　ガ　ン"] != 'Tr' else 0),
                    YO=float(row["ヨ　ウ　素"] if row["ヨ　ウ　素"] != 'Tr' else 0),
                    SE=float(row["セ　レ　ン"] if row["セ　レ　ン"] != 'Tr' else 0),
                    CR=float(row["ク　ロ　ム"] if row["ク　ロ　ム"] != 'Tr' else 0),
                    RETOL=float(row["VA　レチノール"] if row["VA　レチノール"] != 'Tr' else 0),
                    CARTA=float(row["VA　α|カロテン"] if row["VA　α|カロテン"] != 'Tr' else 0),
                    CARTB=float(row["VA　β|カロテン"] if row["VA　β|カロテン"] != 'Tr' else 0),
                    CRYPXB=float(row["VＡ　β|クリプトキサンチン"] if row["VＡ　β|クリプトキサンチン"] != 'Tr' else 0),
                    CARTBEQ=float(row["ＶＡ　β|カロテン当量"] if row["ＶＡ　β|カロテン当量"] != 'Tr' else 0),
                    VITA_RAE=float(row["ＶＡ　レチノール活性当量"] if row["ＶＡ　レチノール活性当量"] != 'Tr' else 0),
                    VITD=float(row["ビタミンD"] if row["ビタミンD"] != 'Tr' else 0),
                    TOCPHA=float(row["VE　α|トコフェロール"] if row["VE　α|トコフェロール"] != 'Tr' else 0),
                    TOCPHB=float(row["VE　β|トコフェロール"] if row["VE　β|トコフェロール"] != 'Tr' else 0),
                    TOCPHG=float(row["VE　γ|トコフェロール"] if row["VE　γ|トコフェロール"] != 'Tr' else 0),
                    TOCPHD=float(row["VE　δ|トコフェロール"] if row["VE　δ|トコフェロール"] != 'Tr' else 0),
                    THIA=float(row["ビタミンＢ１"] if row["ビタミンＢ１"] != 'Tr' else 0),
                    RIBF=float(row["ビタミンB２"] if row["ビタミンB２"] != 'Tr' else 0),
                    NIA=float(row["ナイアシン"] if row["ナイアシン"] != 'Tr' else 0),
                    VITB6A=float(row["ビタミンＢ６"] if row["ビタミンＢ６"] != 'Tr' else 0),
                    VITB12=float(row["ビタミンＢ１２"] if row["ビタミンＢ１２"] != 'Tr' else 0),
                    FOL=float(row["葉　酸"] if row["葉　酸"] != 'Tr' else 0),
                    PANTAC=float(row["パントテン酸"] if row["パントテン酸"] != 'Tr' else 0),
                    NACL_EQ=float(row["食塩相当量"] if row["食塩相当量"] != 'Tr' else 0),
                )
                db.session.add(ingredient)
            except Exception as e:
                print(f"Error processing row {index}: {e}")
        db.session.commit()
        print("データ格納が完了しました！")

def load_aafco_standards():
    aafco_path = os.path.join(os.path.dirname(__file__), 'aafco_standards.xlsx')
    if not os.path.exists(aafco_path):
        print("AAFCO基準値のExcelファイルがありません")
        return {}
    df = pd.read_excel(aafco_path, engine='openpyxl')
    return {row["nutrient"]: row["minimum"] for _, row in df.iterrows()}

aafco_standards = {}

def suggest_ingredients_for_deficiencies(deficiencies):
    suggestions = {}
    for nutrient in deficiencies:
        top_ingredients = (Ingredient.query
                           .order_by(getattr(Ingredient, nutrient).desc())
                           .limit(3)
                           .all())
        suggestions[nutrient] = [(ingredient.name, getattr(ingredient, nutrient)) for ingredient in top_ingredients]
    return suggestions

@app.route('/')
def index():
    ingredients = Ingredient.query.all()
    return render_template('index.html', ingredients=ingredients)

@app.route('/calculate', methods=['POST'])
def calculate():
    selected_ids = request.form.getlist('ingredient_ids')
    if not selected_ids:
        return "食材が選択されていません。"
    
    selected_ids = [int(i) for i in selected_ids]
    selected_ingredients = Ingredient.query.filter(Ingredient.id.in_(selected_ids)).all()

    nutrient_labels = {
        'ENERC_KCAL': ('エネルギー', 'kcal'),
        'WATER': ('水分', 'g'),
        'ILE': ('イソロイシン', 'g'),
        'LEU': ('ロイシン', 'g'),
        'LYS': ('リシン（リジン）', 'g'),
        'MET': ('メチオニン', 'g'),
        'CYS': ('シスチン', 'g'),
        'PHE': ('フェニルアラニン', 'g'),
        'TYR': ('チロシン', 'g'),
        'THR': ('トレオニン（スレオニン）', 'g'),
        'TRP': ('トリプトファン', 'g'),
        'VAL': ('バリン', 'g'),
        'HIS': ('ヒスチジン', 'g'),
        'ARG': ('アルギニン', 'g'),
        'F18D2N6': ('リノール酸', 'g'),
        'F18D3N3': ('α-リノレン酸', 'g'),
        'F22D6N3': ('ドコサヘキサエン酸', 'g'),
        'NAT': ('ナトリウム', 'mg'),
        'K': ('カリウム', 'mg'),
        'CA': ('カルシウム', 'mg'),
        'MG': ('マグネシウム', 'mg'),
        'P': ('リン', 'mg'),
        'FE': ('鉄', 'mg'),
        'ZN': ('亜鉛', 'mg'),
        'CU': ('銅', 'mg'),
        'MN': ('マンガン', 'mg'),
        'YO': ('ヨウ素', 'μg'),
        'SE': ('セレン', 'μg'),
        'CR': ('クロム', 'μg'),
        'RETOL': ('レチノール', 'μg'),
        'CARTA': ('α-カロテン', 'μg'),
        'CARTB': ('β-カロテン', 'μg'),
        'CRYPXB': ('クリプトキサンチン', 'μg'),
        'CARTBEQ': ('カロテン当量', 'μg'),
        'VITA_RAE': ('レチノール活性当量', 'μg'),
        'VITD': ('ビタミンD', 'μg'),
        'TOCPHA': ('α-トコフェロール', 'mg'),
        'TOCPHB': ('β-トコフェロール', 'mg'),
        'TOCPHG': ('γ-トコフェロール', 'mg'),
        'TOCPHD': ('δ-トコフェロール', 'mg'),
        'THIA': ('ビタミンB1', 'mg'),
        'RIBF': ('ビタミンB2', 'mg'),
        'NIA': ('ナイアシン', 'mg'),
        'VITB6A': ('ビタミンB6', 'mg'),
        'VITB12': ('ビタミンB12', 'μg'),
        'FOL': ('葉酸', 'μg'),
        'PANTAC': ('パントテン酸', 'mg'),
        'NACL_EQ': ('食塩相当量', 'g')
    }

    totals = {nutrient: 0 for nutrient in nutrient_labels.keys()}
    selected_list = []

    total_grams = 0  # 初期化
    for ingredient in selected_ingredients:
        grams = float(request.form.get(f'grams_{ingredient.id}', 0))
        if grams > 0:
            selected_list.append((ingredient.name, grams))
            total_grams += grams  # 合計グラム数を計算
            for nutrient in nutrient_labels.keys():
                nutrient_value = getattr(ingredient, nutrient, 0)
                totals[nutrient] += nutrient_value * (grams / 100)

    result_symbols = {}
    for nutrient, total_val in totals.items():
        if nutrient in aafco_standards:
            if total_val >= aafco_standards[nutrient]:
                result_symbols[nutrient] = "○"
            else:
                result_symbols[nutrient] = "×"
        else:
            result_symbols[nutrient] = "-"

    deficiencies = [nutrient for nutrient, symbol in result_symbols.items() if symbol == "×"]
    suggestions = suggest_ingredients_for_deficiencies(deficiencies)

    return render_template('calculate.html',
                           totals=totals,
                           nutrient_labels=nutrient_labels,
                           selected_list=selected_list,
                           total_grams=total_grams,  # 合計グラム数をテンプレートに渡す
                           result_symbols=result_symbols,
                           suggestions=suggestions)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if Ingredient.query.count() == 0:
            process_excel()
        aafco_standards = load_aafco_standards()

    # $PORT環境変数を使用
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
