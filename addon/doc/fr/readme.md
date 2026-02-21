# Demander à OpenRouter (Ask OpenRouter)

Cette extension pour NVDA vous permet d'interagir avec les modèles d'intelligence artificielle proposés par la plateforme OpenRouter directement depuis votre lecteur d'écran.

L’extension prend désormais en charge :

* La sélection automatique et aléatoire d’un modèle gratuit
* Le choix manuel d’un modèle spécifique, y compris les modèles payants

*--

## Fonctionnalités principales

* Accès rapide à une interface de chat via un raccourci clavier.
* Gestion des conversations (nouvelle ou poursuite d'un échange).
* Sélection intelligente et aléatoire des modèles gratuits pour optimiser les quotas.
* Possibilité de choisir manuellement un modèle (gratuit ou payant).
* Affichage des réponses dans une fenêtre lisible avec historique optionnel.

*--

## Configuration : Obtenir et installer votre clé API

Pour fonctionner, l'extension nécessite une clé API provenant d'OpenRouter.

Même si vous utilisez uniquement des modèles gratuits, la clé est indispensable pour identifier vos requêtes.

### 1. Comment obtenir une clé API ?

1. Rendez-vous sur le site https://openrouter.ai/
2. Créez un compte en cliquant sur **"Sign up"** (vous pouvez utiliser GitHub, Google, MetaMask ou une adresse e-mail).
3. Une fois connecté, accédez à la section **"Keys"** dans votre tableau de bord ou via : https://openrouter.ai/keys
4. Cliquez sur **"Create Key"**.
5. Donnez un nom à votre clé (par exemple : "Ma clé API OpenRouter") puis validez.
6. **Important :** La clé n’est affichée qu’une seule fois. Copiez-la immédiatement et conservez-la dans un endroit sûr.

*--

### 2. Configurer la clé dans NVDA

1. Ouvrez le menu NVDA (NVDA + N).
2. Allez dans **Préférences**, puis **Paramètres**.
3. Sélectionnez la catégorie **"Demander à OpenRouter"**.
4. Collez votre clé dans le champ **"Clé API OpenRouter"** (les caractères sont masqués par défaut).
5. Validez avec le bouton **OK**.

#### Remarque

Juste après le champ **"Clé API OpenRouter"**, vous trouverez la case à cocher :

**"Afficher la clé API"**

Si cochée, les caractères de la clé deviennent visibles.  
Par défaut, ils sont masqués pour des raisons de sécurité.

*--

## Sélection des modèles

Dans la catégorie **"Demander à OpenRouter"** des paramètres NVDA, une nouvelle option est disponible :

### **"Utilisez tous les modèles, y compris les modèles payants"**

Cette option détermine la manière dont les modèles sont sélectionnés.

### Lorsque la case est DÉCOCHÉE (comportement par défaut)

* L’extension utilise uniquement les modèles gratuits.
* À chaque nouvelle conversation, un modèle gratuit est sélectionné aléatoirement.
* Cela permet de répartir la charge et de limiter les blocages liés aux quotas.

### Lorsque la case est COCHÉE

Lorsque cette option est activée, une liste des modèles disponibles apparaît automatiquement après la case.

* La liste est triée par ordre croissant selon le **coût des tokens de prompt** (coût par token d’entrée), du moins cher au plus cher.
* Seuls les modèles non obsolètes disposant d’un fournisseur valide sont affichés.

### Que pouvez-vous faire lorsque cette option est activée ?

* Choisir librement le modèle que vous souhaitez utiliser.
* Utiliser des modèles payants (si vous disposez de crédits OpenRouter suffisants).
* Sélectionner le modèle le plus adapté à vos besoins.
* Utiliser toujours le modèle sélectionné (sans rotation automatique).

### Qu’est-ce qu’un token de prompt ?

Un token de prompt correspond à une petite unité de texte envoyée au modèle (votre question ou votre message).

Les modèles sont généralement facturés séparément pour :
* Les tokens d’entrée (prompt)
* Les tokens de sortie (completion)

## Utilisation de l'extension

### Ouvrir l'interface de dialogue

À tout moment, ouvrez l’interface avec :

**Alt + Ctrl + A**

Vous pouvez modifier ce geste dans :

Menu NVDA → Préférences → Gestes de commandes → Demander à OpenRouter

*--

### Interface principale

La boîte de dialogue propose trois options :

1. **Créer un nouveau chat** : Démarrer une conversation.
2. **Continuer un chat** : Reprendre la conversation précédente (historique conservé).
3. **Fermer** : Quitter la boîte de dialogue (Échap fonctionne également).

*--

### Saisir votre question

Après avoir choisi de créer ou continuer un chat :

* Un champ multiligne apparaît.
* La touche **Entrée** insère un saut de ligne.
* Pour envoyer votre message :
  - Appuyez sur **Tabulation** jusqu’au bouton **OK**
  - Puis appuyez sur **Entrée**

*--

### Lecture de la réponse

Après traitement, une fenêtre de résultat s'affiche avec :

* **"Vous avez dit :"** suivi de votre question.
* **"Le modèle a répondu :"** suivi de la réponse.
* Un bouton **"Copier"** pour copier la réponse.

Si l’historique complet est activé, chaque échange est clairement séparé par des entêtes pour faciliter la lecture avec les touches de navigation rapide de NVDA.

*--

## Options d’affichage

Si vous préférez afficher uniquement la dernière réponse :

1. Ouvrez le menu NVDA (NVDA + N).
2. Allez dans **Préférences → Paramètres**.
3. Sélectionnez **Demander à OpenRouter**.
4. Décochez **"Afficher l'historique complet pour les discussions continues"**.
5. Validez avec **OK**.

*--

## Scripts non attribués

Les scripts suivants n’ont pas de gestes attribués.  
Vous pouvez les configurer dans :

Préférences → Gestes de commandes → Demander à OpenRouter

Scripts disponibles :

* Ouvrir le panneau des paramètres de l’extension
* Créer un nouveau chat directement
* Continuer un chat existant directement

*--

## Modèles gratuits, modèles payants et quotas

### Utilisation des modèles gratuits

Lorsque **"Use all models, including paid ones"** est décoché :

* Seuls les modèles marqués comme gratuits sont utilisés.
* Les modèles gratuits ont :
  - Un quota journalier limité
  - Des limitations de débit (rate limit)
  - Une disponibilité parfois temporairement restreinte

L’extension effectue une rotation automatique entre les modèles gratuits disponibles.

*--

### Utilisation des modèles payants

Lorsque **"Use all models, including paid ones"** est coché :

* Le modèle sélectionné est utilisé exclusivement.
* Des crédits OpenRouter peuvent être nécessaires.
* Les limitations du fournisseur s’appliquent.

Des erreurs telles que :

* 402 (crédits insuffisants)
* 429 (limitation temporaire)
* 404 (modèle bloqué par les paramètres de confidentialité)

peuvent s’afficher pour vous informer du problème.

*--

## Paramètres de confidentialité OpenRouter

Si vous utilisez des modèles gratuits et recevez une erreur mentionnant :

> "No endpoints found matching your data policy"

Vous devez ajuster vos paramètres de confidentialité :

https://openrouter.ai/settings/privacy

Assurez-vous d’autoriser les endpoints publics ou gratuits.

*--

## Résumé

Ask OpenRouter permet désormais :

* La sélection automatique de modèles gratuits
* Le choix manuel de tout modèle disponible
* L’utilisation de modèles payants
* L’affichage complet ou partiel de l’historique
* Une meilleure gestion des limitations des modèles gratuits

Cette flexibilité permet une utilisation aussi bien occasionnelle (gratuite) qu’avancée (modèles payants) directement depuis NVDA.

## Compatibilité ##

* Cette extension est compatible avec les versions de NVDA allant de 2025.1
  et au-delà.
