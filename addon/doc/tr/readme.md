# OpenRouter'a Sor

- Yazar(lar) : Abdel.

Bu NVDA eklentisi, OpenRouter platformu tarafından sağlanan Yapay Zeka modelleriyle doğrudan ekran okuyucunuzdan etkileşim kurmanıza olanak tanır.

Eklenti her ikisini de destekler:

- Ücretsiz modellerin otomatik rastgele seçimi
- Mevcut herhangi bir modelin manuel seçimi (ücretli olanlar dahil)

## Temel Özellikler

- Hızlı Erişim: Sohbet arayüzünü istediğiniz zaman küresel bir kısayolla açın.
- Konuşma Yönetimi: Yeni bir sohbet başlatın veya önceki sohbetinize devam edin.
- Akıllı Ücretsiz Model Rotasyonu: Günlük kullanım kotalarını optimize etmek için otomatik olarak rastgele bir ücretsiz model seçer.
- Manuel Model Seçimi: Ayarlar panelinden belirli bir modeli (ücretli modeller dahil) seçin.
- Erişilebilir Sonuçlar: Yanıtları, isteğe bağlı tam geçmiş görüntüleme özelliğiyle net, gezinmesi kolay bir pencerede görüntüleyin.

## Yapılandırma: API Anahtarınızı Alma ve Kurma

Bu eklentiyi kullanmak için OpenRouter'dan bir API anahtarınızın olması gerekir.

Ücretsiz modelleri kullanırken bile, isteklerinizi tanımlamak için anahtar gereklidir.

### 1. API anahtarı nasıl alınır?

