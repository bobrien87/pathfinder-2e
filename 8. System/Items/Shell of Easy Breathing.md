---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]", "[[Water]]"]
price: "{'gp': 160}"
usage: "other"
bulk: "2"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large salt-encrusted seashell is more than 2 feet across, with images of deep sea creatures carved around its edge.

**Activate—Fill the Shell** `pf2:1` (manipulate)

**Effect** You place the shell on a level surface and sprinkle a few drops of water into its basin. The shell slowly fills with saltwater over the course of 1 minute. The shell's magic then becomes active, indicated by a steady stream of bubbles. Moving the shell disturbs its contents, causing the item to deactivate and the water inside to evaporate; otherwise, it remains activated for an unlimited duration. While the shell is activated, a creature can submerge its head and let water and bubbles fill its nose and mouth (or whatever body part it uses for breathing) as a 3-action activity. For the next hour, the creature can breathe underwater. The creature is then temporarily immune to *shells of easy breathing* until the next time it makes its daily preparations.

**Source:** `= this.source` (`= this.source-type`)
