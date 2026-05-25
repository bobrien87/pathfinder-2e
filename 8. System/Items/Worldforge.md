---
type: item
source-type: "Remaster"
level: "25"
traits: ["[[Artifact]]", "[[Invested]]", "[[Magical]]", "[[Mythic]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "15"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Mounted upon a base of iron, inscribed with innumerable runes, this immense anvil can be used to forge nearly anything into reality. Stories claim that even metaphorical and abstract concepts, including "a graveknight's mercy" and "the tears of a living wildfire" have been hammered into solid shape upon *Worldforge*, though the tales disagree about what form those objects took.

The cost of using *Worldforge*, however, is prohibitive for mere mortals. In addition to the fuel and metal it consumes, *Worldforge* draws upon the user's physical and spiritual strength to sustain the act of creation. The demand of its magic is such that no one save gods, or those who are nearly gods, can use it and survive.

**Activate—Wondrous Forge** (downtime, manipulate)

**Requirements** You have the ability to make a Crafting check at mythic proficiency (such as that granted by the Artisan's Calling)

**Effect** After spending 2 days setting up the work (or 1 if you have the desired item's formula) and supplying *Worldforge* with adequate raw materials (as determined by the GM), you attempt to Craft something upon it. The DC and final cost of the item is also determined by the GM. For each day you spend Crafting, you must expend a Mythic Point or your [[Drained]] condition increases by 1; this condition can't be reduced until you have finished Crafting the item or you abandon the project. Each day spent Crafting upon the *Worldforge* counts as 10 days of normal Crafting time. If the value of your drained condition reaches 4, you must attempt a DC 46 [[Fortitude]] save or die. If you fail this save or if you abandon the activity, what remains of your project shatters irrecoverably into a multitude of useless fragments.

**Destruction** *Worldforge* can't be destroyed as long as [[Torag]] maintains his divinity.

**Source:** `= this.source` (`= this.source-type`)
