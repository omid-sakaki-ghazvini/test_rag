from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = "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"
os.environ['OPENAI_API_KEY'] = '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'


docs = [
        'خرابی های مربوط به اتصال 19 ولت:
لبتاپ روشن نمیشه و روی منبع تغذیه ۵امپر می‌کشد چیکار باید کنم؟ جوابش میشه اینکه خرابی در مدار محافظ یا بعد مدار محافظ هستش باید فیوز خروجی رو برداره ببینید اتصالی از کدوم سمت هست
اگر از مدار محافظ باشه جک آداپتور یا قطعات مدار محافظ باشد  اگر مشکل از بعد از مدار محافظ باشد همه جاهایی که ۱۹ولت رفته باشه می‌تونه باعث اتصالی باشه باید تست دیودی خروجی مدار محافظ رو بگیریم و با تست دیودی تک تک سلف ها با کنفی مدار مقایسه کنیم اون سلفی که عدد یکسان نشون میده خرابی از اون مدار هست عدد صفر  بیشترین خرابی از خازن های مدار سی پی یو و گرافیک هست عدد نزدیک صفر ماسفت های مدار سی پی یو گرافیک یا رم می باشد
دو طرف تست عدد یکسان از ماسفت های مدار شارژ یا مدار پاور می باش'
       ]
