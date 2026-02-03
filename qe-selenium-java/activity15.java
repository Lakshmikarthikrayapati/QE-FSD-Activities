package demos;


import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.WebDriverWait;


public class activity15 {
public static void main(String[] args) {
    WebDriver driver = new FirefoxDriver();
    WebDriverWait wait = new WebDriverWait(driver,Duration.ofSeconds(seconds: 10));
    driver.get("https://training-support.net/webelements/dynamic-attributes");
    System.out.println("Title of the page: " + driver.getTitle());
    System.out.println(driver.getTitle());
    WebElement fullname = driver.findElement(By.xpath("//input[@id='full-name-056c']"));
    WebElement email = driver.findElement()
    By.cssSelector("input[id$='email']")
    WebElement date = driver.findElement(By.xpath("//input[contains[@name, 'event-date')]"));
    WebElement textArea = driver.findElement(By.xpath("//textarea[contains@id,'additional-details')]"));
    fullName.sendKeys("admin");
    email.sendKeys("abc@xyz.com");
    date.sendKeys("2026-02-01");
    textArea.sendKeys("party Time!")
    driver.findElements(By.xpath("//button[text() = 'Submit']")).click();
    WebElement message = wait.until(ExceptedConditions.visibilityOfElementLocated(By.id("actionconformatiion")));
    System.out.println(message.getText());
    driver.quit();
}
}