public class DriverLicense {

private License driverLicense;

public DriverLicense(String dni) {

    driverLicense = new License();
    driverLicense.setDNI(dni);
    driverLicense.setCategory("A");
    driverLicense.setType("I");
}

public void seeDetail() {
    driverLicense.seeDetail();
}

}