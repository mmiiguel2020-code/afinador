# afinador

Afina samples WAV a la **nota exacta más cercana** (temperamento igual, A4 = 440 Hz
por defecto) **cambiando el tono de verdad en el audio**, remuestreando.

Pensado para muestras de instrumento (una nota por archivo), como las de un
acordeón, antes de meterlas en un SoundFont o en un sampler.

## Qué hace

```
entrada:  samb11.wav   64,88 Hz   (Do2 −14,0 cents)
salida:   samb11.wav   65,41 Hz   (Do2   0,0 cents)
```

1. **Detecta el tono** con `librosa.pyin` en dos pasadas:
   - gruesa, de C2 a C7, resolución 10 cents
   - fina, ±2 semitonos alrededor del resultado, resolución 1 cent
2. **Descarta los cuadros sin energía** (por debajo de −25 dB del máximo), para
   no medir colas ni ruido.
3. **Descarta errores de octava** (desviaciones de más de 300 cents sobre la
   mediana).
4. **Remuestrea** el audio al tono objetivo (`soxr_hq`).

El remuestreo es real, como subir o bajar la velocidad de un sampler: la
**duración cambia hasta un 3 %** para correcciones de 50 cents.

## Instalación

```bash
python3 -m venv ~/venvs/afinador
~/venvs/afinador/bin/pip install -e ~/afinador
```

O sin instalar, usando el script directamente:

```bash
pip install numpy scipy soundfile librosa
python3 src/afinador/__main__.py CARPETA_ENTRADA CARPETA_SALIDA
```

## Uso

```bash
# afinar una carpeta entera a otra carpeta
afinador carpeta_entrada carpeta_salida

# un solo archivo
afinador sample.wav carpeta_salida

# SOLO medir, sin escribir nada
afinador carpeta_entrada /tmp/loquesea --solo-reportar

# con otro diapasón (por ejemplo 442 Hz)
afinador entrada salida --a4 442
```

### Opciones

| Opción | Qué hace |
|---|---|
| `--a4` | Frecuencia de La4 en Hz (por defecto `440`) |
| `--solo-reportar` | Mide y muestra, pero **no escribe archivos** |

### Formatos

Entrada: `.wav`, `.flac`, `.aif`, `.aiff`.
Salida: WAV, con el **mismo subtipo** que la entrada (si es válido), si no `PCM_24`.

## Salida típica

```
samb11.wav  (48000 Hz, 1 canal(es), 1.94 s)
  detectado: 64.88 Hz = Do2 -14.0 cents  (objetivo 65.41 Hz)
  correccion: +14.0 cents, duracion 1.008x
  -> /ruta/salida/samb11.wav
```

## Verificación

Sobre 59 muestras de acordeón (`sambucles`):

```
desvío corregido:   de −49 a +38 cents  (media −15,9)
desvío residual:    máximo 1,00 cent  ·  medio 0,05 cents
archivos:           59 · 0 errores · 0 sin detectar
```

## Limitaciones

- **Una nota por archivo.** No separa acordes ni polifonía.
- **La duración cambia** al remuestrear. Si necesitas conservarla, hay que
  estirar en vez de remuestrear (otro algoritmo, que mete artefactos).
- Se apoya en la **mediana** del tono: en muestras con mucho vibrato o glissando
  afin ará la mediana, no la nota base.
- El detector puede equivocarse **de octava** en graves con armónicos fuertes;
  el filtro de 300 cents lo cubre en parte, no del todo.

## Estructura

```
afinador/
  src/afinador/
    __init__.py     importa lo publico
    __main__.py     la implementacion (script original)
  docs/
    INTERIORIDADES.md   por que hace lo que hace
  pyproject.toml
  README.md
```

## Licencia

MIT.
