// hash_table.h
typedef struct ht_item {
  char *key;
  char *value;
};

typedef struct ht_hash {
  int size;
  int count;
  ht_item **items;
};