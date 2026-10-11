from pathlib import Path
import re

p=Path("public/index.html")
s=p.read_text(encoding="utf-8")

def get_section(text, section_id):
    pattern=rf'<section class="section [^"]*" id="{re.escape(section_id)}">.*?</section>'
    m=re.search(pattern,text,flags=re.S)
    if not m:
        raise SystemExit(f"Missing section: {section_id}")
    return m.group(0)

# Desired story:
# empathy -> why -> reach -> stock/AI -> Instagram×Google -> services
# -> results -> partners -> samples -> compare -> pricing -> other -> about -> cta

reach=get_section(s,"reach-design")
stock=get_section(s,"ai")
# Ensure reach appears before stock.
if s.find(stock) < s.find(reach):
    start=min(s.find(stock),s.find(reach))
    end=max(s.find(stock)+len(stock),s.find(reach)+len(reach))
    between=s[start:end]
    # only reorder these two section blocks; preserve whitespace minimally
    s=s[:start]+reach+"\n"+stock+s[end:]

results=get_section(s,"results")
tools=get_section(s,"tools")
# Ensure results appears before tools.
if s.find(tools) < s.find(results):
    start=min(s.find(tools),s.find(results))
    end=max(s.find(tools)+len(tools),s.find(results)+len(results))
    s=s[:start]+results+"\n"+tools+s[end:]

p.write_text(s,encoding="utf-8")

# Validate relative order.
ids=["empathy","why","reach-design","ai","dual-platform","services","results","tools","samples","compare","pricing","other-services","contact"]
positions=[]
for section_id in ids:
    pos=s.find(f'id="{section_id}"')
    if pos < 0:
        raise SystemExit(f"Missing ordered section: {section_id}")
    positions.append(pos)
if positions != sorted(positions):
    raise SystemExit(f"Story order invalid: {list(zip(ids,positions))}")
