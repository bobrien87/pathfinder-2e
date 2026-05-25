---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 4100}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A large, stylized symbol of an eye adorns the top of this wooden staff, representing the watchful eye of the divine powers. The bearer of the staff can guide and protect, seeing bounties and tragedies that could befall them in the future. When wielding this staff, you gain a +1 item bonus to Survival checks to [[Sense Direction]] or [[Subsist]] and to Religion checks to [[Recall Knowledge]].

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Guidance]]
- **1st** [[Bless]], [[Create Water]]
- **2nd** [[Augury]], [[Create Food]], [[See the Unseen]], [[Status]]
- **3rd** [[Safe Passage]], [[Wanderer's Guide]]
- **4th** [[Cleanse Affliction]], [[Dispelling Globe]], [[Status]]
- **5th** [[Dispelling Globe]], [[Scouting Eye]], [[See the Unseen]]
- **6th** [[Dispelling Globe]], [[Scintillating Safeguard]], [[Truesight]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
