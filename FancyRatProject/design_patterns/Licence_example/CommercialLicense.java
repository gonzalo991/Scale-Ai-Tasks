public class CommercialLicense {

private License license;

public CommercialLicense(String dni, String category, String type) {

    license = new License();
    license.setDNI(dni);
    license.setCategory(category);
    license.setType(type);
}

public void seeDetail() {
    license.seeDetail();
}

}