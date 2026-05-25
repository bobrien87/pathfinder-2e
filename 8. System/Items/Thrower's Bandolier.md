---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bandolier is covered in straps and pouches capable of holding up to 2 Bulk of one-handed thrown weapons. A thrower's bandolier has a *+1 weapon potency rune* etched into it, and it can be etched with runes as though it were a one-handed thrown weapon. When you invest the thrower's bandolier, you can attune it to all the weapons sheathed in it (this ends any previous attunements made with the bandolier). Whenever you draw a weapon from the bandolier, the bandolier's runes are replicated onto that weapon. Any runes already on the weapon are suppressed, and any runes previously replicated to a different weapon in this way are removed, returning it to normal.

**Activate** `pf2:2` (concentrate, manipulate)

**Effect** All weapons attuned to the bandolier, not including any weapons you're currently wielding, return to the bandolier.

**Source:** `= this.source` (`= this.source-type`)
