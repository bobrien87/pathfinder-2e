---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 80}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Some troops wear this plume of short feathers in their hats as part of a formal uniform, but the soft glow emanating from it can be useful elsewhere. While wearing the *shining hackle*, you gain a +1 item bonus to Perception checks based on sight, but you also take a –1 item penalty to your Stealth checks.

**Activate—Glowing Hackle** `pf2:1` (concentrate, light)

**Effect** Your *shining hackle* glows even brighter, shedding bright light in a 20-foot radius (and dim light for the next 20 feet). This effect lasts until you Dismiss it.

**Source:** `= this.source` (`= this.source-type`)
