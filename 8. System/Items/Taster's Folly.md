---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Devised to bypass detection, a dose of taster's folly consists of two compounds that aren't mixed but placed in the contents of one meal. Each compound is harmless on its own. The DC to Recall Knowledge about this poison from one of its components is 23 and attempts to use magic to detect the unmixed components require a successful DC 23 counteract check. The onset period begins only if a victim consumes both compounds during the same hour. If the two compounds mix prior to consumption, they become toxic and are detectable as such. The sickened condition can't be ended until the poison's effects end.

**Saving Throw** DC 21 [[Fortitude]] save

**Onset** 10 minutes

**Maximum Duration** 6 minutes

**Stage 1** 2d4 poison damage (1 minute)

**Stage 2** 3d4 poison damage and [[Sickened]] 1 (1 minute)

**Stage 3** 4d4 poison damage and sickened 1 (1 minute)

**Source:** `= this.source` (`= this.source-type`)
