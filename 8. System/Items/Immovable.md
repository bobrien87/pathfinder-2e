---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]"]
price: "{'gp': 1800}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rune utilizes magical principles to manipulate gravity and turn you into an immovable object.

**Activate**`pf2:1` (manipulate)

**Frequency** once per day

**Effect** Your armor anchors you in place, even defying gravity, rendering you [[Immobilized]] until you Dismiss the Activation. While you're immobilized in this way, you can be moved only if a creature succeeds at a DC 40 [[Athletics]] check to [[Force Open]] your armor. You can also be moved if 8,000 pounds of pressure are placed upon you, though this is likely fatal.

**Source:** `= this.source` (`= this.source-type`)
