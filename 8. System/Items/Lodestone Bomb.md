---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Force]]", "[[Splash]]"]
price: "{'gp': 400}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

Lodestone bombs hold reactive ionized minerals preserved in a dormant state until broken. The bomb grants a +2 item bonus to attack rolls and deals 3d4 force damage and 2 force splash damage. In addition, a target made of metal, wearing metal armor, or using metal weapons takes 2d4 persistent,force and is [[Clumsy]] 1 and [[Enfeebled]] 1 while taking the persistent damage. The persistent damage can last up to 1 minute.

**Source:** `= this.source` (`= this.source-type`)
