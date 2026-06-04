"""Tests for Nous E6 Temperature and Humidity sensor."""

import pytest
from zhaquirks.tuya.ts0601_sensor_nous_e6 import NousE6_TZE284_wtikaxzs
import zhaquirks.const as data_const

def test_signature(assert_signature_matches_quirk):
    """Test that the quirk matches the signature."""
    signature = {
        "node_descriptor": "NodeDescriptor(logical_type=<LogicalType.EndDevice: 2>, manufacturer_code=4417)",
        "endpoints": {
            "1": {
                "profile_id": 0x0104,
                "device_type": 0x0051,
                "in_clusters": [0x0000, 0x0004, 0x0005, 0xEF00],
                "out_clusters": [0x000a, 0x0019],
            }
        },
        "manufacturer": "_TZE284_wtikaxzs",
        "model": "TS0601",
    }
    assert_signature_matches_quirk(NousE6_TZE284_wtikaxzs, signature)
