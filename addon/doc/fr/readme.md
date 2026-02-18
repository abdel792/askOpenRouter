Demander à OpenRouter (Ask OpenRouter)
Demander à OpenRouter (Ask OpenRouter)

Cet extension pour NVDA vous permet d'interagir avec les modèles d'intelligence artificielle gratuits proposés par la plateforme OpenRouter directement depuis votre lecteur d'écran.

## Fonctionnalités principales

* Accès rapide à une interface de chat via un raccourci clavier.
* Gestion des conversations (nouvelle ou poursuite d'un échange).
* Sélection intelligente et aléatoire des modèles gratuits pour optimiser les quotas.
* Affichage des réponses dans une fenêtre lisible avec historique.

## Configuration : Obtenir et installer votre clé API

Pour fonctionner, l'extension nécessite une clé API provenant d'OpenRouter. Bien que l'accès aux modèles soit gratuit, la clé est indispensable pour identifier vos requêtes.

### 1\. Comment obtenir une clé API gratuite ?

1. Rendez-vous sur le site [OpenRouter.ai](https://openrouter.ai/).
2. Créez un compte en cliquant sur le bouton **"Sign up"** (vous pouvez utiliser un compte GitHub, Google, MetaMask ou une adresse e-mail).
3. Une fois connecté, accédez à la section **"Keys"** (Clés) dans votre tableau de bord ou via l'adresse : [https://openrouter.ai/keys](https://openrouter.ai/keys).
4. Cliquez sur le bouton **"Create Key"**.
5. Donnez un nom à votre clé (par exemple : "Ma première clé API OpenRouter") et validez.
6. **Important :** Votre clé s'affiche une seule fois. Copiez-la immédiatement et sauvegardez-la dans un endroit sûr.
### 2\. Configurer la clé dans NVDA

1. Ouvrez le menu NVDA (touche NVDA + N).
2. Allez dans **Préférences**, puis **Paramètres**.
3. Dans la liste des catégories, recherchez **"Demander à OpenRouter"**.
4. Tabulez une seule fois, vous êtes sur le champ **"Clé API OpenRouter"**, collez-y votre clé (les caractères sont masqués par défaut).
5. Validez en appuyant sur le bouton **OK**.

#### **Remarque**
Dans le panneau des paramètres de NVDA, juste après le champ **"Clé API OpenRouter"**, il y a une case à cocher intitulé **"Afficher la clé API"**.

Si vous cochez cette case, les caractères de la clé API devraient apparaitre devant vous, au cas où vous souhaiteriez la visualiser, ou la copier à nouveau.

Par défaut, les caractères de la clé sont toujours masqués, par mesure de sécurité.

## Utilisation de l'extension

### Ouvrir l'interface de dialogue

À tout moment, vous pouvez ouvrir l'interface de chat proposée par l'extension en utilisant le raccourci suivant :

* **Alt + Ctrl + A**

Vous pouvez modifier ce geste dans le menu des préférences de NVDA, dans le sous-menu **"Gestes de commandes"**, et plus précisément, dans la catégorie **"Demander à OpenRouter"**.

### L'interface principal

Une boîte de dialogue s'ouvre avec trois options :

1. **Créer un nouveau chat** : Pour démarrer une conversation de zéro.
2. **Continuer un chat** : Pour reprendre la discussion là où vous l'avez laissée (l'historique est conservé pour le modèle).
3. **Fermer** : Pour quitter la boîte de dialogue (vous pouvez aussi utiliser la touche **Échappe**).

### Saisir votre question

Une fois que vous avez choisi de créer ou continuer un chat, un champ de saisie apparaît :

* **Champ multiligne** : Ce champ vous permet d'écrire de longs messages. Comme il est multiligne, la touche **Entrée** crée un saut de ligne.

#### **Envoi du message** :
Pour envoyer votre message, appuyez sur **Tabulation** pour atteindre le bouton **OK**, puis validez avec **Entrée**.

### Lecture de la réponse

Après un court instant de traitement, une fenêtre de résultat s'affiche. Elle contient :

* Une section **"Vous avez dit :"** rappelant votre question.
* Une section **"Le modèle a répondu :"** contenant la réponse de l'IA.
* Un bouton **"Copyer"** pour copier la réponse reçue.

Si la conversation se poursuit, l'historique affichera les échanges précédents en utilisant  chacune de ces entêtes pour faciliter la lecture avec les touches de navigation rapide de NVDA.

### **Remarque**
Si vous préférez n'avoir toujours qu'une seule réponse à vos questions posées, vous pouvez configurer l'extension afin qu'elle n'affiche que la dernière réponse reçue.

Pour ce faire, procédez comme suit :

1. Ouvrez le menu NVDA (touche NVDA + N).
2. Allez dans **Préférences**, puis **Paramètres**.
3. Dans la liste des catégories, recherchez **"Demander à OpenRouter"**.
4. Tabulez jusqu'à atteindre la case à cocher **"Afficher l'historique complet pour les discussions continues"**, puis décochez la case avec espace.
5. Validez en appuyant sur le bouton **OK**.

## Scripts non attribués

Les scripts suivants n'ont pas de gestes attribués, vous pouvez les définir depuis le menu des préférences, sous-menu "Gestes de commandes", dans la catégorie "Demander à OpenRouter".

* Un script permettant d'ouvrir le panneau des paramètres de l'extension.
* Un script permettant d'ouvrir une boîte de dialogue pour créer un nouveau chat.
* Un script permettant d'ouvrir une boîte de dialogue pour continuer un chat existant.

## Quotas et modèles gratuits

### Limites d'utilisation

L'extension utilise exclusivement les modèles listés comme "gratuits" par OpenRouter. Veuillez noter que :

* Les modèles gratuits disposent d'un **quota limité par jour** (nombre de messages maximum).
* Il est recommandé de les utiliser avec modération pour ne pas épuiser votre limite quotidienne trop rapidement.

### Rotation aléatoire

Pour vous aider à ne pas saturer le quota d'un seul modèle, l'extension inclut une fonctionnalité de **sélection aléatoire**. À chaque nouvelle question, l'extension analyse la liste des modèles gratuits actuellement disponibles sur OpenRouter et en choisit un au hasard. Cela permet de répartir la charge et d'augmenter vos chances d'obtenir une réponse même si un modèle particulier est momentanément saturé.

