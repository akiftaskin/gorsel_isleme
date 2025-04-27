# OpenCV kütüphanesini içe aktarıyoruz
import cv2

# Görseli okuyoruz ('gorsel.jpg' dosyasını klasörüne koymalısın)
img = cv2.imread('gorsel.jpg')

# Eğer görsel yüklenemediyse hata verdiriyoruz
if img is None:
    print("Görsel bulunamadı!")
    exit()

# 1. Görseli gri tonlamaya çeviriyoruz
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Görselin HSV tonlamasını elde ediyoruz
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 3. Renk kanallarını değiştiriyoruz (R ile B'yi yer değiştiriyoruz)
# OpenCV'de kanal sırası BGR'dir
b, g, r = cv2.split(img)  # B, G, R kanallarını ayır
swapped_img = cv2.merge([r, g, b])  # R ve B kanallarını değiştirerek birleştir

# 4. Görselin altına adımızı yazdırıyoruz
# Adımızı yazacağımız font ve konumu seçiyoruz
font = cv2.FONT_HERSHEY_SIMPLEX
position = (50, img.shape[0] - 50)  # Alt tarafa 50px yukarıda olacak şekilde konum
font_scale = 1
font_color = (255, 255, 255)  # Beyaz renk
thickness = 2

# İsmimizi orijinal görselin üzerine yazıyoruz
img_with_name = img.copy()
cv2.putText(img_with_name, 'Akif Taskin', position, font, font_scale, font_color, thickness, cv2.LINE_AA)

# Sonuçları kaydediyoruz (İstersen gösterip kapatabilirsin de)
cv2.imwrite('gri_tonlama.jpg', gray)
cv2.imwrite('hsv_tonlama.jpg', hsv)
cv2.imwrite('kanal_degistirme.jpg', swapped_img)
cv2.imwrite('isimli_gorsel.jpg', img_with_name)

# İstersen her adımı göstermek için açıp bakabilirsin
# cv2.imshow('Gri Tonlama', gray)
# cv2.imshow('HSV Tonlama', hsv)
# cv2.imshow('Kanal Değiştirme', swapped_img)
# cv2.imshow('Isimli Görsel', img_with_name)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
