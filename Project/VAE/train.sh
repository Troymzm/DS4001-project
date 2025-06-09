python train.py \
--task VAEwolabel \
--epochs 50 \
--batch_size 1024 \
--lr 5e-3 \
--save_dir model_Conv3_50_1024_5e-3_20_0.25 \
--latent_dim 20 \
--var 0.25;
echo "job end"