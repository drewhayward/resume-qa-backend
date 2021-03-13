from typing import Optional

from fastapi import FastAPI

from qa_model import build_pipeline

app = FastAPI()

nlp_pipeline = build_pipeline()

text = """
The kangaroo is a marsupial from the family Macropodidae (macropods, meaning "large foot"). In common use the term is used to describe the largest species from this family, the red kangaroo, as well as the antilopine kangaroo, eastern grey kangaroo, and western grey kangaroo.[1] Kangaroos are indigenous to Australia and New Guinea. The Australian government estimates that 34.3 million kangaroos lived within the commercial harvest areas of Australia in 2011, up from 25.1 million one year earlier.[2]

As with the terms "wallaroo" and "wallaby", "kangaroo" refers to a paraphyletic grouping of species. All three refer to members of the same taxonomic family, Macropodidae, and are distinguished according to size. The largest species in the family are called "kangaroos" and the smallest are generally called "wallabies". The term "wallaroos" refers to species of an intermediate size.[3] There are also the tree-kangaroos, another type of macropod, which inhabit the tropical rainforests of New Guinea, far northeastern Queensland and some of the islands in the region. A general idea of the relative size of these informal terms could be:

wallabies: head and body length of 45–105 cm and tail length of 33–75 cm; the dwarf wallaby (the smallest of all known macropod species) is 46 cm long and weighs 1.6 kg;
tree-kangaroos: ranging from Lumholtz's tree-kangaroo: body and head length of 48–65 cm, tail of 60–74 cm, weight of 7.2 kg (16 lb) for males and 5.9 kg (13 lb) for females; to the grizzled tree-kangaroo: length of 75–90 cm (30 to 35 in) and weight of 8–15 kg (18–33 lb);
wallaroos: the black wallaroo (the smallest of the two species) with a tail length of 60–70 cm and weight of 19–22 kg (41.8–48.5 lb) for males and 13 kg (28.6 lb) for females;
kangaroos: a large male can be 2 m (6 ft 7 in) tall and weigh 90 kg (200 lb).
Kangaroos have large, powerful hind legs, large feet adapted for leaping, a long muscular tail for balance, and a small head. Like most marsupials, female kangaroos have a pouch called a marsupium in which joeys complete postnatal development.

The large kangaroos have adapted much better than the smaller macropods to land clearing for pastoral agriculture and habitat changes brought to the Australian landscape by humans. Many of the smaller species are rare and endangered, while kangaroos are relatively plentiful.
"""


@app.get("/question/{q}")
def answer_question(q: str):
    answer = nlp_pipeline(q, text)
    return {"answer": answer}
