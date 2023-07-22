from mlforkids import MLforKidsImageProject

# treat this key like a password and keep it secret!
key = "a4e85d90-283a-11ee-8c07-03302dfbe941254fed93-e305-46fc-b3c1-69cd462647da"

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("mlforkid-p1/1200px-Phat_Thai_kung_Chang_Khien_street_stall.jpg")

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))