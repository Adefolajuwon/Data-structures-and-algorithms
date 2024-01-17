// hash_table.h
 struct ht_item {
  char *key;
  char *value;
};

 struct ht_hash_table {
  int size;
  int count;
  ht_item **items;
};