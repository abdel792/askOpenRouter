# Ask OpenRouter

* Autor(es): Abdel.

Este complemento para NVDA le permite interactuar con modelos de Inteligencia Artificial proporcionados por la plataforma OpenRouter directamente desde su lector de pantalla.

El complemento admite tanto:
* Selección aleatoria automática de modelos gratuitos
* Selección manual de cualquier modelo disponible (incluidos los de pago)

## Características principales

* Acceso rápido: abra la interfaz de chat en cualquier momento mediante un atajo global.
* Gestión de conversaciones: inicie una conversación nueva o continúe el intercambio anterior.
* Rotación inteligente de modelos gratuitos: selecciona automáticamente un modelo gratuito aleatorio para optimizar las cuotas de uso diarias.
* Selección manual de modelos: elija un modelo específico (incluidos los modelos de pago) desde el panel de configuración.
* Resultados accesibles: consulte las respuestas en una ventana clara y fácil de navegar, con la posibilidad de mostrar el historial completo.

## Configuración: obtención e instalación de su clave API

Para utilizar este complemento, debe disponer de una clave API de OpenRouter.

Incluso cuando utilice modelos gratuitos, la clave es necesaria para identificar sus solicitudes.

### 1. Cómo obtener una clave API

1. Vaya a [OpenRouter.ai](https://openrouter.ai/).
2. Cree una cuenta haciendo clic en «Sign up» (puede iniciar sesión con una cuenta de GitHub, Google o MetaMask, o con su dirección de correo electrónico).
3. Una vez iniciada la sesión, vaya a la sección «Keys» de su panel de control o acceda directamente a: https://openrouter.ai/keys
4. Haga clic en el botón «Create Key».
5. Asigne un nombre a su clave (por ejemplo: «Mi clave API de OpenRouter») y haga clic en «Create».
6. Importante: su clave solo se mostrará una vez. Cópiela inmediatamente y guárdela en un lugar seguro.

### 2. Configuración de la clave en NVDA

1. Abra el menú de NVDA (NVDA + N).
2. Vaya a Preferencias y, a continuación, a Configuración.
3. En la lista de categorías, seleccione «Ask OpenRouter».
4. Pegue su clave API en el campo «OpenRouter API Key».
5. Pulse Aceptar para guardar.

#### Mostrar la clave API

En el panel de configuración de NVDA, justo después del campo «OpenRouter API Key», encontrará una casilla de verificación denominada:

«Mostrar la clave API»

If checked, the characters of the API key become visible.
De forma predeterminada, permanecen ocultos por motivos de seguridad.

## Configuración de selección de modelos

En la categoría de configuración de Ask OpenRouter encontrará una nueva opción:

### «Usar todos los modelos, incluidos los de pago»

Esta opción controla la forma en que se seleccionan los modelos.

### Cuando la opción está DESMARCADA (comportamiento predeterminado)

* El complemento selecciona automáticamente un modelo gratuito aleatorio para cada nueva conversación.
* Va alternando entre los modelos gratuitos disponibles.
* Esto ayuda a distribuir el uso y evitar los límites de frecuencia.

### Cuando la opción está MARCADA

Cuando esta opción está habilitada, aparece automáticamente una lista de modelos disponibles debajo de la casilla de verificación.

* La lista está ordenada de forma ascendente según el precio de los tokens de entrada (coste por token de entrada), del menor al mayor.
* Solo se muestran modelos no obsoletos con proveedores válidos.

### ¿Qué puede hacer cuando esta opción está habilitada?

* Elegir cualquier modelo disponible.
* Utilizar modelos de pago (si dispone de créditos suficientes en OpenRouter).
* Seleccionar el modelo que mejor se adapte a sus necesidades.
* Seguir utilizando el mismo modelo seleccionado para sus conversaciones (sin rotación automática).

### ¿Qué es un token de entrada?

Un token de entrada representa una pequeña unidad de texto enviada al modelo (su pregunta o entrada).

Los modelos suelen facturar por separado:
* Tokens de entrada (prompt)
* Tokens de salida (respuesta)

## Cómo utilizar el complemento

### Abrir el cuadro de diálogo del chat

Pulse:

Ctrl + Alt + A

Puede cambiar este gesto en:
NVDA → Preferencias → Gestos de entrada → Ask OpenRouter

### Interfaz principal

El cuadro de diálogo contiene tres botones:

1. Nuevo chat: inicia una conversación completamente nueva.
2. Continuar chat: reanuda la conversación anterior (mantiene el historial).
3. Cerrar: cierra el cuadro de diálogo (Escape también funciona).

### Introducción del mensaje

Después de seleccionar «Nuevo chat» o «Continuar chat»:

* Aparece un campo de texto multilínea.
* Al pulsar Intro se inserta una nueva línea.
* Para enviar su mensaje:
  - Pulse Tab hasta llegar al botón Aceptar.
  - Pulse Intro.

### Lectura de la respuesta

Una vez procesada la solicitud, aparece una ventana de resultados que contiene:

* «Usted dijo:» seguido de su mensaje.
* «El modelo respondió:» seguido de la respuesta.
* Un botón «Copiar» para copiar la respuesta.

Si la visualización del historial completo está habilitada, cada intercambio aparece claramente separado mediante encabezados, lo que facilita la navegación utilizando las teclas de navegación rápida de NVDA.

## Opciones de visualización

Si prefiere mostrar únicamente la respuesta más reciente en lugar del historial completo de la conversación:

1. Abra el menú de NVDA (NVDA + N).
2. Vaya a Preferencias → Configuración.
3. Seleccione Ask OpenRouter.
4. Desmarque:
   «Mostrar el historial completo del chat en las conversaciones continuas»
5. Pulse Aceptar.

## Scripts sin asignar

The following scripts do not have gestures assigned.
Puede definirlos en:

Preferencias → Gestos de entrada → Ask OpenRouter

Scripts disponibles:

* Abrir el panel de configuración del complemento
* Iniciar directamente un nuevo chat
* Continuar directamente un chat existente

## Modelos gratuitos, modelos de pago y cuotas

### Uso de modelos gratuitos

Cuando «Usar todos los modelos, incluidos los de pago» está desmarcado:

* Solo se utilizan los modelos marcados como gratuitos en OpenRouter.
* Los modelos gratuitos tienen:
  - Cuotas diarias limitadas
  - Límites de frecuencia compartidos
  - Posibles indisponibilidades temporales

El complemento alterna automáticamente entre los modelos gratuitos para mejorar la disponibilidad.

### Uso de modelos de pago

Cuando «Usar todos los modelos, incluidos los de pago» está marcado:

* El complemento utiliza exactamente el modelo que haya seleccionado.
* Esto puede incluir modelos de pago.
* Debe disponer de créditos suficientes en OpenRouter.
* Pueden aplicarse límites de frecuencia del proveedor.

Errores como:
* 402 (créditos insuficientes)
* 429 (límite de frecuencia alcanzado)
* 404 (modelo no permitido por la configuración de privacidad)

se muestran directamente para informarle del problema.

## Recordatorio sobre la configuración de privacidad

Si utiliza modelos gratuitos y recibe un error que menciona:

> "No endpoints found matching your data policy"

Es posible que deba ajustar la configuración de privacidad de OpenRouter:

https://openrouter.ai/settings/privacy

Asegúrese de que los puntos de acceso públicos/gratuitos de los modelos estén permitidos.

## Compatibilidad ##

* Este complemento es compatible con las versiones de NVDA desde la 2025.1 en adelante.

## Cambios de la versión 20260221.0.0

* Se ha añadido la selección manual de cualquier modelo disponible desde el panel de configuración.
* Se ha añadido la posibilidad de utilizar modelos de pago.

## Cambios de la versión 20260217.0.0

* Versión inicial
