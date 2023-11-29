public class Main {
    // Structure:
    // GeometricObject:
    //      -- Circle
    //      -- Rectangle
    // Animal:
    //      -- Bird
    // ParameterizedClass<T extends GeometricObject>:
    //      -- twoTimesArea(T): T needs to be subclasses of GeometricObject
    //      -- twoTimesWeight(T extends Animal): T needs to be subclasses of Animal

    public static void main(String[] args) {
        Circle circle = new Circle(3);
        Rectangle rectangle = new Rectangle(3, 4);
        GeometricObject object = rectangle;
        Bird bird = new Bird("myBird", 20);

        ParametrizedClass<GeometricObject> p1 = new ParametrizedClass<>();

        System.out.println(p1.twoTimesArea(circle)); // rectangle/object would also work;
                                                     // however, bird is not working
        System.out.println(p1.twoTimesWeight(bird)); // will work: in the method, T is Animal

        ParametrizedClass<Circle> p2 = new ParametrizedClass<>();
        System.out.println(p2.twoTimesArea(circle)); // only circle will work: T now is Circle

        // ParametrizedClass<Bird> p3 = new ParametrizedClass<>(); // error!
                                                                   // Bird is not a subclass of GeometricObject
                                                                   // Animal will also fail
    }
}
