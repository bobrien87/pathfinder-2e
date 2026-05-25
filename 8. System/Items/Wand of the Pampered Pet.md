---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Extradimensional]]", "[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 75, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This extravagant wand is made of gold and capped with a large, sparkling gemstone. Its handle is wrapped in plush, padded fabric.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Pet Cache]] but the accommodations inside the extradimensional space are luxurious and spacious. The food is delicious gourmet cuisine tailored to the pet's palate, the habitat is the perfect temperature and environment for the pet, complete with comfortable bed or lounging area. A pair of phantom hands pamper the pet, patting, grooming, or playing with it at the creature's whim.

**Craft Requirements** Supply a casting of [[Pet Cache]].

**Source:** `= this.source` (`= this.source-type`)
