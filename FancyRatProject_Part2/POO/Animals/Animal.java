public abstract class Animal {
    // Define protected attributes
    protected String name;
    protected String breed;
    protected String species;
    protected String skinColor;
    protected boolean isTerrestrial;

    // Define constructor
    public Animal(String name, String breed, String species, String skinColor, boolean isTerrestrial) {
        this.name = name;
        this.breed = breed;
        this.species = species;
        this.skinColor = skinColor;
        this.isTerrestrial = isTerrestrial;
    }

    // Define get and set methods
    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBreed() {
        return this.breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }

    public String getSpecies() {
        return this.species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }

    public String getSkinColor() {
        return this.skinColor;
    }

    public void setSkinColor(String skinColor) {
        this.skinColor = skinColor;
    }

    public boolean isTerrestrial() {
        return this.isTerrestrial;
    }

    public void setIsTerrestrial(boolean isTerrestrial) {
        this.isTerrestrial = isTerrestrial;
    }

    @Override
    public String toString() {
        return "Animal [name=" + name + ", breed=" + breed + ", species=" + species + ", skinColor=" + skinColor
                + ", isTerrestrial=" + isTerrestrial + "]";
    }

    
}