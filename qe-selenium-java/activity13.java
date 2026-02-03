package demos;
import java.util.List;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;


public class activity13 {
    public static void main(String[] args) {
    WebDriver driver = new FirefoxDriver();
    driver.get("https://training-support.net/webelements/tables");
    System.out.println("Title of the page: " + driver.getTitle());
    List<WebElement> rows = driver.findElements(By.xpath("//table/tbody/tr"));
    List<WebElement> cols = driver.findElements(By.xpath("//table/thead/tr/th"));
    System.out.println(cols.size());
    System.out.println(rows.size());
    List<WebElement> cellValuesOfRow = driver.findElements(By.xpath("//table/tbody/tr[3]/td"));
    for(WebElement cellValue : cellValuesOfRow) {
        System.out.println(cellValue.getText());
    }
    WebElement cellValue = driver.findElement(By.xpath("//table/tbody/tr[2]/td"));
    driver.quit();
}
}