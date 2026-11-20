import pandas as pd


def 정제(df: pd.DataFrame) -> pd.DataFrame:
    정제_df = df.copy()

    # 점수가 비어 있는 행을 삭제한다.
    정제_df = 정제_df.dropna(subset=["점수"])
    print(f"점수 결측 행 삭제 후: {len(정제_df)}행")

    # 모든 열의 값이 같은 중복 행을 하나만 남긴다.
    정제_df = 정제_df.drop_duplicates()
    print(f"중복 행 삭제 후: {len(정제_df)}행")

    # 반과 과목 값의 앞뒤 공백을 제거한다.
    정제_df["반"] = 정제_df["반"].str.strip()
    정제_df["과목"] = 정제_df["과목"].str.strip()
    print(f"공백 제거 후: {len(정제_df)}행")

    # 점수가 0~100 범위를 벗어난 행을 삭제한다.
    정제_df = 정제_df[(정제_df["점수"] >= 0) & (정제_df["점수"] <= 100)]
    print(f"점수 범위 확인 후: {len(정제_df)}행")

    return 정제_df

df = 정제(pd.read_csv("scores_2026.csv"))
print(sorted(df["반"].unique()))
print(sorted(df["과목"].unique()))
정제_df = df[df["과목"] == "수학"]
print(len(정제_df))
정제_df = 정제_df[(정제_df["반"] == "1반") & (정제_df["점수"] >= 90)]

반별_평균 = df.groupby("반")["점수"].mean()
print(반별_평균)

과목_반별_평균 = df.groupby(["과목", "반"])["점수"].mean()
print(과목_반별_평균)

def 반별평균(df):
    통계표 = df.groupby("반")["점수"].agg(
        개수="count",
        평균="mean",
        중앙값="median",
        최댓값="max"
    ).round(2)

    print(통계표)
    return 통계표["평균"]


반별평균(df)

print(df.groupby("반")["점수"].sum().sum())
print(df["점수"].sum())

print(df.groupby("반")["점수"].count().sum())
print(len(df))

print(df[(df["반"] == "1반") & (df["과목"] == "수학")]["점수"])

미니 = 정제(pd.read_csv("mini.csv"))
print( 반별평균( 미니))