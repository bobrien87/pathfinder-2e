---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 70000, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Multicolored threads are woven through this magical banner, causing it to appear purple in some light and green in others. The shimmering light offers hope and safety in the face of powerful magic wielders. You and allies within the banner's aura gain resistance 10 to damage from spells; for spells that apply multiple instances of damage, such as [[Force Barrage]], this applies only to the first instance of damage.

**Source:** `= this.source` (`= this.source-type`)
