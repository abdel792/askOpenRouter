# Ask OpenRouter

- Auteur(s) : Abdel.

Cette extension pour NVDA vous permet d'interagir avec les modèles d'intelligence artificielle proposés par la plateforme OpenRouter directement depuis votre lecteur d'écran.

L'extension prend en charge :

- La sélection automatique et aléatoire de modèles gratuits
- Le choix manuel de n'importe quel modèle disponible (y compris les modèles payants)

## Caractéristiques principales

- Accès rapide : Ouvrez l'interface de discussion à tout moment grâce à un raccourci global.
- Gestion des conversations : Démarrez une nouvelle conversation ou poursuivez votre échange précédent.
- Rotation intelligente des modèles gratuits : Sélectionne automatiquement un modèle gratuit au hasard pour optimiser les quotas d'utilisation quotidienne.
- Sélection manuelle du modèle : Choisissez un modèle spécifique (y compris les modèles payants) depuis le panneau des paramètres.
- Résultats accessibles : Consultez les réponses dans une fenêtre claire et facile à parcourir avec affichage optionnel de l'historique complet.

## Configuration : Obtenir et installer votre clé API

Pour utiliser cette extension, vous devez posséder une clé API d'OpenRouter.

Même si vous utilisez des modèles gratuits, la clé est requise pour identifier vos requêtes.

### 1. Comment obtenir une clé API

