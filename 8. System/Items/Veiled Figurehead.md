---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Figurehead]]", "[[Magical]]", "[[Water]]"]
price: "{'gp': 335}"
usage: "attached-to-ships-bow"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** attached to a ship's bow

This figurehead is carved in the shape of a humanoid, but it has no facial features whatsoever.

**Activate—Veil!** 1 minute (concentrate, illusion, visual)

**Frequency** once per day

**Effect** You change the appearance of the ship in minor but noticeable ways. Its general size and shape can't be changed, but you can alter surface details to your liking. Flags and sails can be recolored and given new markings, and the overall material of the ship can appear a different color or quality. Wear and surface damage (like small holes, tears, and burns) can be masked to make the vessel look unblemished, or you can create such damage and wear. The figurehead itself shifts to fit the change and gains a face to match the rest of the ship. The illusion lasts for 6 hours or until you Dismiss this effect. Any creature that boards the ship or uses the [[Seek]] action to examine it disbelieves the illusion if it succeeds at a DC 25 [[Perception]] check.

**Source:** `= this.source` (`= this.source-type`)
