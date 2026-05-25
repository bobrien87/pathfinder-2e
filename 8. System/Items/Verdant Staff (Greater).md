---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1750}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This oak branch grows leaves in spring that change color in autumn and shed in winter. While wielding it, you gain a +2 circumstance bonus to checks to identify plants and fungi.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrips** [[Tangle Vine]]

- **1st** [[Runic Body]], [[Runic Weapon]]

- **2nd** [[Entangling Flora]], [[Oaken Resilience]], [[One with Plants]], [[Shape Wood]]

- **3rd** [[Wall of Thorns]], [[Speak with Plants]]

- **4th** [[Oaken Resilience]], [[Speak with Plants]]

- **5th** [[Plant Form]], [[Wall of Thorns]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