1. Allez sur [OpenRouter.ai](https://openrouter.ai/).
2. Créez un compte en cliquant sur "Sign up" (vous pouvez vous connecter avec un compte GitHub, Google, MetaMask ou votre adresse e-mail).
3. Une fois connecté, accédez à la section "Keys" de votre tableau de bord, ou allez directement sur : https://openrouter.ai/keys
4. Cliquez sur le bouton "Create Key".
5. Donnez un nom à votre clé (par exemple : "Ma clé API OpenRouter") et cliquez sur "Create".
6. Important : Votre clé ne sera affichée qu'une seule fois. Copiez-la immédiatement et conservez-la dans un endroit sûr.

### 2) 2) Configuration de la clé dans NVDA

1. Ouvrez le menu NVDA (NVDA + N).
2. Allez dans Préférences, puis Paramètres.
3. Dans la liste des catégories, sélectionnez "Ask OpenRouter".
4. Collez votre clé API dans le champ "OpenRouter API Key".
5. Appuyez sur OK pour enregistrer.

#### Afficher la clé API

Dans le panneau des paramètres de NVDA, juste après le champ "OpenRouter API Key", se trouve une case à cocher nommée :

"Afficher la clé API"

Si elle est cochée, les caractères de la clé API deviennent visibles.  
Par défaut, ils sont masqués pour des raisons de sécurité.

## Paramètres de sélection du modèle

Dans la catégorie des paramètres de Ask OpenRouter, vous trouverez une nouvelle option :

### "Utiliser tous les modèles, y compris les payants"

Cette option contrôle la manière dont les modèles sont sélectionnés.

### Lorsque l'option est DÉCOCHÉE (comportement par défaut)

- L'extension sélectionne automatiquement un modèle gratuit au hasard pour chaque nouvelle conversation.
- Elle alterne entre les modèles gratuits disponibles.
- Cela permet de répartir l'utilisation et d'éviter les limites de débit.

### Lorsque l'option est COCHÉE

Lorsque cette option est activée, une liste des modèles disponibles apparaît automatiquement après la case à cocher.

- La liste est triée par ordre croissant selon le prix du jeton de prompt (coût par jeton d'entrée), du moins cher au plus cher.
- Seuls les modèles non obsolètes avec des fournisseurs valides sont affichés.

### Que pouvez-vous faire lorsque cette option est activée ?

- Choisir n'importe quel modèle disponible.
- Utiliser des modèles payants (si vous avez suffisamment de crédits OpenRouter).
- Sélectionner le modèle qui correspond le mieux à vos besoins.
- Continuer à utiliser le même modèle sélectionné pour vos conversations (pas de rotation automatique).

### Qu'est-ce qu'un jeton (token) de prompt ?

Un jeton (token) de prompt représente une petite unité de texte envoyée au modèle (votre question ou entrée).

Les modèles sont généralement facturés séparément pour :

- Les jetons d'entrée (prompt)
- Les jetons de sortie (complétion/réponse)

## Mode d'emploi

### Ouverture de la boîte de dialogue de discussion

Appuyez sur :

Ctrl + Alt + A

Vous pouvez modifier ce geste dans :
Menu NVDA → Préférences → Gestes de commandes → Ask OpenRouter

### Interface principale

La boîte de dialogue contient trois boutons :

1. New Chat – Démarre une toute nouvelle conversation.
2. Continue Chat – Reprend la conversation précédente (conserve l'historique).
3. Close – Ferme la boîte de dialogue (Échap fonctionne également).

### Entering Your Prompt

Après avoir sélectionné "New Chat" ou "Continue Chat" :

- Un champ de texte multiligne apparaît.
- Appuyer sur Entrée insère une nouvelle ligne.
- Pour envoyer votre message :
  - Appuyez sur Tab pour atteindre le bouton OK.
  - Appuyez sur Entrée.

### Lecture de la réponse

Après le traitement, une fenêtre de résultats apparaît contenant :

- "Vous avez dit :" suivi de votre message.
- "Le modèle a répondu :" suivi de la réponse.
- Un bouton "Copier" pour copier la réponse.

Si l'affichage de l'historique complet est activé, chaque échange est clairement séparé par des titres, ce qui facilite la navigation à l'aide des touches de navigation rapide de NVDA.

## Options d'affichage

Si vous préférez n'afficher que la dernière réponse au lieu de l'historique complet de la conversation :

1. Ouvrez le menu NVDA (NVDA + N).
2. Allez dans Préférences → Paramètres.
3. Sélectionnez Ask OpenRouter.
4. Décochez :
   "Afficher l'historique complet de la discussion pour les conversations continues"
5. Appuyez sur OK.

## Scripts non assignés

Les scripts suivants n'ont pas de raccourcis assignés.  
Vous pouvez les définir dans :

Préférences → Gestes de commandes → Ask OpenRouter

Scripts disponibles :

- Ouvrir le panneau des paramètres de l'extension
- Démarrer directement une nouvelle discussion
- Continuer directement une discussion existante

## Modèles gratuits, modèles payants et quotas

### Utilisation des modèles gratuits

Lorsque "Utiliser tous les modèles, y compris les payants" est décoché :

- Seuls les modèles étiquetés comme gratuits sur OpenRouter sont utilisés.
- Les modèles gratuits ont :
  - Des quotas quotidiens limités
  - Des limites de débit partagées
  - Une indisponibilité temporaire possible

L'extension alterne automatiquement entre les modèles gratuits pour améliorer la disponibilité.

### Utilisation des modèles payants

Lorsque "Utiliser tous les modèles, y compris les payants" est coché :

- L'extension utilise exactement le modèle que vous avez sélectionné.
- Cela peut inclure des modèles payants.
- Vous devez avoir suffisamment de crédits OpenRouter.
- Les limites de débit du fournisseur peuvent s'appliquer.

Les erreurs telles que :

- 402 (crédits insuffisants)
- 429 (limite de débit atteinte)
- 404 (modèle non autorisé par les paramètres de confidentialité)

sont affichées directement pour vous informer du problème.

## Rappel sur les paramètres de confidentialité

Si vous utilisez des modèles gratuits et recevez une erreur mentionnant :

> "No endpoints found matching your data policy"

Vous devrez peut-être ajuster vos paramètres de confidentialité OpenRouter :

https://openrouter.ai/settings/privacy

Assurez-vous que les points d'accès (endpoints) pour les modèles publics/gratuits sont autorisés.

## Compatibilité

- Cette extension est compatible avec les versions de NVDA allant de 2025.1 et ultérieures.

## Changements pour la version 20260221.0.0

- Ajout de la sélection manuelle de n'importe quel modèle disponible depuis le panneau des paramètres.
- Ajout de la possibilité d'utiliser des modèles payants.

## Changements pour la version 20260217.0.0

- Version initiale.
