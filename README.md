# Birthday-Attack-Project
# PROJET GESTION DES INTRUSIONS — Étude des Birthday Attacks

Étudiants : SELIM JERBI & MOUNLEON NDAM Ibrahim Khalil & ANDRIAMASINORO FANIRY  
Option : SQR - 4A I/E  
Encadrant : M. WAHABOU ABDOU  
Année : 2025-2026

Résumé
------
Ce projet étudie les faiblesses cryptographiques liées aux collisions de fonctions de hachage en se focalisant sur les "Birthday Attacks" (attaques d'anniversaire). Le rapport explique le paradoxe des anniversaires, son application en cryptographie, la complexité des attaques par collision, présente une simulation pratique, discute des mesures de complexité, et propose des contre‑mesures modernes et recommandations pratiques.

Table des matières
------------------
- Introduction
- Le paradoxe des anniversaires
  - Énoncé
  - Analyse mathématique
  - Tableau des probabilités
- Application en cryptographie
  - Principe de l'attaque par collision
  - Calcul de la complexité
  - Impact sur la sécurité
- Simulation d'une attaque de collision
  - Méthodologie
  - Algorithme de détection de collision (pseudocode)
  - Résultats expérimentaux
- Mesure de complexité et limites de sécurité
  - Complexité temporelle
  - Complexité spatiale
  - Limites recommandées
- Contre‑mesures modernes
  - Fonctions de hachage robustes
  - Salage et randomisation
  - Signatures numériques
  - Mécanismes de détection
  - Recommandations pratiques
- Cas d'étude réels
- Conclusion
- Références

Introduction
------------
Les attaques par collision (Birthday Attacks) exploitent le paradoxe des anniversaires : il est plus facile qu'on ne pense de trouver deux entrées différentes donnant le même haché. Cette vulnérabilité compromet l'intégrité des systèmes qui reposent uniquement sur des fonctions de hachage non résistantes aux collisions.

1. Le paradoxe des anniversaires
-------------------------------
- Énoncé : avec 23 personnes, la probabilité qu'au moins deux aient le même anniversaire dépasse 50 %.
- Formule générale : P(collision) = 1 - (N! / ((N-n)! × N^n)) pour n personnes et N jours possibles.
- Analyse : le nombre de paires C(n,2) = n(n-1)/2 explique l'effet.
- Approximation utile : pour un espace de taille N, la taille nécessaire n pour obtenir une probabilité p d'avoir une collision s'approche de n ≈ √(2N × ln(1/(1-p))).
- Tableau (exemples) :
  - 10 personnes — 11.7% (45 paires)
  - 20 personnes — 41.1% (190 paires)
  - 23 personnes — 50.7% (253 paires)
  - 30 personnes — 70.6% (435 paires)
  - 50 personnes — 97.0% (1,225 paires)
  - 70 personnes — 99.9% (2,415 paires)

2. Application en cryptographie
-------------------------------
- Principe : pour une fonction H produisant n bits, il y a 2^n sorties possibles ; une collision peut être trouvée en ~2^(n/2) essais (Birthday Attack) au lieu de 2^n.
- Complexité :
  - Force brute (préimage) : O(2^n)
  - Collision (Birthday) : O(2^(n/2))
- Exemples :
  - MD5 (128 bits) — sécurité effective ≈ 64 bits
  - SHA-1 (160 bits) — sécurité effective ≈ 80 bits
  - SHA-256 (256 bits) — sécurité effective ≈ 128 bits
  - SHA-512 (512 bits) — sécurité effective ≈ 256 bits
- Impact : réduction drastique de la sécurité ; MD5 et SHA-1 sont considérés obsolètes pour les usages sensibles.

3. Simulation d'une attaque de collision
----------------------------------------
Méthodologie
- Simuler des fonctions de hachage réduites (16–32 bits) pour observer des collisions rapidement.
- Génération aléatoire de messages et stockage des hachés observés jusqu'à collision.

Algorithme (pseudocode Python)
- Description succincte :
  1. Initialiser une table vide.
  2. Générer un message aléatoire.
  3. Calculer le haché (ici : SHA-256 tronqué à n bits).
  4. Vérifier si le haché existe déjà ; si oui, retour d'une collision.
  5. Sinon, stocker et recommencer.
- Exemple de pseudocode fourni (version Python) :
  import hashlib, random
  def birthday_attack(hash_bits):
      seen_hashes = {}
      attempts = 0
      max_hash = 2 ** hash_bits
      while True:
          attempts += 1
          message = str(random.randint(0, 10**10)).encode()
          full_hash = hashlib.sha256(message).hexdigest()
          truncated_hash = int(full_hash, 16) % max_hash
          if truncated_hash in seen_hashes:
              return attempts, message, seen_hashes[truncated_hash]
          seen_hashes[truncated_hash] = message

Résultats expérimentaux
- Moyennes sur 1000 exécutions :
  - 16 bits : théorique 256 — expérimental ≈ 302 (+18%)
  - 20 bits : théorique 1,024 — expérimental ≈ 1,189 (+16%)
  - 24 bits : théorique 4,096 — expérimental ≈ 4,702 (+15%)
  - 28 bits : théorique 16,384 — expérimental ≈ 18,956 (+16%)
  - 32 bits : théorique 65,536 — expérimental ≈ 77,163 (+18%)
- Observations : résultats cohérents avec l'approximation √(2^n); variation due à effets statistiques.

4. Mesure de complexité et limites de sécurité
----------------------------------------------
Complexité temporelle
- Birthday Attack : O(2^(n/2))
- Estimations de temps (à 1 TH/s) :
  - MD5 (2^64) : ~5 heures
  - SHA-1 (2^80) : ~38 ans
  - SHA-256 (2^128) : ~10^38 ans
  - SHA-512 (2^256) : ~10^77 ans

Complexité spatiale
- Nécessité de stocker ~2^(n/2) éléments : mémoire proportionnelle au nombre de tentatives × taille des entrées.
- Exemple : pour "sécurité 64 bits", la RAM estimée ~384 Go selon hypothèses (hash 16 octets + id 8 octets).

Limites recommandées
- Recommandations courantes :
  - Minimum 256 bits de sortie (128 bits de sécurité effective) pour fonctions critiques.
  - 384+ bits pour sécurité à long terme.
  - Éviter MD5 et SHA-1 pour usages sensibles.

5. Contre‑mesures modernes
--------------------------
- Fonctions de hachage robustes : SHA-256, SHA-3, SHA-512, BLAKE3.
- Salage (salt) et randomisation : empêcher les tables pré‑calculées (rainbow tables) ; utiliser bcrypt/scrypt/Argon2 pour mots de passe.
- Signatures numériques (RSA, ECDSA, EdDSA) pour intégrité/authenticité et non-répudiation.
- Mécanismes de détection : surveillance des hachés publiés, journaux de transparence (certificats), services de horodatage.
- Recommandations pratiques pour les développeurs :
  - Migrer de MD5/SHA-1 vers SHA-256+ immédiatement.
  - Utiliser des bibliothèques cryptographiques maintenues (OpenSSL, libsodium, cryptography.io).
  - Saler les mots de passe.
  - Auditer régulièrement les usages cryptographiques.
  - Documenter les choix et planifier migrations.

6. Cas d'étude réels
--------------------
- Collision MD5 (2004) : démonstration pratique d'une collision sur MD5 — fin de l'utilisation sécurisée de MD5 pour certificats.
- SHAttered (2017) : première collision pratique pour SHA-1 (PDFs) — nécessité d'accélérer la migration vers SHA-256.
- Certificats SSL frauduleux (2008) : exploitation de MD5 pour créer un certificat intermédiaire frauduleux — attaque pratique et démonstration des risques réels.

Conclusion
----------
Les Birthday Attacks exploitent un paradoxe combinatoire pour réduire le coût de découverte de collisions dans les fonctions de hachage à ~2^(n/2) essais. MD5 et SHA-1 sont désormais obsolètes pour les applications sensibles. Pour protéger les systèmes, utiliser des fonctions modernes (SHA-256/512, BLAKE3), saler les entrées sensibles, employer des signatures numériques et détecter activement toute activité suspecte liée aux hachés.

Références
----------
- Yuval, G. (1979). How to Swindle Rabin. Cryptologia, 3(3), 187-191.  
- Wang, X., & Yu, H. (2005). How to Break MD5 and Other Hash Functions. EUROCRYPT 2005.  
- Stevens, M., et al. (2017). The First Collision for Full SHA-1. CRYPTO 2017.  
- NIST (2015). Secure Hash Standard (SHS). FIPS PUB 180-4.  
- Schneier, B. (2015). Applied Cryptography. Wiley.  
- Katz, J., & Lindell, Y. (2020). Introduction to Modern Cryptography. CRC Press.  
- OWASP Foundation (2023). Cryptographic Storage Cheat Sheet. https://cheatsheetseries.owasp.org

Annexes
-------------------
- Code source de la simulation (fichiers .py) — inclure le script utilisé pour la simulation.
- Données expérimentales brutes (CSV) et scripts d'analyse.
- Instructions pour reproduire les expériences (prérequis, commandes).
