---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This twisted and grim-looking staff is adorned with hideous skull and bone motifs. Creatures summoned using this staff gain a number of temporary Hit Points equal to the rank of the spell used to summon them.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Void Warp]]

- **1st** [[Grim Tendrils]], [[Summon Undead]]

- **2nd** [[Peaceful Rest]], [[Summon Undead]]

- **3rd** [[Summon Undead]], [[Vampiric Feast]]

- **4th** [[Summon Undead]], [[Vision of Death]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
