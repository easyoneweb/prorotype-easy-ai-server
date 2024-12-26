# from stable_diffusion_cpp import StableDiffusion
#
# def progress(step: int, steps: int, time: float):
#     print('Completed step: {} of {}'.format(step, steps))
#
# def get_image():
#     # SD3.5
#     stable_diffusion = StableDiffusion(
#         model_path='models/sd/sd3.5_large.safetensors',
#         clip_l_path='models/sd/clip_l.safetensors',
#         clip_g_path='models/sd/clip_g.safetensors',
#         t5xxl_path='models/sd/t5xxl_fp16.safetensors',
#     )
#
#     # SD3.5 TXT_TO_IMG
#     output = stable_diffusion.txt_to_img(
#         prompt='a lovely cat holding a sign says "Stable diffusion 3.5 Large"',
#         width=1024,
#         height=1024,
#         cfg_scale=4.5,
#         sample_method='euler'
#     )
#
#     # FLUX
#     # stable_diffusion = StableDiffusion(
#     #     diffusion_model_path='models/sd/flux1-dev-q4_0.gguf',
#     #     clip_l_path='models/sd/clip_l.safetensors',
#     #     t5xxl_path='models/sd/t5xxl_fp16.safetensors',
#     #     vae_path='models/sd/ae.safetensors',
#     #     # vae_decode_only=True
#     # )
#
#     #FLUX_TXT_TO_IMG
#     # output = stable_diffusion.txt_to_img(
#     #     prompt='business class black car with snowy mountains in background',
#     #     sample_steps=4,
#     #     cfg_scale=1.0,
#     #     sample_method='euler',
#     #     progress_callback=progress
#     # )
#
#     # FLUX_IMG_TO_IMG
#     # input_image = '02.png'
#     #
#     # output = stable_diffusion.img_to_img(
#     #     prompt='держит в руках живую лошадку',
#     #     image=input_image,
#     #     strength=0.4
#     # )
#
#     output[0].save('output.png')
#     return 'done'