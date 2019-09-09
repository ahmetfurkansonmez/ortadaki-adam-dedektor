import subprocess # bilgisayarda komut calistirmak icin kullanilan kutuphane
import re # metinin icinde arama yapmak icin kullanilan kutuphane
import time # komutlari verilen araliklarda calistiran kutuphane

#komutlari sonsuz donguye aliyoruz
while True:
    # ayni agdaki cihazlarin mac adreslerini ogrenmek icin arp-a komutu calistiriyoruz
    result = subprocess.check_output("arp -a")
    # ayni agdaki cihazlarin mac adreslerini liste seklinde bir degiskene atiyoruz
    mac_addresses = re.findall(r"..-..-..-..-..-..", result)
    # listenin ilk elemani yani modemin mac adresini bir degiskene atiyoruz
    gateway_mac = mac_addresses[0]
    # for ile surekli modemin mac adresini diger mac adreslerle karsilastiran ve

    for x in range(1, len(mac_addresses)):
        if gateway_mac == mac_addresses[x]:
            print('[+] olasi ortadaki-adam saldirisi')
            # eger baska bir cihazin mac adresi modem mac adresine esit ise ekrana uyari ver
        else:
            continue
            # degilse devam et


    time.sleep(5)
    #donguyu 5 saniyede bir calistir