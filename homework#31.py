import re

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline : 28/02/2022."

result = re.finditer(r"(\d{2}/\d{2}/\d{4}|\d{2}.\d{2}.\d{4}|\d{2}-\d{2}-\d{4})", text)

for res in result:
    print(res.group())



# ----------------------------------------


tag_input = "python, data-science / machine-learning; AI neural-networks"

data = re.split(r"[,\s/;]+", tag_input)
data1 = re.findall(r"[^,\s/;]+", tag_input)
print(data)
print(data1)
