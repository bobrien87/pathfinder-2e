---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Companion]]", "[[Invested]]", "[[Primal]]"]
price: "{'gp': 125}"
usage: "worncollar"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This unobtrusive collar is made to hide beneath an animal's fur or blend in against scaled skin. It's most often used by unscrupulous trophy hunters hoping to make a name for themselves by defeating threats they artificially created, using hapless animals as pawns.

A *chaos collar* fuses to its animal bearer the first time it's clasped around the creature's neck. Three nights per month, it transforms the animal into the form of a terrifying monster. The appearance is the same size as the original animal and doesn't change the animal's statistics, but it's always something new, horrifying, and unique to that particular *chaos collar*. The transformation lasts from dusk until dawn, and it occurs with complete randomness throughout the month.

An animal slain while wearing a *chaos collar* remains in the form it had at the time of its death. Once its bearer dies, the collar transforms into a scrap of dirty string and falls off, where the unscrupulous hunter can collect and use it again.

**Source:** `= this.source` (`= this.source-type`)
