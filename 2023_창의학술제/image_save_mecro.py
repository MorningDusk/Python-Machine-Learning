import requests
import os

with open("C:/Users/user/python_machine_learning/2023_창의학술제/galclass_finding_list.txt", "r") as f:
    celestial_coordinates = f.readlines()

ra_list = [coordinate.split(" ")[2] for coordinate in celestial_coordinates]
dec_list = [coordinate.split(" ")[3] for coordinate in celestial_coordinates]

image_urls = []
for ra, dec in zip(ra_list, dec_list):
    image_urls.append("https://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg?TaskName=Skyserver.Chart.List&ra=" + ra + "&dec=" + dec + "&scale=0.4&width=120&height=120&opt=")

for i, image_url in enumerate(image_urls):
    try:
        image_data = requests.get(image_url).content
    except requests.exceptions.HTTPError as e:
        print(e)
    with open(os.path.join("F:/images/", f"{ra_list[i]}_{dec_list[i]}.jpg"), "wb") as f:
        f.write(image_data)
        print(f"{i + 1}/{len(image_urls)} 이미지 다운로드 완료")
