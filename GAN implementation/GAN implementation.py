import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
import os

# Generator
def build_generator():
    model = tf.keras.Sequential([
        layers.Dense(256, input_shape=(100,)),
        layers.BatchNormalization(),
        layers.LeakyReLU(alpha=0.2),
        layers.Dense(512),
        layers.BatchNormalization(),
        layers.LeakyReLU(alpha=0.2),
        layers.Dense(784, activation='sigmoid')
    ])
    return model

# Discriminator
def build_discriminator():
    model = tf.keras.Sequential([
        layers.Dense(512, input_shape=(784,)),
        layers.LeakyReLU(alpha=0.2),
        layers.Dense(256),
        layers.LeakyReLU(alpha=0.2),
        layers.Dense(1, activation='sigmoid')
    ])
    return model

# Build models
generator = build_generator()
discriminator = build_discriminator()

# Compile discriminator
discriminator.compile(optimizer=tf.keras.optimizers.Adam(0.0002, 0.5), loss='binary_crossentropy', metrics=['accuracy'])

# GAN
discriminator.trainable = False
gan_input = layers.Input(shape=(100,))
generated_image = generator(gan_input)
gan_output = discriminator(generated_image)
gan = tf.keras.Model(gan_input, gan_output)
gan.compile(optimizer=tf.keras.optimizers.Adam(0.0002, 0.5), loss='binary_crossentropy')

# Visualization function
def save_and_visualize_generated_images(epoch, generator, output_dir='generated_images'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    noise = np.random.normal(0, 1, (16, 100))  # Generate 16 random samples
    generated_images = generator.predict(noise).reshape(-1, 28, 28)
    
    fig, axes = plt.subplots(4, 4, figsize=(8, 8))
    for i, ax in enumerate(axes.flat):
        ax.imshow(generated_images[i], cmap='gray')
        ax.axis('off')
    
    plt.tight_layout()
    file_path = os.path.join(output_dir, f"epoch_{epoch}.png")
    plt.savefig(file_path)
    plt.close()
    print(f"Saved generated images at epoch {epoch} to {file_path}")

# Training
def train_gan(generator, discriminator, gan, epochs, batch_size):
    (x_train, _), _ = tf.keras.datasets.mnist.load_data()
    x_train = x_train.reshape(-1, 784).astype('float32') / 255.0

    for epoch in range(epochs):
        # Train discriminator
        real_images = x_train[np.random.randint(0, x_train.shape[0], batch_size)]
        fake_images = generator.predict(np.random.normal(0, 1, (batch_size, 100)))
        labels_real = np.ones((batch_size, 1))
        labels_fake = np.zeros((batch_size, 1))

        d_loss_real = discriminator.train_on_batch(real_images, labels_real)
        d_loss_fake = discriminator.train_on_batch(fake_images, labels_fake)

        # Train generator
        noise = np.random.normal(0, 1, (batch_size, 100))
        misleading_labels = np.ones((batch_size, 1))
        g_loss = gan.train_on_batch(noise, misleading_labels)

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, D Loss: {d_loss_real[0] + d_loss_fake[0]}, G Loss: {g_loss}")
            save_and_visualize_generated_images(epoch, generator)

# Train the GAN
train_gan(generator, discriminator, gan, epochs=1000, batch_size=32)
