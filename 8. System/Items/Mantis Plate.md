---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Bulwark]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 2800}"
bulk: "4"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The beautiful plates of this *+2 resilient Greater Ready full plate* armor are shaped from the carapace of a deadly mantis, providing excellent protection with added flexibility. When wearing a suit of mantis plate, you gain a +2 item bonus to your Athletics DC.

**Activate—Mandible Vambraces** `pf2:2` (concentrate, manipulate)

**Effect** Make a melee Strike. If you succeed, the target is caught by the spikes on the armor's forearms, taking an additional 6d6 piercing damage (DC 30 [[Reflex]] save).

**Craft Requirements** The initial raw materials must include the arms and carapace of a deadly mantis.

**Source:** `= this.source` (`= this.source-type`)
