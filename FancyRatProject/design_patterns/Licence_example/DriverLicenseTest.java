import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class DriverLicenseTest {

@Test
void testDriverLicense() {
    DriverLicense driverLicense = new DriverLicense("000.000.000-00");
    assertEquals("000.000.000-00", driverLicense.getDNI());
    assertEquals("A", driverLicense.getCategory());
    assertEquals("I", driverLicense.getType());
    driverLicense.seeDetail();
}

}