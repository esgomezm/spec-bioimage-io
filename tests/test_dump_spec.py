from bioimageio.spec.shared import yaml


def test_spec_roundtrip(unet2d_nuclei_broad_any_minor_path):
    from bioimageio.spec import load_raw_model, serialize_raw_model_to_dict

    data = yaml.load(unet2d_nuclei_broad_any_minor_path)
    # monkeypatch: yaml.load already converts timestamp to datetime.datetime, while we serialize it to ISO 8601
    if "timestamp" in data:
        data["timestamp"] = data["timestamp"].isoformat()

    raw_model = load_raw_model(unet2d_nuclei_broad_any_minor_path)

    serialized = serialize_raw_model_to_dict(raw_model)
    assert isinstance(serialized, dict)

    # from pathlib import Path
    # from bioimageio.spec import save_raw_model
    # save_raw_model(raw_model, Path() / "serialized.yml")

    assert serialized == data

    raw_model_from_serialized = load_raw_model(serialized)
    assert raw_model_from_serialized == raw_model

    raw_model_from_serialized_wo_defaults = load_raw_model(serialized)
    assert raw_model_from_serialized_wo_defaults == raw_model
