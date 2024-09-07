Aqui haremos un poco de sentence similarity, similaridad entre oraciones.
Sentence similarity mide cuanto de similitud tiene un texto comparado con otro

Esta tarea es particularmente util para la recuperacion de informacion o agrupamiento de textos.

Let's go!


Usaremos el modelo: [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

Tambien se puede acceder al API Inference de HuggingFace


Un poquito de background
Este modelo fue sacado a la luz por google, pero fue porque hizo como una hackathon para la comunidad donde ellos hicieron fine tuning y entrenamiento y ahi sacaron este modelo jaja
Bueno
Lo que hace el modelo es practicamente convertir el texto en vectores (embeddings), capturando la informacion semántica
Y luego hace la similitud

Para hacer la similitud usa: "cosine similarity"


