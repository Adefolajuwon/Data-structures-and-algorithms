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
// hash_table.h
void ht_insert(ht_hash_table *ht, const char *key, const char *value);
char *ht_search(ht_hash_table *ht, const char *key);
void ht_delete(ht_hash_table *h, const char *key);