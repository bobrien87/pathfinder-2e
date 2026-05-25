---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]"]
price: "{'gp': 150}"
usage: "worngloves"
bulk: "—"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Glowing runes cover these *+1 striking handwraps of mighty blows*. When you critically hit an enemy with a Strike as part of a [[Flurry of Blows]], you can regain @Damage[4[healing,vitality]|traits:healing,vitality]{4 Hit Points}. This is a healing vitality effect. The handwraps can heal you only once every 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
