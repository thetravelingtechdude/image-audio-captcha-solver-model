# image-audio-captcha-solver-model

Audio Captcha current accuracy - 95%

Steps taken in preprocessing to improve the model accuracy:

	1. Pre-processing as audio:	
		a) Dimension reduction of the audio using Mel Spectrogram
		c) Converting amplitude into decibels using librosa.amplitude_to_db
		d) Plotting audio as a spectrogram in greyscale (dimensions - 128 x 64)
	
	4. Pre-processing as image:
		a) Auto-contrasting (cutoff = 10)
		


