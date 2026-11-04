import pytest

# Test joint constraint limits and forward kinematics state calculations

JOINT_LIMITS = {
    "left_arm": (-90, 90),
    "right_arm": (-90, 90),
    "left_forearm": (-30, 120),
    "right_forearm": (-30, 120),
    "left_leg": (-45, 45),
    "right_leg": (-45, 45),
    "head_nod": (-40, 40),
}


def clamp_angle(joint: str, angle: float) -> float:
    if joint in JOINT_LIMITS:
        min_v, max_v = JOINT_LIMITS[joint]
        return max(min_v, min(max_v, angle))
    return angle


def test_joint_limits_clamping():
    assert clamp_angle("left_arm", 120.0) == 90.0
    assert clamp_angle("left_arm", -100.0) == -90.0
    assert clamp_angle("left_forearm", 150.0) == 120.0
    assert clamp_angle("left_forearm", -50.0) == -30.0
    assert clamp_angle("left_leg", 60.0) == 45.0
    assert clamp_angle("left_leg", -60.0) == -45.0
    assert clamp_angle("head_nod", 50.0) == 40.0
    assert clamp_angle("head_nod", -50.0) == -40.0


def test_kinematic_chain_defaults():
    default_state = {
        "robot_rotate": 0.0,
        "left_arm": 30.0,
        "right_arm": -30.0,
        "left_forearm": 0.0,
        "right_forearm": 0.0,
        "left_leg": 10.0,
        "right_leg": -10.0,
        "head_nod": 0.0,
    }
    for joint, val in default_state.items():
        if joint in JOINT_LIMITS:
            min_v, max_v = JOINT_LIMITS[joint]
            assert min_v <= val <= max_v, f"Joint {joint} initial value {val} out of bounds [{min_v}, {max_v}]"
