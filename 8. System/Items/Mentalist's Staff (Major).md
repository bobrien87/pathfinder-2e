---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1800}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This polished wooden staff bears a swirling motif reminiscent of the folds of a brain. While wielding the staff, you gain a +2 circumstance bonus to checks to identify mental magic.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Daze]]

- **1st** [[Mindlink]] [[Phantom Pain]]

- **2nd** [[Paranoia]]

- **3rd** [[Hypercognition]] [[Phantom Pain]]

- **4th** [[Rewrite Memory]] [[Telepathy]]

- **5th** [[Hallucination]] [[Phantom Pain]] [[Synaptic Pulse]]

**Craft Requirements** Supply one casting of all listed levels of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
