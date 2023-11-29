public class Circle extends GeometricObject{
    private double radius;
    Circle(double r) {
        radius = r;
    }
    public double getArea() {
        return 3.14 * radius * radius;
    }
}
