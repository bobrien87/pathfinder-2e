---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Illusion]]", "[[Magical]]", "[[Structure]]"]
price: "{'gp': 900}"
usage: "carried"
bulk: "3"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This three-panel folding backdrop measures 5 feet tall and 3 feet wide and takes 2 hands to carry when folded up. It projects a preset illusion when fully unfolded. Illusory backdrops are typically used by artists, bards, gallery owners, and the occasional politician, and common illusions include the tops of battlements with grand castles in the background, cozy bowers, and well-appointed rooms.

**Activate—Set the Scene** 1 minute (manipulate)

**Effect** You unfold the illusory backdrop, placing it on the edge of three contiguous 5-foot squares in a straight line. The illusion then emanates in a @Template[type:cone|distance:15] from the center of the line, facing straight away from the panel. The illusion contains a scene that includes up to 5 discrete objects (usually foliage or pieces of furniture). The scene is static and lasts for 1 hour, though that duration restarts if the backdrop is refolded and then unfolded again. The appearance of the illusion is determined when the illusory backdrop is crafted and can't be changed.

**Source:** `= this.source` (`= this.source-type`)
