# Softmax Tabanlı Yük Dengeleyici (Softmax-Based Load Balancer)

Bu proje, **dağıtık sistemlerde** sıkça karşılaşılan **non-stationary (zamanla değişen)** ve **gürültülü (noisy)** sunucu performanslarını yönetmek için geliştirilmiş bir İstemci Taraflı Yük Dengeleyicisidir (Client-Side Load Balancer).

## 🎯 Proje Amacı
Geleneksel "Round-Robin" veya "Random" algoritmaları, sunucuların anlık durumuna kördür. Bu proje, **Pekiştirmeli Öğrenme (Reinforcement Learning)** prensiplerine dayanan **Softmax Action Selection** algoritmasını kullanarak:
1.  Sunucuların değişen performansını öğrenmeyi,
2.  **Keşif (Exploration)** ve **Sömürü (Exploitation)** dengesini kurmayı,
3.  Toplam bekleme süresini (latency) minimize etmeyi hedefler.