1. [OpenRouter.ai](https://openrouter.ai/) adresine gidin.
2. "Sign up"a tıklayarak bir hesap oluşturun (GitHub, Google veya MetaMask hesabı veya e-posta adresinizle oturum açabilirsiniz).
3. Oturum açtıktan sonra kontrol panelinizdeki "Keys" bölümüne gidin veya doğrudan şu adrese gidin: https://openrouter.ai/keys
4. "Create Key" düğmesine tıklayın.
5. Anahtarınıza bir ad verin (örneğin: "OpenRouter API anahtarım") ve "Create"e tıklayın.
6. Önemli: Anahtarınız yalnızca bir kez görüntülenecektir. Hemen kopyalayın ve güvenli bir yerde saklayın.

### 2.2) NVDA'da anahtarın ayarlanması

1. NVDA menüsünü açın (NVDA + N).
2. Tercihler'e ve ardından Ayarlar'a gidin.
3. Kategoriler listesinde "Ask OpenRouter"ı seçin.
4. API anahtarınızı "OpenRouter API Key" alanına yapıştırın.
5. Kaydetmek için Tamam'a basın.

#### API Anahtarını Göster

NVDA ayarları panelinde, "OpenRouter API Key" alanının hemen ardından şu etiketli bir onay kutusu bulunur:

"Show API key"

İşaretlenirse API anahtarının karakterleri görünür hale gelir.  
Varsayılan olarak güvenlik nedeniyle gizlenirler.

## Model Seçim Ayarları

Ask OpenRouter ayarları kategorisinde yeni bir seçenek bulacaksınız:

### "Ücretli modeller dahil tüm modelleri kullan"

Bu seçenek modellerin nasıl seçildiğini kontrol eder.

###

- Eklenti, her yeni konuşma için otomatik olarak rastgele bir ücretsiz model seçer.
- Mevcut ücretsiz modeller arasında dönüşümlü olarak çalışır.
- Bu, kullanımın dağıtılmasına ve hız sınırlarının önlenmesine yardımcı olur.

### Seçenek işaretlendiğinde

Bu seçenek etkinleştirildiğinde, onay kutusunun ardından otomatik olarak mevcut modellerin bir listesi görünür.

- Liste, istem jetonu (prompt token) fiyatına (giriş jetonu başına maliyet) göre artan sırada, en düşükten en yükseğe doğru sıralanmıştır.
- Yalnızca desteği kesilmemiş ve geçerli sağlayıcısı olan modeller görüntülenir.

### Bu seçenek etkinleştirildiğinde ne yapabilirsiniz?

- Mevcut herhangi bir modeli seçin.
- Ücretli modelleri kullanın (yeterli OpenRouter krediniz varsa).
- İhtiyaçlarınıza en uygun modeli seçin.
- Sohbetlerinizde seçtiğiniz modeli kullanmaya devam edin (otomatik rotasyon yok).

### İstem jetonu (prompt token) nedir?

Bir istem jetonu, modele gönderilen küçük bir metin birimini (sorunuzu veya girdinizi) temsil eder.

Modeller genellikle aşağıdakiler için ayrı olarak faturalandırılır:

- Giriş jetonları (prompt)
- Çıkış jetonları (completion)

## Nasıl Kullanılır?

### Sohbet İletişim Kutusunu Açma

Şu tuşlara basın:

Ctrl + Alt + A

Bu hareketi şu şekilde değiştirebilirsiniz:
NVDA menüsü → Tercihler → Girdi Hareketleri → Ask OpenRouter

### Ana Arayüz

İletişim kutusunda üç düğme bulunur:

1. New Chat – Yepyeni bir konuşma başlatır.
2. Continue Chat – Önceki konuşmayı sürdürür (geçmişi tutar).
3. Close – İletişim kutusunu kapatır (Escape de çalışır).

### İsteminizi Girme

"New Chat" veya "Continue Chat" seçeneğini seçtikten sonra:

- Çok satırlı bir metin alanı görünür.
- Enter'a basıldığında yeni bir satır eklenir.
- Mesajınızı göndermek için:
  - Tamam düğmesine ulaşmak için Tab'a basın.
  - Enter'a basın.

### Yanıtı Okuma

İşlemden sonra aşağıdakileri içeren bir sonuç penceresi görünür:

- "Siz:" (You said:) ve ardından mesajınız.
- "Model yanıt verdi:" (The model replied:) ve ardından gelen yanıt.
- Yanıtı kopyalamak için "Kopyala" düğmesi.

Tam geçmiş gösterimi etkinleştirildiğinde, her bir değişim başlıklarla net bir şekilde birbirinden ayrılır; bu sayede NVDA'nın hızlı dolaşım tuşlarını kullanarak kolayca gezinebilirsiniz.

## Görüntüleme Seçenekleri

Konuşma geçmişinin tamamı yerine yalnızca en son yanıtı görüntülemeyi tercih ederseniz:

1. NVDA menüsünü açın (NVDA + N).
2. Tercihler → Ayarlar'a gidin.
3. Ask OpenRouter'ı seçin.
4. İşareti kaldırın:
   "Sürekli tartışmalar için tam sohbet geçmişini görüntüle"
5. Tamam'a basın.

## Atanmamış Komut Dosyaları

Aşağıdaki komutlara hareket atanmamıştır.  
Bunları şu yoldan tanımlayabilirsiniz:

Tercihler → Girdi Hareketleri → Ask OpenRouter

Kullanılabilir komutlar:

- Eklenti ayarlar panelini aç
- Doğrudan yeni bir sohbet başlat
- Doğrudan mevcut bir sohbete devam et

## Ücretsiz Modeller, Ücretli Modeller ve Kotalar

### Ücretsiz Model Kullanımı

"Ücretli modeller dahil tüm modelleri kullan" seçeneğinin işareti kaldırıldığında:

- Yalnızca OpenRouter'da ücretsiz olarak etiketlenen modeller kullanılır.
- Ücretsiz modeller şunlara sahiptir:
  - Sınırlı günlük kotalar
  - Paylaşımlı hız sınırları (rate limits)
  - Olası geçici ulaşılamama durumları

Eklenti, kullanılabilirliği artırmak için ücretsiz modeller arasında otomatik olarak geçiş yapar.

### Ücretli Model Kullanımı

"Ücretli modeller dahil tüm modelleri kullan" seçeneği işaretlendiğinde:

- Eklenti tam olarak seçtiğiniz modeli kullanır.
- Bu, ücretli modelleri içerebilir.
- Yeterli OpenRouter krediniz olmalıdır.
- Sağlayıcı hız sınırları geçerli olabilir.

Şu hatalar:

- 402 (yetersiz kredi)
- 429 (hız sınırı aşıldı)
- 404 (gizlilik ayarları tarafından izin verilmeyen model)

sorun hakkında sizi bilgilendirmek için doğrudan görüntülenir.

## Gizlilik Ayarları Hatırlatıcısı

Ücretsiz modeller kullanıyor ve şunu belirten bir hata alıyorsanız:

> "Veri politikanızla eşleşen uç nokta bulunamadı"

OpenRouter gizlilik ayarlarınızı düzenlemeniz gerekebilir:

https://openrouter.ai/settings/privacy

Kamuya açık/ücretsiz model uç noktalarına izin verildiğinden emin olun.

## Uyumluluk

- Bu eklenti, NVDA'nın 2025.1 ve sonraki sürümleriyle uyumludur.

## 20260221.0.0 için değişiklikler

- Ayarlar panelinden mevcut tüm modellerin manuel seçimi eklendi
- Ücretli modelleri kullanma yeteneği eklendi

## 20260217.0.0 için değişiklikler

- İlk sürüm
