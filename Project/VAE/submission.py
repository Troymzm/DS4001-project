import torch
import torch.nn as nn
import torch.nn.functional as F

# TODO: 2.2 Your VAE model here!
class VAE(nn.Module):
    """
    This model is a VAE for MNIST, which contains an encoder and a decoder.
    
    The encoder outputs mu_phi and log (sigma_phi)^2
    The decoder outputs mu_theta
    """
    def __init__(self, input_dim=784, hidden_dim=400, latent_dim=20):
        """
        You should define your model parameters and the network architecture here.
        """
        super(VAE, self).__init__()
        
        # TODO: 2.2.1 Define your encoder and decoder
        # Encoder
        # Output the mu_phi and log (sigma_phi)^2
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=4, stride=2, padding=1),  # 28x28 -> 14x14
            nn.LeakyReLU(0.2),
            nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=1),  # 14x14 -> 7x7
            nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),  # 7x7 -> 7x7
            nn.LeakyReLU(0.2),
            nn.Flatten(),  # 7x7x128 = 6272
            nn.Linear(6272, hidden_dim),
            nn.LeakyReLU(0.2)
        )
        # raise ValueError("Not Implemented yet!")

        # Output layers for mean and log variance
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

        # Decoder
        # Output the recon_x or mu_theta
        self.decoder_input = nn.Linear(latent_dim, 7 * 7 * 128)
        
        self.decoder = nn.Sequential(
            nn.Unflatten(1, (128, 7, 7)),
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=1, padding=1),
            nn.LeakyReLU(0.2),
            nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.ConvTranspose2d(32, 1, kernel_size=4, stride=2, padding=1),
            nn.Sigmoid()
        )
        # raise ValueError("Not Implemented yet!")

    def encode(self, x):
        """ 
        Encode the image into z, representing q_phi(z|x) 
        
        Args:
            - x: the input image, we have to flatten it to (batchsize, 784) before input

        Output:
            - mu_phi, log (sigma_phi)^2
        """
        # TODO: 2.2.2 finish the encode code, input is x, output is mu_phi and log(sigma_theta)^2
        h = self.encoder(x)
        mu = self.fc_mu(h)
        log_var = self.fc_logvar(h)
        # raise ValueError("Not implemented yet!")
        return mu, log_var

    def reparameterize(self, mu, log_var):
        """ Reparameterization trick """
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z, labels):
        """ 
        Decode z into image x

        Args:
            - z: hidden code 
            - labels: the labels of the inputs, useless here
        
        Hint: During training, z should be reparameterized! While during inference, just sample a z from random.
        """
        # TODO: 2.2.3 finish the decoding code, input is z, output is recon_x or mu_theta
        # Hint: output should be within [0, 1], maybe you can use torch.sigmoid()
        h = self.decoder_input(z)
        recon_x = self.decoder(h)
        # raise ValueError("Not Implemented yet!")
        return recon_x

    def forward(self, x, labels):
        """ x: shape (batchsize, 28, 28) labels are not used here"""
        # TODO: 2.2.4 passing the whole model, first encoder, then decoder, output all we need to cal loss
        # Hint1: all input data is [0, 1], 
        # and input tensor's shape is [batch_size, 1, 28, 28], 
        # maybe you have to change the shape to [batch_size, 28 * 28] if you use MLP model using view()
        # Hint2: maybe 3 or 4 lines of code is OK!
        # x = x.view(-1, 28 * 28)
        mu, log_var = self.encode(x)
        z = self.reparameterize(mu, log_var)
        recon_x = self.decode(z, labels)
        # raise ValueError("Not Implemented yet!")
        return recon_x, mu, log_var

# TODO: 2.3 Calculate vae loss using input and output
def vae_loss(recon_x, x, mu, log_var, var=0.5):
    """ 
    Compute the loss of VAE

    Args:
        - recon_x: output of the Decoder, shape [batch_size, 1, 28, 28]
        - x: original input image, shape [batch_size, 1, 28, 28]
        - mu: output of encoder, represents mu_phi, shape [batch_size, latent_dim]
        - log_var: output of encoder, represents log (sigma_phi)^2, shape [batch_size, latent_dim]
        - var: variance of the decoder output, here we can set it to be a hyperparameter
    """
    # TODO: 2.3 Finish code!
    # Reconstruction loss (MSE or other recon loss)
    # KL divergence loss
    # Hint: Remember to normalize of batches, we need to cal the loss among all batches and return the mean!
    recon_loss = F.mse_loss(recon_x.view(-1, 28 * 28), x.view(-1, 28 * 28), reduction='sum') / (2 * var)
    kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
    loss = (recon_loss + kl_loss) / x.size(0)
    # raise ValueError("Not Implemented yet!")
    return loss

# TODO: 3 Design the model to finish generation task using label
class GenModel(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=400, latent_dim=20, num_classes=10):
        super(GenModel, self).__init__()
        
        self.num_classes = num_classes

        self.encoder = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=4, stride=2, padding=1),  # 28x28 -> 14x14
            nn.LeakyReLU(0.2),
            nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=1),  # 14x14 -> 7x7
            nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),  # 7x7 -> 7x7
            nn.LeakyReLU(0.2),
            nn.Flatten(),  # 7x7x128 = 6272
            nn.Linear(6272, hidden_dim),
            nn.LeakyReLU(0.2)
        )
       
        self.fc_mu = nn.Linear(hidden_dim + num_classes, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim + num_classes, latent_dim)

        self.decoder_input = nn.Linear(latent_dim + num_classes, 7 * 7 * 128)
        
        self.decoder = nn.Sequential(
            nn.Unflatten(1, (128, 7, 7)),
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=1, padding=1),
            nn.LeakyReLU(0.2),
            nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.ConvTranspose2d(32, 1, kernel_size=4, stride=2, padding=1),
            nn.Sigmoid()
        )

    def encode(self, x, labels):
        h = self.encoder(x) 
        labels_onehot = F.one_hot(labels, num_classes=self.num_classes).float()
        h_cat = torch.cat([h, labels_onehot], dim=1)
        mu = self.fc_mu(h_cat)
        log_var = self.fc_logvar(h_cat)
        return mu, log_var

    def reparameterize(self, mu, log_var):
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z, labels):
        if labels.dim() == 0:
            labels = labels.unsqueeze(0)
        labels_onehot = F.one_hot(labels, num_classes=self.num_classes).float()
        z_cat = torch.cat([z, labels_onehot], dim=1)
        h = self.decoder_input(z_cat)
        recon_x = self.decoder(h)
        return recon_x

    def forward(self, x, labels):
        mu, log_var = self.encode(x, labels)
        z = self.reparameterize(mu, log_var)
        recon_x = self.decode(z, labels)
        return recon_x, mu, log_var

    def vae_loss(recon_x, x, mu, log_var, var=0.5):
        recon_loss = F.mse_loss(recon_x.view(-1, 28 * 28), x.view(-1, 28 * 28), reduction='sum') / (2 * var)
        kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
        loss = (recon_loss + kl_loss) / x.size(0)
        return loss