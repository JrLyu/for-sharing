public class Rectangle extends GeometricObject{
    private double width;
    private double height;

    Rectangle(double w, double h) {
        width = w;
        height = h;
    }

    public double getArea() {
        return width * height;
    }
}
