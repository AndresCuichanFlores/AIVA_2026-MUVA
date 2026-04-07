# =========================
# IMPORTS
# =========================
from alpr_system import ALPRSystem
from pathlib import Path

# =========================
# BLOQUE PRINCIPAL
# =========================
if __name__ == "__main__":
    # Ubicacion del video
    video_path = Path(__file__).resolve().parent.parent / "data" / "videos" / "Video_10.mkv"
    # Iniciamos el sistema ALPR
    ALPR = ALPRSystem()
    ALPR.start_system(str(video_path))
