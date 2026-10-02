from datetime import datetime, timedelta, timezone
import saat


def test_sabit_gecikme():
    an = datetime(2026, 10, 3, 2, 4, tzinfo=timezone(timedelta(hours=3)))
    assert saat.tgs(an) == an - timedelta(minutes=7, seconds=13)


def test_dipnot_cozulur():
    metin = saat.gizli_dipnot()
    assert "kuyruk" in metin
    assert "mühür" in metin
