# csv-to-md <br/>
Basic timelog converter from .csv to .md <br/> <br/>
The script is intented for scanning time logs of a single person <br/> <br/>
**IN ORDER TO RUN THE SCRIPT YOU NEED TO HAVE PYTHON INSTALLED** <br/> <br/>
You can install it from the *official* python [SITE](https://www.python.org) <br/>
**How to use the script**
1. Go to toggl track and press on **Reports** <br/>
![image](https://user-images.githubusercontent.com/48327048/190915337-5bdd1f88-a4ed-4d22-94bd-adc5f1558825.png) <br/>
2. Then press on **Detailed** <br/>
![image](https://user-images.githubusercontent.com/48327048/190915292-054cff9f-65cc-4932-842c-69e0f4e19240.png) <br/>
3. And press **Download CSV** <br/>
![image](https://user-images.githubusercontent.com/48327048/190915622-bfd77363-14f8-483c-b9c2-3dcbb8b00262.png) <br/>
4. You should see something like this <br/>
![image](https://user-images.githubusercontent.com/48327048/190915666-27c95ae9-b44d-42c2-bc85-69e177a6dfe6.png) <br/>
Keep in mind that it is ***crucial*** for your file name to be similar to mine's <br/>
Because the program also reads ***FILE NAME*** for more accurate output <br/>
5. And when you will be **running the script** make sure that .csv file is in the same directory / folder as main.py <br/>
![image](https://user-images.githubusercontent.com/48327048/190915752-eef0f59d-e859-4a5f-a3e3-d870559bb57e.png) <br/>
6. In order to run the script, we will launch it from terminal <br/>
![image](https://user-images.githubusercontent.com/48327048/190916442-9dbcac00-f762-435f-a6d8-08baf7791a82.png) <br/>
7. Press on the field where file location / folder name is being saved (in my case it's **"converter"**), delete the entire **path** and write **cmd** <br/>
![image](https://user-images.githubusercontent.com/48327048/190916549-f9de03e5-2dfd-40d9-95aa-aab184ba65ac.png) <br/>
8. Command prompt should open up and then just type **python main.py** <br/>
9. In the console you should see that ".md file was created successfully!" and "output_data.md" file saved in your folder <br/>
10. The **output_data.md** should look something like this <br/> <br/>
![image](https://user-images.githubusercontent.com/48327048/190916761-1fb67f6f-3819-493c-82ce-13f5d4663302.png) <br/>
Keep in mind that it says **"Week 2"**, because I'm counting which week is it from certain date (2022-09-05) <br/> 
If you want to change the starting date, you can do it in 48 line <br/> <br/>

Credits go to [Jesource](https://github.com/Jesource), it was his idea for such tool <br/>
Link to his [implementation](https://github.com/Jesource/Log-converter/tree/08171d9d1592053ef3716396e0ba13e0abfbad4c) of the converter

