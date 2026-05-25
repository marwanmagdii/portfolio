import re

with open('certifications.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The current broken pattern is:
# onclick="openModal('Balanced Business Model', 'Eyouth', 'Aug 2023', '[&quot;...&quot;]'), 'assets/certifications/Balanced Business Model Eyouth.pdf')>More</button>
# We need to fix it to:
# onclick="openModal('Balanced Business Model', 'Eyouth', 'Aug 2023', '[&quot;...&quot;]', 'assets/certifications/Balanced Business Model Eyouth.pdf')">More</button>

def fix_onclick(match):
    # Group 1: onclick="openModal(...
    # Group 2: )
    # Group 3: , 'assets/...')
    prefix = match.group(1)
    assets_part = match.group(3)
    
    # We want: prefix + assets_part + '"'
    # Wait, assets_part has a closing parenthesis. We just need to append the quote at the end.
    return f"{prefix}{assets_part}\""

# We're matching everything from onclick="openModal( up to the wrong parenthesis, then the rest.
bad_pattern = re.compile(r'(onclick="openModal\([^)]+)(\))(, \'assets[^\']+\'\))')
content = bad_pattern.sub(fix_onclick, content)

with open('certifications.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed onclick syntax bug.')
