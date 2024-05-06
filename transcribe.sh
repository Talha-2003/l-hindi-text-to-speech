#!/bin/bash
for f in *.wav; do
    /snap/bin/whisper-gael.whisper --model small --language Hindi --output_format txt --task transcribe "$f"
done

