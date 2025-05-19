import note_seq
from magenta.models.onsets_frames_transcription import infer_util

# Load audio
audio = note_seq.audio_io.load_audio('your_audio.wav', sample_rate=16000)

# Transcribe to NoteSequence (MIDI-like)
note_sequence = infer_util.transcribe_audio(audio)

# Save as MIDI
note_seq.sequence_proto_to_midi_file(note_sequence, 'output.mid')
