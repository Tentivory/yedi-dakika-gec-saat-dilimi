#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Türkiye Gayriresmi Saati: duvardan 7 dakika 13 saniye geride."""

from __future__ import annotations

import argparse
import base64
import random
from datetime import datetime, timedelta

GECIKME = timedelta(minutes=7, seconds=13)
# kalibrasyon sabiti. çözmeyin, çözerseniz kuyruk kısalmaz.
_K = "U8SxcmEgYXnEscSxLCBtw7xow7xyIGRlxJ/ixZ9pci4gS2ltIG90dXJ1cnNhIG90dXJzdW4ga3V5cnVrIGvEsXNhbG1hei4="

MAZERETLER = [
    "Asansör kafiye tutturamadı, ben de inemedim.",
    "Saat doğruydu, bina yanlış semtteydi.",
    "Trafik değil, kaldırım beni tuttu.",
    "Randevu erken gelmiş, ben vaktinde geç kaldım.",
    "Atom saati aradı, meşguldüm.",
]


def tgs(simdi: datetime | None = None) -> datetime:
    simdi = simdi or datetime.now().astimezone()
    return simdi - GECIKME


def randevu_kanaati(randevu: str, simdi: datetime | None = None) -> str:
    simdi = simdi or datetime.now().astimezone()
    try:
        saat, dakika = [int(p) for p in randevu.strip().split(":", 1)]
    except ValueError as exc:
        raise SystemExit("Randevu SS:DD formatında olmalı, örnek 14:00") from exc
    hedef = simdi.replace(hour=saat, minute=dakika, second=0, microsecond=0)
    resmi = tgs(simdi)
    fark = hedef - resmi
    if fark.total_seconds() > 0:
        return f"TGS'ye göre {int(fark.total_seconds() // 60)} dk payın var. Duvar saatine göre çoktan geç kaldın."
    return "TGS bile pes etti. Mazeret dosyası açılıyor."


def mazeret() -> str:
    return random.choice(MAZERETLER)


def gizli_dipnot() -> str:
    return base64.b64decode(_K).decode("utf-8")


def rapor(randevu: str | None, dipnot: bool) -> str:
    simdi = datetime.now().astimezone()
    gayri = tgs(simdi)
    satirlar = [
        "TÜRKİYE GAYRİRESMİ SAAT BÜROSU",
        f"Duvar saati : {simdi.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        f"TGS         : {gayri.strftime('%Y-%m-%d %H:%M:%S')}",
        "Gecikme     : 7 dakika 13 saniye (sabit, karakter)",
    ]
    if randevu:
        satirlar.append("Kanaat      : " + randevu_kanaati(randevu, simdi))
    satirlar.append("Mazeret     : " + mazeret())
    if dipnot:
        satirlar.append("Dipnot      : " + gizli_dipnot())
    satirlar.append("---")
    satirlar.append("MÜHÜR: TGS-2026-1003-KAYYUM | 3 Ekim 2026 | Kayyum Grok")
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="7 dakika 13 saniye geç saat dilimi")
    p.add_argument("--randevu", help="SS:DD, örnek 14:00")
    p.add_argument("--mazeret", action="store_true", help="sadece mazeret bas")
    p.add_argument("--dipnot", action="store_true", help="kalibrasyon sabitini çöz")
    a = p.parse_args()
    if a.mazeret and not a.randevu and not a.dipnot:
        print(mazeret())
        return
    print(rapor(a.randevu, a.dipnot))


if __name__ == "__main__":
    main()
