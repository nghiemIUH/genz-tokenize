from .model_utils import PretrainModel, LossClassification
import tensorflow as tf


class TrainArg:
    def __init__(
        self,
        epochs: int = 10,
        batch_size: int = 32,
        learning_rate: float = 1e-4

    ) -> None:
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate


class Trainner:
    def __init__(
        self,
        model: PretrainModel,
        arg: TrainArg,
        dataset_train: tf.data.Dataset,
        dataset_val: tf.data.Dataset = None,

    ) -> None:
        self.model = model
        self.dataset_train = dataset_train
        self.dataset_val = dataset_val
        self.arg = arg

        if self.model.__str__() == 'cls':
            self.loss = LossClassification()
        self.optimizer = tf.keras.optimizers.Adam(
            learning_rate=self.arg.learning_rate)

        self.model.compile(loss=self.loss, optimizer=self.optimizer)

    def train(self) -> None:
        self.model.fit(self.dataset_train, epochs=self.arg.epochs,
                       validation_data=self.dataset_val)
