# -dev.4
Pytest, Python'da bir test çerçevesidir ve test fonksiyonlarını belirli bir şekilde çalıştırmak için işaretleyiciler veya dekoratörler (decorators) kullanır. Decoratorlar, test fonksiyonlarınızın davranışını değiştirmenize ve testleri daha yönetilebilir hale getirmenize olanak tanır.

Pytest'in en sık kullanılan decorator'ları şunlardır:

@pytest.fixture: Testleriniz için önceden ayarlanmış koşullar sağlamak için kullanılır. Örneğin, test veritabanına erişiyorsa, fixture'lar veritabanına bağlanmak ve verileri yüklemek için kullanılabilir.

@pytest.mark.parametrize: Tek bir test işleviyle farklı argümanlarla çalışmak için kullanılır. Bu decorator, aynı test işlevini birden çok kez çağırmak yerine, test fonksiyonunun bir dizi parametreyle çalıştırılmasını sağlar.

@pytest.mark.skip: Belirli testleri atlamak için kullanılır. Bu, özellikle testlerin geçici olarak başarısız olması durumunda kullanışlıdır.

@pytest.mark.xfail: Belirli testlerin başarısız olacağını bilerek işaretlemek için kullanılır. Bu, bir testin zaman zaman başarısız olması durumunda kullanışlıdır ve test geçerli bir hata mesajıyla birlikte başarısız olur.
