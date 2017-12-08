/*
 * (C) Copyright 2017-2019 ElasTest (http://elastest.io/)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
package io.elastest.eds.test.e2e;

import static java.lang.invoke.MethodHandles.lookup;
import static java.util.concurrent.TimeUnit.SECONDS;
import static org.slf4j.LoggerFactory.getLogger;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.chrome.ChromeDriver;
import org.slf4j.Logger;

import io.elastest.eds.test.base.EdsBaseTest;
import io.github.bonigarcia.SeleniumExtension;import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * E2E EDS test.
 *
 * @author Boni Garcia (boni.garcia@urjc.es)
 * @since 0.1.1
 */
@Tag("e2e")
@DisplayName("E2E tests of EDS through TORM")
@ExtendWith(SeleniumExtension.class)
public class EdsSupportServiceE2eTest extends EdsBaseTest {

    final Logger log = getLogger(lookup().lookupClass());

    @Test
    @DisplayName("EDS as support service")
    void testSupportService(ChromeDriver driver) throws Exception {
        log.info("Navigate to TORM and start support service");
        driver.manage().window().setSize(new Dimension(1024, 1024));
        driver.manage().timeouts().implicitlyWait(5, SECONDS); // implicit wait
        # navigate to the application home page
        driver.get("http://www.google.com")
        driver.get(tormUrl);
        startTestSupportService(driver, "EDS");

        // Get EBS Service Spark Docker Container Id
        String edsInstances = driver.findElement(By.xpath("//div[contains(string(), 'Instance Id:')]")).getText();
        String[] lines = edsInstances.split("\\r?\\n");
        Boolean tagJustFound = false;
        String containerId = "";
        String tag = "Instance Id:";
        for (String line : lines) {
                // First find a tag line containing the literal "Instance Id" used in the GUI
                if(line.contains(tag)) tagJustFound = true;
                // The next line after the tag line is the value of service Id
                if(!line.contains(tag) && tagJustFound) {
                        tagJustFound = false;
                        // Construct the docker container Id based on the service instance Id
                        containerId = line.replace("-", "")+"_eds_1";
                }
        }

        // Test that the container id has been found
        Boolean containerFound = !containerId.equals("");
        if (containerFound) {
                log.info("*** EBS Container Id = ["+containerId+"]");
        } else {
                log.error("*** EBS Container Id not found !!!");
        }
        assertTrue(containerFound);

        // We will execute a command inside the EDS docker container
        boolean success = false;
        try {
                String fileName = "test_" + new SimpleDateFormat("yyyyMMddHHmm'.txt'").format(new Date());

                // Start a process to execute the command
                String[] command = {"docker", "exec", "-i", containerId, "eds", "fs", "copyFromLocal"+fileName};
                ProcessBuilder pb = new ProcessBuilder(command);
                Process p = pb.start();

                // Get output from the process
                InputStream is = p.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader processOutput = new BufferedReader(isr);

                InputStream errorStream = p.getErrorStream();
                InputStreamReader inputStreamReader = new InputStreamReader(errorStream);
                BufferedReader processErrorOutput = new BufferedReader(inputStreamReader);

                String output;

                while( processErrorOutput.ready() &&
                   (output = processErrorOutput.readLine()) != null) {
                        log.info("*** ERROR OUTPUT  : "+output);
                }

                while ((output = processOutput.readLine()) != null) {
                        log.info("*** NORMAL OUTPUT : "+output);
                        //if (output.contains("Copied file:///opt/spark/README.md to /hdfs")) success = true;
                }

                // Wait for the process to finish
                p.waitFor();

                // Clean up
                processErrorOutput.close();
                processOutput.close();

            } catch (Exception e) {
                e.printStackTrace();
            }

            // Log test result
            if (success) {
                log.info("*** Test Result: Write to EDS SUCCEEDED");
            } else {
                log.info("*** Test Result: Write to EDS FAILED");
            }

            // Check test result
            assertTrue(success);

    }

}
