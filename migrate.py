"""기존 todos.json 데이터를 Supabase로 이전하는 스크립트. 한 번만 실행."""
import json
import ssl
import httpx
from pathlib import Path
from supabase import create_client, ClientOptions

SUPABASE_URL = "https://hcjzaxbgmzbqzyelhzwl.supabase.co"
SUPABASE_KEY = "sb_publishable_nZ3U751JEIKqFE_Xoeq7Dg_993GLjvD"

DATA_FILE = Path(__file__).parent / "data" / "todos.json"

# SSL 검사 없이 연결 (마이그레이션 1회용)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
    options=ClientOptions(httpx_client=httpx.Client(verify=False)),
)

todos = json.loads(DATA_FILE.read_text(encoding="utf-8"))

if todos:
    result = client.table("todos").insert(todos).execute()
    print(f"✅ {len(result.data)}개 항목을 Supabase로 이전했습니다.")
else:
    print("이전할 데이터가 없습니다.")
