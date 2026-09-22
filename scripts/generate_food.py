import json
import random
import time
from pathlib import Path
from urllib.request import Request, urlopen

HOST = "http://127.0.0.1:8188"
ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "workflows" / "flux1-schnell-food-api.json"

PROMPT = (
    "A photorealistic editorial food photograph of a thick-cut pork chop, bone-in, "
    "pan-seared with a deeply browned mahogany crust and a warm blush-pink center, "
    "resting on a shallow matte ivory ceramic plate. A small pool of glossy cider "
    "pan sauce gathers beneath the chop, with visible reduction streaks; charred "
    "apple wedges sit at the bone, and three sage leaves are placed irregularly. "
    "Show crisp rendered fat, fine muscle grain at the cut face, tiny black pepper "
    "flecks, and a few coarse salt crystals. The plate sits on dark walnut with a "
    "loosely folded oatmeal linen napkin at the rear right. Large soft window light "
    "from camera left, slightly warm, with a gentle specular edge on the sauce and "
    "dense but open contact shadows. Shot three-quarter overhead at 55mm, f/4, "
    "focus on the cut face and front crust, background falling softly out of focus. "
    "Natural asymmetry, restrained editorial color grade, realistic moisture, "
    "believable reflections, subtle imperfections, no extra garnish."
)
NEGATIVE = "illustration, CGI, plastic food, waxy texture, floating objects, duplicated utensils, unreadable text, oversaturated colors, harsh HDR, extreme bokeh"


def post(path, payload):
    data = json.dumps(payload).encode()
    req = Request(HOST + path, data=data, headers={"Content-Type": "application/json"})
    with urlopen(req, timeout=30) as response:
        return json.loads(response.read())


def main():
    workflow = json.loads(WORKFLOW.read_text(encoding="utf-8"))
    workflow["6"]["inputs"]["text"] = PROMPT
    workflow["7"]["inputs"]["text"] = NEGATIVE
    workflow["3"]["inputs"]["seed"] = random.randrange(1, 2**63 - 1)
    client_id = f"food-lab-{int(time.time())}"
    result = post("/prompt", {"prompt": workflow, "client_id": client_id})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
