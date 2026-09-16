import sounddevice as sd
from faster_whisper import WhisperModel

model = WhisperModel("small",device="cpu", compute_type="int8")

SAMPLE_RATE = 16000
DURATION = 8

print("Speak...")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32"
)

sd.wait()

segments, info = model.transcribe(
    audio[:, 0],
    language="en",
    vad_filter=True,
    beam_size=5
    )

text = "".join(segment.text for segment in segments).strip()

print("You said:", text)