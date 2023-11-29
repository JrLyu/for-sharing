public class SwearFilter {
    public static void main(String[] args) {
        String text = "A duck was sailing on a ship shipping whole wheat bread. Duck that SHIP!!!";
        String[] swear = new String[]{"duck", "ShIP", "WhoLe"};
        System.out.println(swearFilter(text, swear));

        text = "A duck was sailing on a ship shipping whole wheat bread. Duck that SHIP!!!";
        swear = new String[] {"DUCK", "shiP", "Whole"};
        // A d**k was sailing on a s**p s**pping w***e wheat bread. D**k that S**P!!!
        System.out.println(swearFilter(text, swear));

//        text = "duckduckingducker motherducker";
//        swear = new String[] {"duck"};
//        // d**kd**kingd**ker motherd**ker
//        System.out.println(swearFilter(text, swear));

        text = "beach";
        swear = new String[] {"beach"};
        // b***h
        System.out.println(swearFilter(text, swear));

        text = "";
        swear = new String[] {"beach"};
        //
        System.out.println(swearFilter(text, swear));

        text = "beach";
        swear = new String[] {};
        // beach
        System.out.println(swearFilter(text, swear));

//        text = "I wish you to bless your heart for good blessing";
//        swear = new String[] {"I", "to", "you", "for", "", "heart", "bless", "wish"};
//        // I w**h y*u to b***s y*ur h***t f*r good b***sing
//        System.out.println(swearFilter(text, swear));
    }

    public static String swearFilter(String text, String[] swear) {
        String result = "";
        int countSpace = 0;
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') {
                countSpace++;
            }
        }
        String[] words = new String[countSpace + 1];
        int index = 0;
        int n = 0;
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') {
                words[index] = text.substring(n, i);
                index++;
                n = i + 1;
            }
        }
        words[countSpace] = text.substring(n);
        for (int i = 0; i < words.length; i++) {
            String word = words[i].toLowerCase();
            boolean isSwear = false;
            for (int j = 0; j < swear.length; j++) {
                for (int k = 0; k < word.length() - swear[j].length() + 1; k++) {
                    String part = word.substring(k, swear[j].length());
                    if (part.equals(swear[j].toLowerCase())) {
                        isSwear = true;
                        result += words[i].charAt(0);
                        for (int m = 0; m < swear[j].length() - 2; m++) {
                            result += "*";
                        }
                        result += words[i].substring(swear[j].length() - 1) + " ";
                    }
                }
            }
            if (!isSwear) {
                result += words[i] + " ";
            }
        }
        return result;
    }
}
