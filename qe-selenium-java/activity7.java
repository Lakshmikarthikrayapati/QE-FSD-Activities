package demos;


import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class activity7 {
    public static void main(String[] args, Object remove_button) {
        WebDriver driver = new FirefoxDriver();
        driver.get("https://training.support.net/webelements/dynamic-controls");
        System.out.println(driver.getTitle());

        WebElement textField = driver.findElement(By.xpath("//input[@id = 'textInput']"));
        System.out.println("Is textField enabled? "+ textField.isEnabled());


        driver.findElement(By.xpath("//button[text() = 'Enable Input']")).click();

        System.out.println("Is textField enable? " + textField.isEnabled());

        driver.quit();

}
 }
