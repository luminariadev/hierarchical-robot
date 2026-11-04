# Hierarchical 3D Robot Kinematics Simulator

[![CI](https://github.com/luminariadev/hierarchical-robot/actions/workflows/ci.yml/badge.svg)](https://github.com/luminariadev/hierarchical-robot/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenGL](https://img.shields.io/badge/OpenGL-5586A4?logo=opengl&logoColor=white)](https://www.opengl.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive 3D articulated robot simulation implementing hierarchical forward kinematics and transformation matrix stacks (`glPushMatrix` / `glPopMatrix`) via PyOpenGL and GLUT.

---

## Kinematic Hierarchy Tree

Transformations applied to parent joints propagate downward through child joints according to standard skeletal matrix nesting:

```
World Origin
     │
     ▼
[Torso Base] (Global Translation & Y-Axis Rotation)
     ├────────────────────────┬────────────────────────┬────────────────────────┐
     ▼                        ▼                        ▼                        ▼
  [Head]                [Left Shoulder]          [Right Shoulder]             [Hips]
(Pitch Nod: ±40°)             │                        │                        │
                              ▼                        ▼            ┌───────────┴───────────┐
                        [Upper Arm]              [Upper Arm]        ▼                       ▼
                        (Pitch: ±90°)            (Pitch: ±90°)  [Left Leg]              [Right Leg]
                              │                        │        (Pitch: ±45°)           (Pitch: ±45°)
                              ▼                        ▼
                          [Forearm]                [Forearm]
                        (Bend: -30°~120°)        (Bend: -30°~120°)
```

---

## Keyboard Controls

| Key | Joint / Action | Direction & Range |
| :---: | :--- | :--- |
| `Q` / `A` | **Robot Base** | Rotate entire model Y-axis (continuous) |
| `W` / `S` | **Left Upper Arm** | Pitch elevation ($-90^\circ$ to $+90^\circ$) |
| `E` / `D` | **Right Upper Arm** | Pitch elevation ($-90^\circ$ to $+90^\circ$) |
| `R` / `F` | **Left Forearm** | Elbow bend ($-30^\circ$ to $+120^\circ$) |
| `T` / `G` | **Right Forearm** | Elbow bend ($-30^\circ$ to $+120^\circ$) |
| `Y` / `H` | **Left Leg** | Hip swing ($-45^\circ$ to $+45^\circ$) |
| `U` / `J` | **Right Leg** | Hip swing ($-45^\circ$ to $+45^\circ$) |
| `I` / `K` | **Head** | Pitch nod ($-40^\circ$ to $+40^\circ$) |
| `ESC` | **Application** | Terminate simulator |

Control reference diagram is located in `assets/keyboard_guide.png`.

---

## Project Structure

```
hierarchical-robot/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── assets/
│   └── keyboard_guide.png      # Interactive keybindings schematic
├── tests/
│   └── test_kinematics.py      # Kinematic joint limits verification
├── hierarchical_robot.py       # Main PyOpenGL rendering & matrix loop
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## Quickstart

### 1. Clone Repository

```bash
git clone https://github.com/luminariadev/hierarchical-robot.git
cd hierarchical-robot
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Launch Simulator

```bash
python hierarchical_robot.py
```

*Note for Linux/WSL users: Requires active X11 / Wayland display server (`freeglut3-dev` package).*

---

## Testing

Execute unit tests via pytest:

```bash
pytest tests/ -v
```

CI workflows test compilation and joint constraints automatically on push and pull requests.

---

## License

Distributed under the [MIT](LICENSE) License.
