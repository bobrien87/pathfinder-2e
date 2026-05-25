---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Iron strips line the body of an *accursed staff*, capping the bottom and folding into an intricate knot at the top. While wielding an *accursed staff*, you're empowered by the curses you inflict. If an enemy fails a saving throw against a spell you cast that has the curse trait, you gain temporary Hit Points equal to double that spell's rank. These temporary Hit Points last 10 minutes. The enemy must be a significant threat and can't have been a willing subject of the curse.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Daze]]
- **1st** [[Bane]], [[Ill Omen]]
- **2nd** [[Blood Vendetta]], [[Warrior's Regret]]
- **3rd** [[Claim Curse]], [[Cup of Dust]]
- **4th** [[Cleanse Affliction]], [[Outcast's Curse]], [[Warrior's Regret]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
