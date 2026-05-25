---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 330}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *zombie staff* is etched with the rotting visage of an undead humanoid grimacing in terror and dismay carved atop it. The staff's *summon undead* spells can summon only undead that have flesh and an Intelligence modifier of –4 or lower.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list. If you cast *summon undead*, you can also cast *protect companion* on the resulting minion as a free action.

- **Cantrip** [[Protect Companion]]
- **1st** [[Necromancer's Generosity]], [[Summon Undead]]
- **2nd** [[Final Sacrifice]], [[Summon Undead]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
