El reconocimiento automatico de voz es basicamente una forma de identificar la voz y transcribirla a un texto.

En este capitulo veremos como hacer una tarea de deteccion automatica de voz con el modelo (distil-whisper/distil-small.en)[https://huggingface.co/distil-whisper/distil-small.en]

Whisper fue entrenado por OpenAI, es uno de los mejores modelos para este task.
Este modelo fue entrenado con una vasta cantidad de data y audio transcrito. Aproximadamente de 680000 horas de audio.
Adicional a este dato, casi 117000 horas de este audio es en otros idiomas (que no son Ingles)
Esto es muy util, casi pueden aplicarse como 96 idiomas para identificar con este modelo.

Sin embargo, para esta clase usaremos el modelo pequeño, que basicamente entiende ingles a un buen nivel y tiene respuestas más rapidas.

Hay que tener encuenta el simple_rate que tiene el modelo y que tienen nuestros audios para probar.

