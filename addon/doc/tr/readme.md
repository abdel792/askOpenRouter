# OpenRouter'a sor

* Yazar(lar): Abdel.

Bu NVDA eklentisi, OpenRouter platformu tarafından sağlanan Yapay Zeka modelleriyle doğrudan ekran okuyucunuzdan etkileşim kurmanıza olanak tanır.

Eklenti her ikisini de destekler:
* Ücretsiz modellerin otomatik rastgele seçimi
* Mevcut herhangi bir modelin manuel seçimi (ücretli olanlar dahil)

## Temel Özellikler

* Hızlı Erişim: Sohbet arayüzünü istediğiniz zaman genel bir kısayolla açın.
* Konuşma Yönetimi: Yeni bir sohbet başlatın veya önceki sohbetinize devam edin.
* Akıllı Boş Model Döndürme: Günlük kullanım kotalarını optimize etmek için otomatik olarak rastgele bir boş model seçer.
* Manuel Model Seçimi: Ayarlar panelinden belirli bir model seçin (ücretli modeller dahil).
* Erişilebilir Sonuçlar: Yanıtları, isteğe bağlı tam geçmiş ekranıyla net, dolaşılması kolay bir pencerede görüntüleyin.

## Yapılandırma: API Anahtarınızı Alma ve Yükleme

Bu eklentiyi kullanmak için OpenRouter'dan bir API anahtarınızın olması gerekir.

Ücretsiz modelleri kullanırken bile isteklerinizi tanımlamak için anahtar gereklidir.

### 1. API anahtarı nasıl alınır

