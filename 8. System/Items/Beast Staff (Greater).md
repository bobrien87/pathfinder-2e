---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The visages of beasts are carved into the painted wood of a *beast staff*, with a large head on top. When used as a weapon, the staff is a *+2 striking staff*. While wielding the staff while you have it prepared, you're affected by [[Speak with Animals]]. If you have [[Animal Empathy]], you gain a +2 circumstance bonus on checks using it.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Gouging Claw]]

- **1st** [[Runic Body]], [[Pest Form]]

- **2nd** [[Animal Form]], [[Enlarge]]

- **3rd** [[Animal Form]], [[Insect Form]]

- **4th** [[Animal Form]], [[Bestial Curse]], [[Insect Form]], [[Pest Form]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
