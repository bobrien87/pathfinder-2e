---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This staff of magically hardened wood is topped with a silver sculpture depicting magical runic symbols. A staff of arcane might is a *+1 striking staff*.

**Activate—Sunder** `pf2:2` (death, force, manipulate)

**Effect** You destroy the staff, unleashing a blast of arcane power in a @Template[cone|distance:30], dealing 2d6 force damage per charge remaining in the staff with a DC 30 [[Reflex]] save.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Detect Magic]]

- **1st** [[Phantasmal Minion]]

- **2nd** [[Everlight]]

- **3rd** [[Force Barrage]], [[Paralyze]]

- **4th** [[Dispelling Globe]], [[Mystic Armor]], [[Translocate]]

- **5th** [[Fireball]], [[Force Barrage]], [[Lightning Bolt]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
