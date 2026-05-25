---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Companion]]", "[[Magical]]"]
price: "{'gp': 35}"
usage: "affixed-to-harness"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This charm, usually placed on an animal companion's collar, contains a single strand of your hair, as well as one of your animal companion's, creating a link that better transmits emotional cues to a trained psychological assistance animal.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** You attempt a saving throw against an emotion effect

**Requirements** Your animal companion wearing the empathy charm is within 10 feet

**Effect** Your animal companion senses the effect and attempts to calm you. You gain a +1 circumstance bonus against the triggering save.

**Source:** `= this.source` (`= this.source-type`)
