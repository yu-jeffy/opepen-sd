---
license: cc-by-nd-4.0
---
# A Dataset of skyscrapers in the style of a city building game

## Terms and Conditions

The dataset is usable for training and experimenting with new models, but since the images are generated using OpenAI's API, as stated by them, if your project involves sensitive or controversial content, you should review their policies and terms to ensure compliance

https://openai.com/it-IT/policies/usage-policies
https://openai.com/it-IT/policies/terms-of-use

If you copy and distribute this work you have to give credit to the author of this repo and to OpenAI as the original source of the images. Furthermore if your project involves sensitive or controversial content you have to make sure you follow the terms and policies above 

## How this dataset was generated

The dataset has been created sampling 100 images from OpenAI Dall-e 3 using the official API. I checked with their support team and given that users own the output images, they are allowed to publish them anywhere including github, and they are allowed to used them as datapoints to train a new model. 

The descriptions are derived using the chat-gpt 4 API to describe the datapoints in a synthetic way and the output is then trimmed to the last period.

## What can you do with this dataset

The idea behind this dataset is: can you use images from a high quality partially restricted image generation model to improve the output of a lower quality model?

Even if you don't have a powerful GPU you can can try this yourself, using this colab notebook (the free tier T4 GPU should suffice): 

https://github.com/loulblemo/colab_diffusers_finetuning/blob/main/diffusion_finetune_skyscrapers.ipynb


