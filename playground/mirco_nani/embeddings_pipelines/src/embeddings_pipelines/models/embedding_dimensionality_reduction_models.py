import numpy as np
from embeddings_pipelines.model.models import EmbeddingDimensionalityReductionModel

class DummyEmbeddingDimensionalityReductionModel(EmbeddingDimensionalityReductionModel):
    def __init__(self, reduced_embedding_size: int):
        """this embedder takes the first reduced_embedding_size dimensions of a given embedding

        Args:
            embedding_size (int): the size of the output embedding
        """
        self.reduced_embedding_size = reduced_embedding_size

    
    def build(self):
        pass


    def predict(self, embedding:np.array) -> np.array:
      """Applies the built model to reduce an embedding

      Args:
          embedding (np.array): A 1-D numpy array of floats, being the embedding to reduce

      Returns:
          np.array: a 1-D numpy array with dimensions lower than the input embedding
      """
      return embedding[:self.reduced_embedding_size]


    def dispose():
        pass