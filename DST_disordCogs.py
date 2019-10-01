from dst_co import Code
from dst_template_generator import Template_Gen
import json

_int = Template_Gen(code=Code.search(name="로젠택배"), dst_code="95101121253")
result = _int.generate()
print(json.dumps(result, indent=4, ensure_ascii=False))