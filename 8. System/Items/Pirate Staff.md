---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 2000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Carved of salt-stained driftwood white with the salt of the sea, a *pirate staff* has jewels and gold pieces embedded in the wood. A skull and crossbones sit on top. When used as a weapon, the staff is a *+2 striking fearsome* staff. While wielding the staff, you gain a +2 circumstance bonus to Intimidation checks to [[Coerce]].

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Gale Blast]], [[Know the Way]]
- **1st** [[Seashell of Stolen Sound]]
- **2nd** [[Mist]], [[Water Breathing]], [[Water Walk]]
- **3rd** [[Mind of Menace]], [[Water Breathing]]
- **4th** [[Coral Eruption]], [[Water Breathing]], [[Water Walk]]
- **5th** [[Flowing Strike]], [[Mariner's Curse]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
