import distutils.command.install_lib

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import utils
import cv2


image = cv2.imread('.\src\carroprata1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


plt.figure()
plt.imshow(image)



# reshape the image to be a list of pixels
image2 = image.reshape((image.shape[0] * image.shape[1], 3))

# quantidade de clusters
clt = KMeans(n_clusters = 3)
clt.fit(image2)

# cria um histograma de clusters e entao cria uma figure
# representa o número de pixels rotulados para cada cor
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)

# mostra a paleta de cores
plt.figure()
plt.axis("off")
plt.imshow(bar)  #imagem da paleta de cores
plt.show()


############ identifica a cor de um pixel (mesma logica do codigo main)


hsv_frame = cv2.cvtColor(bar, cv2.COLOR_RGB2HSV)

height, width, _ = bar.shape

cx = int((width / 2) - 50)
cy = int((height / 2.5) - 10)


pixel_center = hsv_frame[cy, cx]
h_value = pixel_center[0]
s_value = pixel_center[1]
v_value = pixel_center[2]



if (s_value <= 40) and (v_value <= 227):
	color = "PRATA"
elif v_value <= 43:
	color = "PRETO"
elif s_value <= 44:
	color = "BRANCO"
elif (h_value <= 7) or (h_value >= 170):
	color = "VERMELHO"
elif (h_value >= 8) and (h_value <= 20):
	color = "LARANJA"
elif (h_value >= 21) and (h_value <= 35):
	color = "AMARELO"
elif (h_value >= 36) and (h_value <= 84):
	color = "VERDE"
elif (h_value >= 85) and (h_value <= 133):
	color = "AZUL"
elif (h_value >= 134) and (h_value <= 148):
	color = "VIOLETA"
elif (h_value >= 149) and (h_value <= 169):
	color = "ROSA"
else:
	color = "Nao identificado"


print(color)