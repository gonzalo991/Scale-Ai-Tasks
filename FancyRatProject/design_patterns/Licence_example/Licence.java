public class License {

    private String dni;
    private String category;
    private String type;

    public License() {}

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String seeDetail() {
        return String.format("DNI: %s\nLicense: %s%s", dni, category, type);
    }
}
