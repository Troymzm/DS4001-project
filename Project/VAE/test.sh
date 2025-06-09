python inference.py \
--task VAEwolabel \
--checkpoint_path ./model_Conv3_50_1024_5e-3_20_0.25/epoch_50.pth \
--save_dir ./VAEwolabel/model_Conv3_50_1024_5e-3_20_0.25 \
--latent_dim 20;
echo "job end"