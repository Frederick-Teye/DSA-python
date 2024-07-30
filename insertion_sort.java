public class insertion_sort {

  public static void main(String[] args) {
    int[] list = { 9, 4, 6, 7, 2, 8, 1, 3 };

    insertionSort(list);

    for (int i = 0; i < list.length; i++) {
      System.out.print(i + " ");
    }
  }

  public static void insertionSort(int[] list) {
    for (int i = 1; i < list.length; i++) {
      int key = list[i];
      int j = i - 1;

      while (j >= 0 && list[j] > key) {
        list[j + 1] = list[j];
        j--;
      }

      list[j + 1] = key;

    }
  }
}
