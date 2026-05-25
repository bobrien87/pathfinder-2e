---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 480, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This satchel is made of finely worked leather and stitched with golden thread. A complex pattern of trees, leaves, and vines covers its surface. The satchel always contains a bulk of seeds, and drawing one from the bag results in a random tree or crop plant seed.

**Activate—Seed of Safety** `pf2:2` (manipulate, primal)

**Frequency** once per day

**Effect** You draw a seed and cast it into a space within 30 feet. The satchel casts protector tree (Player Core 2 249) as a 2nd-rank spell.

**Activate—Seed of Sustenance** `pf2:2` (healing, manipulate, primal)

**Frequency** once per day

**Effect** You draw a seed and cast it into a space within 30 feet. A small tree sprouts within 10 minutes, producing 5 fruits. A creature who eats the fruit with an Interact action regains @Damage[(1d6+2)[healing]] Hit Points and receives as much nourishment as one meal for a typical human. After an hour, the tree and all its fruits wither away.

**Source:** `= this.source` (`= this.source-type`)
