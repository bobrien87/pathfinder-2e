---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Metal]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 4000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This cylindrical iron staff has colored segments on both ends, one red and one blue. When you Strike with the staff, you gain a +1 circumstance bonus to the attack roll if the target is wearing metal armor or is primarily made of metal.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrips** [[Detect Metal]]

- **1st** [[Conductive Weapon]], [[Shielded Arm]]

- **2nd** [[Magnetic Attraction]], [[Magnetic Repulsion]]

- **3rd** [[Magnetic Acceleration]], [[Noxious Metals]]

- **4th** [[Mercurial Stride]], [[Rust Cloud]]

- **5th** [[Magnetic Repulsion]], [[Impaling Spike]]

- **6th** [[Field of Razors]], [[Magnetic Acceleration]]

**Source:** `= this.source` (`= this.source-type`)
