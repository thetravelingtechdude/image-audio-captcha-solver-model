Audio Captcha current accuracy - 95%

Steps taken in preprocessing to improve the model accuracy:

	1. Pre-processing as audio:	
		a) Dimension reduction of the audio using Mel Spectrogram
		c) Converting amplitude into decibels using librosa.amplitude_to_db
		d) Plotting audio as a spectrogram in greyscale (dimensions - 128 x 64)
	
	4. Pre-processing as image:
		a) Auto-contrasting (cutoff = 10)
		

Audio Captcha Model Training Method:

Number of Audio files	Epoch	Accuracy
      20000		  2	  12%
      20000		  2	  40%
      40000		  2	  50.10%
      40000		  4	  66%
      40000		  6	  71.187%





