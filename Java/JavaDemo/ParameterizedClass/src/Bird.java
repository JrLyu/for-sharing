public class Bird extends Animal{
    private String name;
    private double weight;
    Bird(String s, double w) {
        name = s;
        weight = w;
    }

    public double getWeight() {
        return weight;
    }
}
