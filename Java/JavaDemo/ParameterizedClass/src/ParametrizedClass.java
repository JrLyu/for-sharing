public class ParametrizedClass<T extends GeometricObject> {
    public double twoTimesArea(T geometricObject) {
        return geometricObject.getArea() * 2;
    }

    public <T extends Animal>double twoTimesWeight(T animal) {
        return animal.getWeight() * 2;
    }

    public static void main(String[] args) {
        // ParametrizedClass<T> p = new ParametrizedClass<>(); // error: not sure what is T
    }
}