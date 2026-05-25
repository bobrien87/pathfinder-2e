---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 4000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The stone head piece of this smooth wooden staff is carved to look like a lidless eye. While wielding it, you gain a +1 status bonus to Perception checks made for initiative.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Detect Magic]]
- **1st** [[Sure Strike]]
- **2nd** [[Darkvision]], [[See the Unseen]], [[Translate]]
- **3rd** [[Darkvision]], [[Mind Reading]]
- **4th** [[Clairvoyance]], [[Detect Scrying]], [[Telepathy]]
- **5th** [[Mind Probe]], [[Scouting Eye]]
- **6th** [[Telepathy]], [[Truesight]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
