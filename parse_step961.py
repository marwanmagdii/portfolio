import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open('step961_raw.json', 'r', encoding='utf-8', errors='ignore') as f:
    data = json.load(f)

# The structure is a log step containing tool_calls
print("keys:", data.keys())
calls = data.get('tool_calls', [])
for i, call in enumerate(calls):
    print(f"Call {i}: name = {call.get('name')}")
    args = call.get('args', {})
    print("  TargetFile:", args.get('TargetFile'))
    print("  Instruction:", args.get('Instruction'))
    # Print replacement chunks or details
    chunks_str = args.get('ReplacementChunks')
    if chunks_str:
        try:
            chunks = json.loads(chunks_str)
            print(f"  Number of chunks: {len(chunks)}")
            for j, chunk in enumerate(chunks):
                print(f"    Chunk {j}: StartLine={chunk.get('StartLine')}, EndLine={chunk.get('EndLine')}")
                print(f"      TargetContent length: {len(chunk.get('TargetContent', ''))}")
                print(f"      ReplacementContent length: {len(chunk.get('ReplacementContent', ''))}")
                # Save chunk files for reference
                with open(f'chunk_{j}_target.txt', 'w', encoding='utf-8') as out:
                    out.write(chunk.get('TargetContent', ''))
                with open(f'chunk_{j}_replacement.txt', 'w', encoding='utf-8') as out:
                    out.write(chunk.get('ReplacementContent', ''))
        except Exception as e:
            print("    Failed parsing chunks:", e)
            # Write raw to check
            with open('raw_chunks.txt', 'w', encoding='utf-8') as out:
                out.write(chunks_str)
