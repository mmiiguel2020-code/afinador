#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Afinador: lleva cada sample WAV a la nota exacta mas cercana (A4 = 440 Hz).

El paquete se llama `afinador`. La implementacion esta en `__main__.py`
(es el script original, sin cambios de logica).
"""
from .__main__ import (  # noqa: F401
    EXTS,
    FRAME,
    HOP,
    REJECT_CENTS,
    NOTAS,
    nombre_nota,
    tono_del_sample,
    procesar,
    main,
)

__version__ = "1.0.0"
__all__ = [
    "EXTS",
    "FRAME",
    "HOP",
    "REJECT_CENTS",
    "NOTAS",
    "nombre_nota",
    "tono_del_sample",
    "procesar",
    "main",
]
