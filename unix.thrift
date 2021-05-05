namespace experiment

struct RequestMeta {
    1: string id;
}

struct Locale {
  1: string language;
  2: optional string script;
  3: optional string country;
}

enum TagType {
  CONVERSATION,
  USER,
  QUEUE
}