1. [OpenRouter.ai](https://openrouter.ai/) adresine gidin.
2. "Kaydol"u tıklayarak bir hesap oluşturun (GitHub, Google veya MetaMask hesabıyla veya e-posta adresinizle oturum açabilirsiniz).
3. Oturum açtıktan sonra kontrol panelinizdeki "Anahtarlar" bölümüne gidin veya doğrudan şu adrese gidin: https://openrouter.ai/keys
4. "Anahtar Oluştur" düğmesini tıklayın.
5. Anahtarınıza bir ad verin (örneğin: "OpenRouter API anahtarım") ve "Oluştur"a tıklayın.
6. Önemli: Anahtarınız yalnızca bir kez görüntülenecektir. Hemen kopyalayın ve güvenli bir yerde saklayın.

### 2. NVDA'da anahtarın ayarlanması

1. NVDA menüsünü açın (NVDA + N).
2. Tercihler'e ve ardından Ayarlar'a gidin.
3. Kategoriler listesinde "OpenRouter'a Sor" seçeneğini seçin.
4. API anahtarınızı "OpenRouter API Anahtarı" alanına yapıştırın.
5. Kaydetmek için Tamam'a basın.

#### API Anahtarını Göster

NVDA ayarları panelinde, "OpenRouter API Anahtarı" alanının hemen ardından şu etikete sahip bir onay kutusu vardır:

"API anahtarını göster"

İşaretlenirse API anahtarının karakterleri görünür hale gelir.
Varsayılan olarak güvenlik nedeniyle gizlenirler.

## Model Seçim Ayarları

OpenRouter'a Sor ayarları kategorisinde yeni bir seçenek bulacaksınız:

### "Ücretli olanlar dahil tüm modelleri kullanın"

Bu seçenek modellerin nasıl seçildiğini kontrol eder.

### Seçenek İŞARETİ KALDIRILMADIĞINDA (varsayılan davranış)

* Eklenti, her yeni konuşma için otomatik olarak rastgele bir ücretsiz model seçer.
* Mevcut ücretsiz modeller arasında dönüşümlü olarak çalışır.
* Bu, kullanımın dağıtılmasına ve hız sınırlarının önlenmesine yardımcı olur.

### Seçenek işaretlendiğinde

Bu seçenek etkinleştirildiğinde, onay kutusunun ardından otomatik olarak mevcut modellerin bir listesi görünür.

* Liste, İstem jetonu fiyatına (giriş jetonu başına maliyet) göre artan sırada, en düşükten en yükseğe doğru sıralanmıştır.
* Yalnızca geçerli sağlayıcılara sahip, kullanımdan kaldırılmamış modeller görüntülenir.

### Bu seçenek etkinleştirildiğinde ne yapabilirsiniz?

* Mevcut herhangi bir modeli seçin.
* Ücretli modelleri kullanın (yeterli OpenRouter krediniz varsa).
* İhtiyaçlarınıza en uygun modeli seçin.
* Sohbetlerinizde seçtiğiniz modeli kullanmaya devam edin (otomatik dönüşüm yok).

### İstem jetonu nedir?

Bir komut jetonu, modele gönderilen küçük bir metin birimini (sorunuzu veya girdinizi) temsil eder.

Modeller genellikle aşağıdakiler için ayrı olarak faturalandırılır:
* Giriş jetonları (istem)
* Çıktş jetonları (tamamlanma)

## Nasıl Kullanılır

### Sohbet İletişim Kutusunu Açma

Basın:

Ctrl + Alt + A

Bu hareketi şu şekilde değiştirebilirsiniz:
NVDA menüsü → Tercihler → Girdi Hareketleri → OpenRouter'a Sor

### Ana Arayüz

İletişim kutusunda üç düğme bulunur:

1. Yeni Sohbet – Yepyeni bir sohbet başlatır.
2. Sohbete Devam Et – Önceki konuşmayı sürdürür (geçmişi tutar).
3. Kapat – İletişim kutusunu kapatır (Escape tuşuda çalışır).

### İsteminizi Girme

"Yeni Sohbet" veya "Sohbete Devam Et" seçeneğini seçtikten sonra:

* Çok satırlı bir metin alanı görünür.
* Enter tuşuna basıldığında yeni bir satır eklenir.
* Mesajınızı göndermek için:
  - Tamam düğmesine ulaşmak için Tab tuşuna basın.
  - Enter'a basın.

### Yanıtı Okumak

İşlemden sonra aşağıdakileri içeren bir sonuç penceresi görünür:

* "Siz:" ve ardından mesajınız.
* "Model cevap verdi:" ve ardından yanıt geldi.
* Yanıtı kopyalamak için "Kopyala" düğmesi.

Tam geçmiş gösterimi etkinleştirildiğinde, her bir işlem başlıklar ile net bir şekilde birbirinden ayrılır; bu sayede NVDA'nın hızlı dolaşım tuşlarını kullanarak kolayca gezinebilirsiniz.

## Görüntüleme Seçenekleri

Konuşma geçmişinin tamamı yerine yalnızca en son yanıtı görüntülemeyi tercih ederseniz:

1. NVDA menüsünü açın (NVDA + N).
2. Tercihler → Ayarlar'a gidin.
3. OpenRouter'a Sor'u seçin.
4. İşareti kaldırın:
   "Sürekli tartışmalar için sohbet geçmişinin tamamını görüntüle"
5. Tamam'a basın.

## Atanmamış Komutlar

Aşağıdaki komutlara hareket atanmamıştır.
Bunları şu şekilde tanımlayabilirsiniz:

Tercihler → Girdi Hareketleri → OpenRouter'a Sor

Mevcut komutlar:

* Eklenti ayarları panelini açın
* Doğrudan yeni bir sohbet başlatın
* Mevcut bir sohbete doğrudan devam edin

## Ücretsiz Modeller, Ücretli Modeller ve Kotalar

### Ücretsiz Model Kullanımı

"Ücretli olanlar dahil tüm modelleri kullan" seçeneğinin işareti kaldırıldığında:

* Yalnızca OpenRouter'da ücretsiz olarak etiketlenen modeller kullanılır.
* Ücretsiz modeller şunları içerir:
  - Sınırlı günlük kotalar
  - Ortak kullanım sınırları
  - Hizmetin geçici olarak kullanılamama ihtimali

Eklenti, kullanılabilirliği artırmak için ücretsiz modeller arasında otomatik olarak geçiş yapar.

### Ücretli Model Kullanımı

"Ücretli olanlar dahil tüm modelleri kullan" seçeneği işaretlendiğinde:

* Eklenti tam olarak seçtiğiniz modeli kullanır.
* Buna ücretli modeller de dahil olabilir.
* Yeterli OpenRouter krediniz olmalıdır.
* Sağlayıcı ücret limitleri geçerli olabilir.

Aşağıdaki gibi hatalar:
* 402 (yetersiz kredi)
* 429 (hız sınırlı)
* 404 (gizlilik ayarları modele izin vermiyor)

sorun hakkında sizi bilgilendirmek için doğrudan görüntülenir.

## Gizlilik Ayarları Hatırlatıcısı

Ücretsiz modeller kullanıyor ve şunu belirten bir hata alırsanız:

> "Veri politikanızla eşleşen uç nokta bulunamadı"

OpenRouter gizlilik ayarlarınızı değiştirmeniz gerekebilir:

https://openrouter.ai/settings/privacy

Genel/ücretsiz model uç noktalarına izin verildiğinden emin olun.

## Uyumluluk ##

* Bu eklenti, NVDA'nın 2025.1 ve sonraki sürümleriyle uyumludur.

## 20260221.0.0 için değişiklikler

* Ayarlar panelinden mevcut tüm modellerin manuel olarak seçilebilme özelliği eklendi
* Ücretli modelleri kullanma yeteneği eklendi

## 20260217.0.0 için değişiklikler

* İlk sürüm
