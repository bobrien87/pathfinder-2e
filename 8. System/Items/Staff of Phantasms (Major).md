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

This ornate metal staff shines with precious inlays of gold. When you Cast a Spell from the staff, the illusory image of something you desire flashes across its surface. While wielding the staff, you gain a +2 status bonus to checks to disbelieve an illusion.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Figment]]

- **1st** [[Illusory Disguise]], [[Illusory Object]]

- **2nd** [[Illusory Creature]], [[Illusory Object]], [[Item Facade]]

- **3rd** [[Illusory Disguise]], [[Item Facade]]

- **4th** [[Illusory Creature]], [[Illusory Scene]], [[Illusory Disguise]]

- **5th** [[Illusory Creature]], [[Illusory Scene]]

- **6th** [[Hallucination]], [[Mislead]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
