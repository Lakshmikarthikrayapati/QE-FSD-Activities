package demos;


import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class activity6 {
    public static void main(String[] args, Object remove_button) {
        WebDriver driver = new FirefoxDriver();
        driver.get("https://training.support.net/webelements/dynamic-controls");
        System.out.println(driver.getTitle());

        WebElement checkbox = driver.findElement(By.xpath("//input[@id = 'checkbox']"));
        System.out.println(checkbox.isSelected());
        checkbox.click();

        System.out.println(checkbox.isSelected());

        driver.quit();

}
 }