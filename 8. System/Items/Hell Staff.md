---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]", "[[Unholy]]"]
price: "{'gp': 13000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *hell staff* is a tall, pointed staff forged of red-tinted steel with Diabolic inscriptions that march neatly down its sides. At its top sits an inverted ruby pyramid divided into nine sections. Found mostly in Cheliax or other lands where diabolic influences hold sway, when used as a weapon the staff is a *+3 greater striking flaming unholy staff*. When you prepare this staff, if you're holy, you become [[Drained]] 1 until your next daily preparations.

The staff's *summon lesser servitor spell* can be used only to summon animals with the fiend trait, devils, or hell hounds (at 4th rank). Its *summon fiend* spell can summon only devils or hell hounds.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Divine Lance]]
- **1st** [[Protection]], [[Summon Lesser Servitor]]
- **2nd** [[Darkvision]], [[Summon Lesser Servitor]]
- **3rd** [[Chilling Darkness]], [[Darkvision]], [[Summon Lesser Servitor]]
- **4th** [[Divine Wrath]], [[Summon Lesser Servitor]]
- **5th** [[Darkvision]], [[Divine Immolation]], [[Summon Fiend]]
- **6th** [[Devil Form]], [[Summon Fiend]]
- **7th** [[Divine Decree]], [[Summon Fiend]]

**Craft Requirements** You're unholy. Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
