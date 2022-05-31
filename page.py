
import instaloader
 
ig = instaloader.Instaloader()
DP = input("luisrjean : ")
 
ig.download_profile(DP , profile_pic_only=True)
print("Your Image is Downloaded")