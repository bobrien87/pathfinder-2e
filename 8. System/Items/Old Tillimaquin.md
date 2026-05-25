---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]"]
price: "{'gp': 2000}"
usage: "other"
bulk: "3"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This beloved tavern mascot is a shabby old stuffed beast mounted on an immense slab of ironwood. The beast is roughly the size and shape of a wolverine but with a broader snout, blue stripes along its upper legs and bristled back, and a club of spiked bone at the end of its long tail. No one can recall where *Old Tillimaquin* originally came from, how the taxidermic beast came to stand in its tavern, or even whether it's a genuine article. The tradition of rubbing its bronzed claws for good luck has been observed for so long that the front claws are worn to stubs. Local belief holds that as long as Old Tillimaquin stands, neither fire nor flood will claim its town.

**Activate—Luck of the Mascot** `pf2:1` (fortune, manipulate, occult)

**Frequency** once per month

**Effect** You rub *Old Tillimaquin*'s bronzed claws for good luck before setting out on a task that might benefit the town. You can reroll a single failed saving throw within the next 24 hours, but you must take the second result, even if it's worse than your original result. Each person who rubs the claws can benefit only once per month, but there's no limit to how many people can draw on *Old Tillimaquin*'s luck.

**Source:** `= this.source` (`= this.source-type`)
