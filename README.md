# Quiz-Mania-Project-1_V2
this is the DJango version of the QuizMania project build in CGI

## Steps to Add a new TestPage On Website
1. The file should be made in ```xml``` format given in ```media``` folder
2. As long as The test box can be seen on website
    1. Save the test page file with same name as test with its level ```docker_b.xml```
    2. Run ```python3 SetQuestions.py```
    3. When prompted enter the table name ```TestTime_docker_b```
    4. When prompted enter the test file name ```docker_b.xml```
    5. Enter and test information will be added to database
3. Reload the server and system settings by
    ```shell
    $sudo systemctl daemon-reload
    $sudo systemctl restart gunicorn
    $sudo service nginx restart
    ```
