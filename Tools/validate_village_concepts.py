"""Validate archived bytes, roster geometry and road/estate clearance (stdlib only)."""
from pathlib import Path
import hashlib
import json
import math
import re
import struct
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'References/Targets/Act_I_Village'


def point_distance(p, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = max(0, min(1, ((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy)))
    return math.hypot(p[0]-a[0]-t*dx, p[1]-a[1]-t*dy)


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def intersects(a, b, c, d):
    if max(a[0], b[0]) < min(c[0], d[0]) or max(c[0], d[0]) < min(a[0], b[0]):
        return False
    if max(a[1], b[1]) < min(c[1], d[1]) or max(c[1], d[1]) < min(a[1], b[1]):
        return False
    return cross(a,b,c)*cross(a,b,d) <= 0 and cross(c,d,a)*cross(c,d,b) <= 0


def inside(p, polygon):
    signs = [cross(a,b,p) for a,b in zip(polygon, polygon[1:]+polygon[:1])]
    return all(v >= 0 for v in signs) or all(v <= 0 for v in signs)


entries = json.loads((BASE/'manifest.json').read_text())['entries']
assert len(entries) == 20
for entry in entries:
    p = ROOT/entry['path']
    data = p.read_bytes()
    assert hashlib.sha256(data).hexdigest() == entry['sha256'], p
    assert data[:8] == b'\x89PNG\r\n\x1a\n', p
    assert list(struct.unpack('>II', data[16:24])) == entry['native_dimensions'], p
    assert not entry['modeling_ready'] and not entry['historical_certification']

layout = json.loads((BASE/'Layout/village-layout.json').read_text())
assert sorted(y['id'] for y in layout['yards']) == list(range(1,24))
polygons = []
for yard in layout['yards']:
    a = math.radians(yard['rotation'])
    p = [(yard['x']+u*math.cos(a)-v*math.sin(a), yard['y']+u*math.sin(a)+v*math.cos(a))
         for u,v in layout['yard_polygon_local']]
    polygons.append((yard['id'],p))
    for road in layout['roads']:
        for c,d in zip(road,road[1:]):
            assert not inside(c,p) and not inside(d,p), yard['id']
            for a,b in zip(p,p[1:]+p[:1]):
                assert not intersects(a,b,c,d), yard['id']
                clearance = min(point_distance(a,c,d),point_distance(b,c,d),
                                point_distance(c,a,b),point_distance(d,a,b))
                assert clearance > layout['road_half_width'], (yard['id'],clearance)
for i,p in polygons:
    for j,q in polygons:
        if i >= j:
            continue
        assert not inside(p[0],q) and not inside(q[0],p), (i,j)
        assert not any(intersects(a,b,c,d) for a,b in zip(p,p[1:]+p[:1])
                       for c,d in zip(q,q[1:]+q[:1])), (i,j)
svg = ET.parse(BASE/'Layout/village-terrain-selected.svg')
assert len([e for e in svg.iter() if e.attrib.get('data-key','').startswith('h')]) == 23
for p in [ROOT/'Docs/Art/Act_I_Village_Plan.md', ROOT/'Docs/Art/Village_Concept_Review.md', BASE/'README.md']:
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if '://' not in target and not target.startswith('#'):
            assert (p.parent/target.split('#')[0]).exists(), (p,target)
print('20 native PNG hashes/dimensions; 23 unique nonoverlapping estates; full-width road clearance; SVG count and new document links: passed.')
