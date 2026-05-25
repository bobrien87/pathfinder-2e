---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Fire]]", "[[Magical]]", "[[Versatile p]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Smoke constantly belches from this +1 magic longsword. Any successful Strike with this sword deals 1 extra fire damage. You can use a special action to make the blade's edges light on fire.

**Activate—Stoke Flames** `pf2:1` (concentrate)

Until the end of your turn, the blade deals 1d6 extra fire damage instead of just 1. After you use this action, you can't use it again for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
