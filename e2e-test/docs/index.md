# End-to-end tests of ElasTest Device Emulator Service (EDS)

This project contains several end-to-end (E2E) test aimes to verify the correctness of the ElasTest Device Emulator Service (EDS) through the Test Orchestration and Recommendation Manager (TORM).

In order to implement these test we use [Selenium WebDriver], which is an web testing framework to automate the navigation and verification of web applications using a given test logic. In this case, we use Java to implement the test, and [JUnit 5] as base testing framework. In order to ease the management on web browsers in the tests, we use an open source JUnit 5 extension called [selenium-jupiter].

E2E tests for EDS are going to be implemented as support service. The following sections of this document summarizes the main parts of these tests.

## Use of EDS as support service

This test in implemented in the test [EusSupportServiceE2eTest.java]. As can be seen, this class extends a parent class: [EdsBaseTest.java]. This parent class contains a common setup for tests (annotated with JUnit 5's `@BeforeEach`):

```java
    @BeforeEach
    void setup() {
        String etmApi = getProperty("etEmpApi");
        if (etmApi != null) {
            tormUrl = etmApi;
        }
        log.info("Using URL {} to connect to TORM", tormUrl);
    }
```

This piece of code read the JVM argument called `etEmpApi` to find out the TORM URL. The value of this argument is supposed to be configured previously to the test execution, and this is done in the [Jenkins pipeline]:

```
stage ("E2E tests") {
   try {
      sh "cd e2e-test; mvn -B clean test -DetEmpApi=http://${etEmpApi}:8091/"
   } catch(e) {
      sh 'docker ps | awk "{print $NF}" | grep eds | xargs docker logs'
   }
   step([$class: 'JUnitResultArchiver', testResults: '**/target/surefire-reports/TEST-*.xml'])
}
```

The structure of the actual test (method annotated with JUnit 5's annotation `@Test` in ) is as follows:


```java
@Tag("e2e")
@DisplayName("E2E tests of EDS through TORM")
@ExtendWith(SeleniumExtension.class)
public class EdsSupportServiceE2eTest extends EdsBaseTest {

    final Logger log = getLogger(lookup().lookupClass());

    @Test
    @DisplayName("EDS as support service")
    void testSupportService(ChromeDriver driver) throws Exception {
        // Test logic
    }

}
```

In addition to the JUnit 5 annotation for tagging and naming (`@Tag` and `@DisplayName`), we see that we are using the [selenium-jupiter] extension, declaring it using the annotation `@ExtendWith(SeleniumExtension.class)`. Thanks to the dependency injection feature of JUnit 5, the extension creates propoer WebDriver instances for tests. In this case, simply declaring this instance in the test arguments (in this case, `ChromeDriver driver`), we can use a browser (in this case Chrome) in our test is a seamless way. The Jenkins job is configured properly to use a Docker image ([elastest/ci-docker-e2e]) in which several browsers (Chrome and Firefox) are ready to be used by tests.

Regarding the test logic, it is basically an specific application of Selenium WebDriver to test the web GUI provided by the TORM. For instance, the first part of the test is the following:

```java
        log.info("Navigate to TORM and start support service");
        driver.manage().window().setSize(new Dimension(1024, 1024));
        driver.manage().timeouts().implicitlyWait(5, SECONDS); // implicit wait
        driver.get(tormUrl);
        startTestSupportService(driver, "EDS");
```

In this snippet, we see that we force the size of the browser windows, we configure a global implicit wait of 5 seconds (to wait for elements to be located by WebDriver), then we open the TORM URL, and then we use the parent method `startTestSupportService` to start the support service identified by the label `EDS`.

The next part is specific for the EDS GUI. First, we click on the Chrome radio button and start a live session:

```java
        log.info("Select Chrome as browser and start session");
        driver.findElement(By.id("chrome_radio")).click();
        driver.findElement(By.id("start_session")).click();

```

Then we need to create an explicit wait for the iframe to be available. This operation can be time-consuming, since the Chrome Docker image needs to be downloaded, and the first time we make a pull (and this is very likely to happen in Jenkins) can last a couple of minutes.

```java
        log.info("Wait to load browser");
        By iframe = By.id("eds_iframe");
        WebDriverWait waitBrowser = new WebDriverWait(driver, 240); // seconds
        waitBrowser.until(visibilityOfElementLocated(iframe));
        driver.switchTo().frame(driver.findElement(iframe));
```

After that, we move to the EDS iframe, interacting with the HTML5 Canvas in which the browser session is displayed to the user. The simulate a 5 seconds session (just to be able to make a brief recording, which is used in the next steps). 

```java
        log.info("Click browser navigation bar and navigate");
        WebElement canvas = driver.findElement(By.id("noVNC_canvas"));
        new Actions(driver).moveToElement(canvas, 142, 45).click().build()
                .perform();
        canvas.sendKeys("elastest.io" + RETURN);
        int navigationTimeSec = 5;
        log.info("Waiting {} secons (simulation of manual navigation)",
                navigationTimeSec);
        sleep(SECONDS.toMillis(navigationTimeSec));
        log.info("Screenshot (in Base64) after manual navigation:\n{}",
                getBase64Screenshot(driver));

```

Notice also that a method of the parent class is called at the end of this snippet: `getBase64Screenshot`. This is basically used for logging and debugging purposes. The objective is able to trace to E2E tests, which as you can see, are difficult per nature (in fact making this process more easy for developers and testers is one of the main objectives of ElasTest). At this stage of the project, we use the capability provided by Selenium WebDriver to get screeshots of the web application under test, logging it as a Base64 string. This string can be later recover from the Jenkins logs, and this string can be directly pasted in a web browsers as a PNG picture. In this test, the first screenshot would be as follows:   

![EDS screenshot examaple](img/eds-e2e-screenshot.png)

The rest of the test follows the same guidelines, i.e. the use of WebDriver API to interact with the GUI, explicit waits when needed, and logging screenshots for debugging purposes. 



[Selenium WebDriver]: http://www.seleniumhq.org/projects/webdriver/
[JUnit 5]: http://junit.org/junit5/docs/current/user-guide/
[selenium-jupiter]: https://bonigarcia.github.io/selenium-jupiter/
[EdsSupportServiceE2eTest.java]: https://github.com/elastest/elastest-user-emulator-service/blob/master/e2e-test/src/test/java/io/elastest/eds/test/e2e/EdsSupportServiceE2eTest.java
[EdsTJobE2eTest.java]: https://github.com/elastest/elastest-user-emulator-service/blob/master/e2e-test/src/test/java/io/elastest/eds/test/e2e/EdsTJobE2eTest.java
[EdsseTest.java]: https://github.com/elastest/elastest-user-emulator-service/blob/master/e2e-test/src/test/java/io/elastest/eds/test/base/EdsBaseTest.java
[Jenkins pipeline]: https://github.com/elastest/elastest-user-emulator-service/blob/master/e2e-test/Jenkinsfile
[elastest/ci-docker-e2e]: https://hub.docker.com/r/elastest/ci-docker-e2e/
