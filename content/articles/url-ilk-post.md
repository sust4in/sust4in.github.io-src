Title: Url nedir? 
Date: 2016-10-10 08:00
Modified: 2016-10-10 08:00
Category: Web Application Security
Tags: url, web, browser
Slug: url-nedir

Gördüğünüz tabelalardan kaçını okuyorsunuz...  
Genel olarak yorumlarsak yani teknolojiyi bir kenara bırakalım, araç kullanan insanlar nereye gittiklerini tabelalardan anlayabilirler.  
Sembollerinden ve renklerinden bir çok farklı anlamlar ortaya çıkabiliyor. Url dediğimde aklıma tam olarak bu geliyor.  


![where-to-go](images/tabela1.jpg)


Interneti tek bir bilgisayar gibi düşünürsek, URL bu bilgisayardaki dosyalara eriştiğimiz pathlerdir, internetteki bir kaynağa erişmemizi sağlayan yapılardır.  
## URL Yapısı

 *Absolute*(Tam) bir Url yapısı [RFC](https://tr.wikipedia.org/wiki/Request_for_Comments) [3986](https://tools.ietf.org/html/rfc3986)'da böyle belirtilmiş. Araştırdığım bütün kaynaklarda böyle bir sonuçla karşılaştım. Belli bir standart belirlenmiş.

 Aşağıdaki tabloda tam url yapısının parçalarını görebilirsiniz.


|scheme:|//|login.password@|address|:port| /path/to/resource | ?query_string|#fragment
|:--------:|:----:||:--------:|:----:||:--------:|:----:||:--------:|:----:|
|1|2|3|4|5|6|7|8|

1. Şema/Protokol adı (*http*, *https* gibi)
2. Sabit url yapısı göstergesi
3. Kaynağa erişebilmek için kullanılabilecek credentials yeri (opsiyonel)
4. Data'nın geleceği server
5. Bağlanılacak port numarası (opsiyonel)
6. kaynağı gösteren hiyerarşik unix path'i
7. **Query string** parametreleri (opsiyonel)
8. **Fragment identifiers** (opsiyonel)
	3.ve 5. alanlar dahil olmak üzere tümüne bir url'in "Authority" kısmı denir.

Tüm bunlar birleştiğinde elimizde belli karakterler barındıran bir string kalıyor. Peki Bir url parser oluşturmak istersek hangi adımları izlememiz gerekebilir?

* Şema adını görebilmek için ilk ":" karakterine kadar ilerleriz. Şimdi solumuzda kalan kısım şema/protokol stringi olmalı. Eğer beklenmeyen bir string yapısıyla karşılaşırsak bunu reddedip yolumuza devam ederiz.(tam olmayan relative pathlerde olabileceği gibi)

* Şema adının hemen ardından "//" gelmeli. eğer varsa tamam. Değilse almıyoruz.

* Authority kısmını komple almamız gerek. Bu sebeple port kısmının sonuna kadar bakıyoruz. Yani önümüze eğer "/", "\", "?", "#" gibi karakterler gelirse durmamız ve solumuzda kalan stringi extract etmemiz gerekecek. Windows işletim sisteminde filepathler "\" ile yazılır bu sebeple browserlar slash ve backslashi birlikte destekler.

* Eğer varsa credential bulmamız gerekecek. Biraz önce söktüğümüz string içerisinde "@" karakterine göre split işlemi gerçekleştiriyoruz. İlk kolon login-password içeriği olacaktır.

* Ve ardından varış adresini yani 4. alanı extract etmemiz gerekiyor. Elimizde kalan substringde şimdi sadece adres ve port kalmış olmalı ":" karakterine göre split ettiğimizde ilk kısım adresi verecektir. IPv6 adreslerde farklı bir işlem yapmamız gerekebilir

* Eğer varsa Path'i almamız lazım. Authority kısmının hemen ardından "/" veya "\" gelebildiğini biliyoruz. O zaman bir sonraki bakmamız gereken "?","#" gibi karakterler olabilir. Hangisi önce gelirse. Kalan stringin sonuna kadar bakılmalı. Eğer varış noktasına ulaşıldıysa, bu substring path'i içerir.

* Query stringini extract etmeye başladıysak bir önceki maddede "?" karakterine gelmiş olmalıyız. Bir sonraki "#" karakterine kadar gittiğimizde ise arada kalan string bize query stringi verir

* Eğer sonunda "#" karakterine vardıysanız bundan sonra sona kadar ilerlenen kısım fragment identifier olarak parse edilir.

Bu örneği The Tangled Web kitabından bloguma yazıyorum. Başta karışık gibi görünsede bu tarz bir kompleksliği anlamaya çalıştığım zaman web teknolojilerinin köşe taşlarından biri olan url yapısına daha detaylı bir açıyla bakmaya başladığımı hissettim. Kitapta ilerlediğim ve beğendiğim kısımları blogumda yer vermeye devam edeceğim.


**Reference**

- [The Tangled Web](https://www.amazon.com/Tangled-Web-Securing-Modern-Applications/dp/1593273886)
- [Outline Recap Secure Programming Lecture 11: Web Application Security II David Aspinall 3rd March 2014 by Austin Shelton](http://docplayer.net/19360794-Full-urls-specified-in-rfc-3986-have-up-to-eight-parts-scheme-login-password-address-port-path-to-resource-query_string-fragment.html)
- [URL](http://searchnetworking.techtarget.com/definition/URL)





