---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 160}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** Your Strike with the affixed weapon was a critical success.

The bright red tassels of the creature known as Taljjae are a ubiquitous motif in Hwanggot and are used as charms to pray for good fortune and reward for great effort. They adorn clothing, weapons, and even drinking gourds. These particular tassels carry within them a potent fraction of the mysterious fey's power. When you activate a Taljjae tassel, your weapon gains the properties of the [[Grievous]] rune for the duration of the triggering attack.

**Source:** `= this.source` (`= this.source-type`)
