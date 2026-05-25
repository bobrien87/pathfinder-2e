---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Air]]", "[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 95}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This staff is made of a dense wood and strikes the ground with an imposing boom. At the top of the staff is a perfectly round obsidian sphere that, when stared at for too long, makes viewers feel as though they're heavier than before. When wielding this staff, you gain a +1 item bonus to saves against forced movement.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Gale Blast]]
- **1st** [[Air Bubble]], [[Gravitational Pull]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
