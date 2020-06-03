# implement evaluvation function to check the prediction result and view summary report
#Note:
#   1. Do not scramble while generating the captcha images
#   2. place the file in the project folder where train.py is present
#   3. use the command python Evaluvator.py --captcha-length 5  --predicted-output stuff.txt

import argparse

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--captcha-length', help='Model name to use for classification', type=int)
    parser.add_argument('--predicted-output', help='Model name to use for classification', type=str)
    argument = parser.parse_args()

    if argument.captcha_length is None:
        print("kindly specify the number of characters used to create the captcha")
        exit(1)

    if argument.predicted_output is None:
        print("kindly specify the file that contains predected results")
        exit(1)

    total = 0
    success = 0
    failure = 0

    with open(argument.predicted_output) as f:
        results = f.readlines()
        results = [x.strip() for x in results]
        total = len(results)

        for result in results:
            resultArray = result.split('.mp3,')
            if(resultArray[0] == resultArray[1]):
                success += 1
            else:
                failure += 1

        print("Total number of image captchas taken for prediction: " + str(total))
        print("Number of correct predictions: "+ str(success))
        print("Number of wrong predictions: "+ str(failure))
        accuracy = (success/total)*100
        print("The accuracy of the model is "+ str(accuracy) + "%")

if __name__ == '__main__':
    run()