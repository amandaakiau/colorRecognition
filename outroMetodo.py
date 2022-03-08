from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import utils
import cv2
import numpy as np


image = cv2.imread('.\src\carroazul.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


#extrai informações da altura e largura da imagem
height, width, _ = np.shape(image)

plt.figure()
plt.imshow(image)


# reshape da imagem para ser uma lista de pixels (uma matriz com linhas = [altura*width] colunas = 3 (rgb)
image2 = image.reshape((height * width, 3))

# quantidade de clusters
clt = KMeans(n_clusters = 1)
clt.fit(image2)

# cria um histograma de clusters e entao cria uma figura
# que representa o número de pixels rotulados para cada cor
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)

# mostra a paleta de cores
plt.figure()
plt.axis("off")
plt.imshow(bar)  #imagem da paleta de cores
plt.show()


############ identifica a cor de um pixel (mesma logica do codigo main)


#hsv_frame = cv2.cvtColor(bar, cv2.COLOR_BGR2HSV)
hsv_frame = cv2.cvtColor(bar, cv2.COLOR_RGB2HSV)

height, width, _ = bar.shape

cx = int((width / 2))
cy = int((height / 2))


pixel_center = hsv_frame[cy, cx]
h_value = pixel_center[0]
s_value = pixel_center[1]
v_value = pixel_center[2]



if (s_value <= 20) and (v_value >= 230):
	cor = "BRANCO"
elif (v_value < 230) and (s_value <= 57):
	cor = "PRATA"
elif (v_value < 57):
	cor = "PRETO"
elif (h_value <= 7) or (h_value >= 170):
	cor = "VERMELHO"
elif (h_value >= 8) and (h_value <= 20):
	cor = "LARANJA"
elif (h_value >= 21) and (h_value <= 35):
	cor = "AMARELO"
elif (h_value >= 36) and (h_value <= 84):
	cor = "VERDE"
elif (h_value >= 85) and (h_value <= 133):
	cor = "AZUL"
elif (h_value >= 134) and (h_value <= 148):
	cor = "VIOLETA"
elif (h_value >= 149) and (h_value <= 169):
	cor = "ROSA"
else:
	cor = "Nao identificado"



print(cor)