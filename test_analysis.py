import pandas as pd

from analysis import 정제, 반별평균


정제_df = 정제(pd.read_csv("scores_2026.csv"))
미니_df = 정제(pd.read_csv("mini.csv"))


def test_scores_2026_has_100_rows():
    assert len(정제_df) == 100


def test_class_values_are_1반_and_2반():
    assert set(정제_df["반"].unique()) == {"1반", "2반"}


def test_class_score_sums_equal_total_score_sum():
    반별_합계 = 정제_df.groupby("반")["점수"].sum().sum()
    전체_합계 = 정제_df["점수"].sum()
    assert 반별_합계 == 전체_합계


def test_mini_first_class_average_is_80():
    반별_평균 = 반별평균(미니_df)
    assert 반별_평균["1반"] == 80.0