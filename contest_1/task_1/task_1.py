v_anchor, v_range = map(int, input().split())
m_anchor, m_range = map(int, input().split())

anchors = [v_anchor, m_anchor]
anchors.sort()

if anchors[1] - anchors[0] > v_range + m_range:
    result = (v_range + m_range) * 2 + 2
else:
    min_range = min(v_anchor - v_range, m_anchor - m_range)
    max_range = max(v_anchor + v_range, m_anchor + m_range)
    result = len(range(min_range, max_range + 1))

print(result)
