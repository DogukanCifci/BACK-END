# Server Systems

- Physical Servers (BareMetal Servers):

  - Bilgisayar -> Yüksek donanım, özel işlemciler, özel işletim sistemleri.
  - Kurulum: zor
  - VeriTaşıma: zor
  - Maliyet: yüksek
  - Dedicated Servers
    \*Bir tane donanim ve bir tane yazilim(1 cihazin icinde bir server)

- Virtual Servers (VMs: Virtual Machines):

  - Bir fiziksel makina içinde çok sanal makina.
  - Kurulum: orta (iso image)
  - VeriTaşıma: orta
  - Maliyet: orta
  - Bir makiaden diğer makinaya geçiş zorluğu.
  - Hypervisor yazılımları -> vmware.com
  - VPS (Virtual Private Server), VDS (Virtual Dedicated Server)
    \*Bir cihazin icinde birden fazla server

- Containers:
  - Bir fiziksel/sanal makina içinde çok konteyner.
  - Kurulum: kolay (container image)
  - VeriTaşıma: kolay
  - Maliyet: düşük
  - Tüm konteynerları aynı ortamdan yönetebilme.
  - Microservice mimarisi.
  - Container yazılımları -> docker.com(En ünlüsü )
    \*Bir cihaz icindeki severlarin birinin icinde birden fazla yazilim-container

## Temel Bilgiler

- IP ve Port mantığı
- Default portlar 80 443 -> https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
- http -> 80 \* http://clarusway.com == http://clarusway.com:80
- https -> 443 \* https://clarusway.com == https://clarusway.com:443 (need SSL)

---

# Docker

## Yüklemeler:

- Docker Desktop -> https://www.docker.com/products/docker-desktop/

  - Windows ve Macos için setup dosyası mevcut.
  - Linux sistemlere CLI üzerinden kurulum yapılabilir. -> https://docs.docker.com/desktop/install/linux-install/

- Docker Hub -> https://hub.docker.com

- VSCode Docker Extension -> https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker
