---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Poison]]", "[[Splash]]"]
price: "{'gp': 3750}"
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

Concentrated wolfsbane and other anti-shapechanger reagents fill trueshape bombs. These bombs grant a +3 item bonus to attack rolls and deal 4d6 poison damage, 4d4 persistent poison damage, and 4 poison splash damage. If the primary target is under the effects of a morph or polymorph effect, it must succeed at a DC 40 [[Fortitude]] save saving throw, or else the effects end and the creature returns to its normal form. Targets taking persistent poison damage from this bomb must succeed at another Fortitude saving throw at the same DC to change shape using a morph or polymorph effect. The persistent damage can last up to 1 minute.

**Source:** `= this.source` (`= this.source-type`)
